import aiohttp
import asyncio
import pyowm
from config import OWM_API_KEY
import json
OWM = pyowm.OWM(OWM_API_KEY)
MGR = OWM.weather_manager()

DATA = []


async def main(lat, lon):
    async with aiohttp.ClientSession() as session:
        resp = await session.get(f'http://api.openweathermap.org/data/2.5/weather?lat='
                                 f'{lat}&lon={lon}&appid={OWM_API_KEY}')
        print(resp.status)
        print(await resp.text())
        DATA.append(await resp.json())

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(
        main(MGR.weather_at_place("New York").location.lat, MGR.weather_at_place("New York").location.lon)),
    loop.create_task(main(MGR.weather_at_place("Boston").location.lat, MGR.weather_at_place("Boston").location.lon)),
    loop.create_task(main(MGR.weather_at_place("Moscow").location.lat, MGR.weather_at_place("Moscow").location.lon)),
]
loop.run_until_complete(asyncio.wait(tasks))

with open('data.json', 'w') as f:
    json.dump(DATA, f)
