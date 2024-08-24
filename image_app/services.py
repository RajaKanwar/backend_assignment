import openai
from PIL import Image
from io import BytesIO
import requests
from django.conf import settings

openai.api_key = 'your_openai_api_key'

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']

def edit_image(image_url, prompt):
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))
    # Add editing logic here
    return image
