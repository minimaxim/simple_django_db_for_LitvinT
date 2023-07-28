import json

import requests

url = 'http://127.0.0.1:8000/api/protected/'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwNTM3MDA0LCJpYXQiOjE2OTA1MzY3MDQsImp0aSI6IjI5NDQwMTVlYmM5ZjQ0ZGY5MTMyMGI2NjkxMTRjZTlmIiwidXNlcl9pZCI6MX0.TNtAIpsl2xiDfB8LWzv4PqX5QI-17GYpBAVTP7g1CfU'
headers = {'Authorization': f'Bearer {token}'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)
else:
    print('Ошибка при запросе к API:', response.status_code)
