import base64
import numpy as np
import json
import requests
import cv2
from openai import OpenAI
from fastapi import FastAPI
import os
from pydantic import BaseModel
from segment_anything import SamPredictor, sam_model_registry
import torch

os.environ["OPENAI_API_KEY"] = "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"
api_key = "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"

class Item(BaseModel):
    point_x: int
    point_y: int
    image_b64: str

app = FastAPI()

# input point is a numpy array e.g. np.array([123,456])
sam = sam_model_registry["default"](checkpoint="sam_vit_h_4b8939.pth")
if torch.cuda.is_available():
    sam = sam.to(device="cuda")
predictor = SamPredictor(sam)
predictor.reset_image()

def find_bounding_box(bool_array):
    # Find indices where True values occur
    true_indices = np.argwhere(bool_array)
    # Determine bounding box coordinates
    y_min, x_min = true_indices.min(axis=0)
    y_max, x_max = true_indices.max(axis=0) + 1  # Add 1 to include the last pixel
    return x_min, y_min, x_max, y_max

def crop_object(image, bool_array):
    # Find bounding box
    x_min, y_min, x_max, y_max = find_bounding_box(bool_array)
    # Crop the image using the bounding box
    cropped_image = image[y_min:y_max, x_min:x_max]
    return cropped_image

def get_object_detection(byt):

    # Getting the base64 string
    base64_image = base64.b64encode(byt).decode('utf-8')

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": "Write a classification of the main, everyday object in the image. e.g. 'CHEESE', 'GOLF BALL'."
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    return response.json()

def get_wikipedia_article(item):
    language_code = 'en'
    search_query = item
    number_of_results = 1
    headers = {
    # 'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'User-Agent': 'YOUR_APP_NAME (YOUR_EMAIL_OR_CONTACT_PAGE)'
    }

    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    endpoint = '/search/page'
    url = base_url + language_code + endpoint
    parameters = {'q': search_query, 'limit': number_of_results}
    response = requests.get(url, headers=headers, params=parameters)


    response = json.loads(response.text)
    try:
        page = response['pages'][0]

        display_title = page['title']
        article_url = 'https://' + language_code + '.wikipedia.org/wiki/' + page['key']
        
        return page['description']
    except:
        return None

def get_prediction(input_x, input_y):
    input_label = np.array([1])

    masks, scores, logits = predictor.predict(
        point_coords=np.array([[input_x, input_y]]),
        point_labels=input_label,
        multimask_output=False,
    )

    for i, (mask, score) in enumerate(zip(masks, scores)):
        cropped_image = crop_object(image, mask)
    
        return cropped_image

def insert_newline(input_string, line_length=50):
    count = 0
    input_string = list(input_string)
    
    for index, char in enumerate(input_string):
        count += 1
        if count >= line_length and char == ' ':
            input_string[index] = '\n'
            count = 0

    return "".join(input_string)

@app.post("/")
def root(item : Item):
    image = base64.b64decode(item.image_b64);
    image = cv2.imdecode(np.asarray(bytearray(image), dtype='uint8'), cv2.IMREAD_COLOR)
    
    predictor.set_image(image)
    
    masks, scores, logits = predictor.predict(
        point_coords=np.array([[item.point_x, item.point_y]]),
        point_labels=np.array([1]),
        multimask_output=False,
    )
    
    cropped_image = crop_object(image, masks[0])
    (x_min, y_min, x_max, y_max) = find_bounding_box(masks[0])

    detec = get_object_detection(cv2.imencode('.jpeg', cropped_image)[1])
    
    print(detec)
    acc_detec = detec["choices"][0]["message"]["content"]

    description = get_wikipedia_article(acc_detec) or acc_detec

    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"Write/Rewrite a brief (less than 100 words) description of \"{description}\". Targeted at young people and those who want to learn more.\nWrite it after the user says START"},
        {"role": "user", "content": "START"}
    ],
    max_tokens=100
    )

    completion.choices[0].message.content

    return {"item": acc_detec, "description": insert_newline(completion.choices[0].message.content), "bbox": {
        "x_min": int(x_min),
        "y_min": int(y_min),
        "x_max": int(x_max),
        "y_max": int(y_max)
    }}

def main():
    with open("/home/daudi/Downloads/20231119_003006.jpg", "rb") as f:
        x = base64.b64encode(f.read())
    resp = requests.post("http://192.168.243.215:8000/", json={"point_x": 200, "point_y": 200, "image_b64": x.decode('utf-8')})

    le = resp.json()
    print(le)

if __name__=="__main__":
    main()