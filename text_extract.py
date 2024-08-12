import requests
import hidden
url = "https://text-in-images-recognition.p.rapidapi.com/prod"

payload = {
    "objectUrl": "./Scanned_Images/Date20240810_223558/scanned_image_3.jpg"
}

headers = {
    "x-rapidapi-key": hidden.image_text_api_key,
    "x-rapidapi-host": "text-in-images-recognition.p.rapidapi.com",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
