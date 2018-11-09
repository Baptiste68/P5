iimport requests
import json
import random


#url = "https://world.openfoodfacts.org/api/v0/product/737628064502.json"
url = "https://fr.openfoodfacts.org/categories.json"
response = requests.get(url)

if(response.ok):
    jData = json.loads(response.content)
    val = []
    i = 1
    while i <= 10:
        rand_place = random.randint(0,len(jData.get('tags')) - 1)
        data = jData.get('tags')[rand_place].get('name')
        nb_prod = jData.get('tags')[rand_place].get('products')
        if (data not in val) and (data[2] is not ':') and (nb_prod > 20):
            val.append(data)
            i = i + 1
    #val = jData.get('product').get('categories')
    for k in val:
        print(k)
else:
    print("nok")


url = "https://fr.openfoodfacts.org/category/"+ val[0] +".json"
response = requests.get(url)
if(response.ok):
    jData = json.loads(response.content)
    for i in range(3):
        print("\n")
        print(jData.get('products')[i].get('product_name_fr'))
        print(jData.get('products')[i].get('quantity'))
        print(jData.get('products')[i].get('stores'))
        print(jData.get('products')[i].get('traces'))
        print(jData.get('products')[i].get('nutrition_grades_tags'))
        print(jData.get('products')[i].get('link'))

