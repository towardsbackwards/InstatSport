import pyowm
import requests
from datetime import datetime as dt
from datetime import timedelta

from config import OWM_API_KEY

OWM = pyowm.OWM(OWM_API_KEY)


def get_owm_time_country(lon, lat):
    request = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OWM_API_KEY}')
    timezone = request.json()['timezone']
    country = request.json()['sys']['country']
    delta_hours = timezone / 3600
    raw_time = dt.utcnow() + timedelta(hours=delta_hours)
    time = str((raw_time.time()))[:-7]
    weekday = raw_time.strftime("%A")
    result_dict = {'country': country, 'weekday': weekday, 'time': time}
    return result_dict


def get_zone_info(city, only_time_temp=False):
    mgr = OWM.weather_manager()
    observation = mgr.weather_at_place(city)
    lon, lat, city_id = mgr.weather_at_place(city).location.lon, mgr.weather_at_place(
        city).location.lat, mgr.weather_at_place(city).location.id
    time = get_owm_time_country(lon, lat)['time']
    weekday = get_owm_time_country(lon, lat)['weekday']
    country = get_owm_time_country(lon, lat)['country']
    weather = observation.weather
    temp = weather.temperature('celsius')["temp"]
    if only_time_temp:
        return time, temp
    clouds = weather.clouds
    pressure = weather.pressure['press']
    return city, country, temp, clouds, pressure, weekday, time


def handle_text(message):
    time_ny, temp_ny,  = get_zone_info('New York', True)
    row_ny = f'Нью Йорк - {time_ny[:-3]}, {temp_ny}C°'
    time_brx, temp_brx = get_zone_info('Brussels', True)
    row_brx = f'Брюссель - {time_brx[:-3]}, {temp_brx}C°'
    time_syd, temp_syd = get_zone_info('Сидней', True)
    row_syd = f'Сидней - {time_syd[:-3]}, {temp_syd}C°'
    time_rnd, temp_rnd = get_zone_info('Ростов-на-Дону', True)
    row_rnd = f'Ростов-на-Дону - {time_rnd[:-3]}, {temp_rnd}C°'
    time_btsk, temp_btsk = get_zone_info('Батайск', True)
    row_btsk = f'Батайск - {time_btsk[:-3]}, {temp_btsk}C°'


get_zone_info('New York')