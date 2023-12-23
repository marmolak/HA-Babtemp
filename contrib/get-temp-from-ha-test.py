import json

from requests import get
from typing import Dict

token : str = ""
address : str = ""

base_url : str = f"http://{address}:8123/api/states/"
headers : Dict[str, str] = {
    "Authorization": f"Bearer {token}",
    "content-type": "application/json",
}

def get_temp(sensor : str) -> float:
    json_content = json.loads(get(base_url + sensor, headers=headers).text)
    return json_content["state"]


village_celsius : float = get_temp("sensor.babice_s_temperature")
stadla_celsius : float = get_temp("sensor.netatmo_favourite_weather_stations_nfws_bns_tono_stadla_temperature")

print(f"Temperature is {village_celsius} and {stadla_celsius}")
