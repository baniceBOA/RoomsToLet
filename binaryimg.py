import requests
from PIL import Image
r = requests.get('http://192.168.43.178:5000/get_images')
result = r.json()
for res in result['result']:
    img = Image.open(res)
    