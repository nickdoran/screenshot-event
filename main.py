import base64
from openai import OpenAI

client = OpenAI()

with open("./Images/test1.png", 'rb') as image_file:
    image_bytes = image_file.read()

image_base64 = base64.b64encode(image_bytes).decode('utf-8') 

image_url = f"data:image/png;base64,{image_base64}"

response = client.responses.create(
    model="gpt-5-mini-2025-08-07",
    input=[
        {
            'content': "What day is it in california USA",
            'role': "user",
        }
    ]
)


print(response.output_text)