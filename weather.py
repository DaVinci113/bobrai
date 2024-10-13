import os
from datetime import datetime
import requests
from dotenv import find_dotenv, load_dotenv
from requests import ConnectTimeout, ReadTimeout


load_dotenv(find_dotenv())

weather_token = os.getenv('WEATHER_TOKEN')


def get_data(city, user_id, message):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric&lang=ru'
    
    data = {}
    try:
        response = requests.get(url)
        r = response.json()
        data['Время'] = datetime.now().strftime('%Y-%m-%d %H:%M')
        data['Город'] = r['name']
        data['Температура'] = r['main']['temp']
        data['Ощущаемая температура'] = r['main']['feels_like']
        data['Описание погоды'] = r['weather'][0]['description']
        data['Влажность'] = r['main']['humidity']
        data['Скорость ветра'] = r['wind']['speed']
        return str(f'Время: {data["Время"]}\n'
                   f'Город: {data["Город"]}\n'
                   f'Температура: {data["Температура"]}°C\n'
                   f'Ощущаемая температура: {data["Ощущаемая температура"]}°C\n'
                   f'Описание погоды: {data["Описание погоды"]}\n'
                   f'Влажность: {data["Влажность"]}%\n'
                   f'Скорость ветра: {data["Скорость ветра"]} м/с')
    
    except ConnectTimeout as ex:
        print(ex)
        return 'Ощибка сервиса. Попробуйте ещё раз'
    
    except ReadTimeout as ex:
        return 'Ощибка сервиса. Попробуйте позже'
    
    except Exception as ex:
        return f'Проверь введеные данные'
