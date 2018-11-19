import requests
import json
import random

from databaselink import Databaselink

db = Databaselink()
db.connect_to_foodexo()

categories_list = ["Boissons","Viandes","Surgelés","Conserves","Fromages","Biscuits","Chocolats", "Apéritifs", "Soupes", "Pizzas"]


for category in categories_list:
    my_insert = "INSERT INTO categories (name_categories)\
     VALUES (\'" + category + "\')"
    db.send_insert(my_insert)
    url = "https://fr.openfoodfacts.org/category/"+ category +".json"
    response = requests.get(url)
    if(response.ok):
        jData = json.loads(response.content)
        k, i = 0, 0
        while k < 20:
            print(jData.get('products')[i].get('nutrition_grades_tags')[0])
            print(i)
            if len(jData.get('products')[i].get('nutrition_grades_tags')[0])\
             is not 1 :
                i = i + 1
            else:
                product_name = jData.get('products')[i].get('product_name_fr')
                quantity = jData.get('products')[i].get('quantity')
                dangers = jData.get('products')[i].get('traces')
                stores = jData.get('products')[i].get('stores')
                nutri_score = jData.get('products')[i].get('nutrition_grades_tags')[0]
                link = jData.get('products')[i].get('link')
                my_insert = "INSERT INTO food ( name_food, quantity_food, \
                dangers_food, store_food, nutri_score_food, link_food ) VALUES (\'"\
                + str(product_name).replace('\'', '\'\'') + "\', \'"\
                + str(quantity).replace('\'', '\'\'') + "\', \'"\
                + str(dangers).replace('\'', '\'\'') + "\', \'"\
                + str(stores).replace('\'', '\'\'') + "\', \'"\
                + str(nutri_score).replace('\'', '\'\'') + "\', \'"\
                + str(link).replace('\'', '\'\'') + "\')"
                db.send_insert(my_insert)
                #print(jData.get('products')[i].get('categories'))
                categories_list.remove(category)
                for cat in jData.get('products')[i].get('categories').split(","):
                    if cat in categories_list:
                        my_insert = "INSERT INTO foodcate SELECT f.id_food, c.id_categories FROM ( SELECT id_food FROM Food WHERE name_Food = \'" + product_name + "\' AND quantity_food = \'" + quantity + "\') AS f CROSS JOIN ( SELECT id_categories FROM Categories WHERE name_Categories = \'" + cat + "\' ) AS c"
                        db.send_insert(my_insert)
                categories_list.append(category)
                my_insert = "INSERT INTO foodcate SELECT f.id_food, c.id_categories FROM ( SELECT id_food FROM Food WHERE name_Food = \'" + product_name + "\' AND quantity_food = \'" + quantity + "\') AS f CROSS JOIN ( SELECT id_categories FROM Categories WHERE name_Categories = \'" + category + "\' ) AS c"
                db.send_insert(my_insert)
                i = i + 1
                k = k + 1



