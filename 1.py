import json
import requests

url = 'http://127.0.0.1:8000/api/protected/'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwNTM3NzA1LCJpYXQiOjE2OTA1Mzc0MDUsImp0aSI6ImM4ZGVhNjEzNjNjMjRlYzRiYmNiNTYzNDFiNDNjODExIiwidXNlcl9pZCI6MX0.R0lThwFUIl8dnGMazUJgRrp4LJM9h_2RjD4ilmnCAYQ'
headers = {'Authorization': f'Bearer {token}'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    formatted_data = json.dumps(data, indent=4)

    # Записываем данные в файл "users_data.json"
    with open('users_data.json', 'w') as file:
        file.write(formatted_data)

    print('Данные успешно сохранены в файл "users_data.json"')
else:
    print('Ошибка при запросе к API:', response.status_code)
