import requests
import json


url = "https://world.openfoodfacts.org/api/v0/product/737628064502.json"

try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

response = requests.get(url)

if(response.ok):
    jData = json.loads(response.content)
    val = jData.get('product').get('categories')
    print(val)
else:
    print("nok")
