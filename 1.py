import requests

def get_data_from_api():
    url = 'http://127.0.0.1:8000/api/users/?format=json'  # Замените на URL вашего JSON API

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок при запросе
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print('Ошибка при запросе к API:', e)
        return None

data = get_data_from_api()
if data is not None:
    # Обработайте данные, полученные из JSON API
    print(data)