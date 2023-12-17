from requests import get
import json

token = ""
address = ""

url = f"http://{address}:8123/api/states/sensor.babice_s_temperature"
headers = {
    "Authorization": f"Bearer {token}",
    "content-type": "application/json",
}

json_content = json.loads(get(url, headers=headers).text)
celsius = json_content["state"]
print(f"Temperature: {celsius}")
