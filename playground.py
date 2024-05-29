import canvasapi
import requests
from config import access_token, base_url

response = requests.get(f'{base_url}/api/v1/courses/23395/sections',
                                headers={'Authorization': f'Bearer {access_token}'})

json = response.json()

print("done")