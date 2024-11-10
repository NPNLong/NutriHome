import easyocr
import os
import json
from dotenv import load_dotenv
import requests


# Khởi tạo EasyOCR reader
reader = easyocr.Reader(['vi'])


# Đọc và nhận dạng văn bản từ ảnh
image_path = 'openAI/4.jpg'
results = reader.readtext(image_path, detail=0)


all_text = ''
for idx, text in enumerate(results, 1):
    all_text += text + " "


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = os.getenv("GEMINI_API_URL")


headers = {
    'Content-Type': 'application/json',
}


diseases = ["diabetes","obesity"]
allergen = ["dầu cọ"]

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": f"""From the product label of the product.: {all_text}
                    I am allergic to these allergen, please warn me if there is any substance that may be dangerous to my allergy.
                    You just need to list the allergen and warn me and explain in Vietnamese:  {', '.join(allergen) }
                    """
                }
            ]
        }
    ]
}
response = requests.post(API_URL, headers=headers, data=json.dumps(data), params={"key": API_KEY})


if response.status_code == 200:
    response_data = response.json()
    print(response_data['candidates'][0]['content']['parts'][0]['text'])
else:
    print(f"Lỗi khi gọi API Gemini: {response.status_code}")