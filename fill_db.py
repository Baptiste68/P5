#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random

import mysql.connector
import requests

from databaselink import Databaselink

"""
    This module is use to create and 
    populate the database.
"""

CREATION_FILE = './database/createv2.sql'

db = Databaselink()

cnx = mysql.connector.connect(host=db.config.get('host'), port=db.config.get(
    'port'), user=db.config.get('user'), password=db.config.get('password'))
cursor = cnx.cursor()


def executeScriptsFromFile(filename):
    """
        This function execute a SQL file
    """
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except (IOError, msg):
            print("Command skipped: ", msg)


executeScriptsFromFile(CREATION_FILE)
cnx.commit()

cursor.execute('use foodexo;')
db.connect_to_foodexo()

categories_list = ["Boissons", "Viandes", "Surgelés", "Conserves",
                   "Fromages", "Biscuits", "Chocolats", "Apéritifs", "Soupes", "Pizzas"]

for category in categories_list:
    print(f"Populating: {category}")
    my_insert = f"INSERT INTO categories (name_categories) VALUES ('{category}')"
    db.send_insert(my_insert)
    page = 1
    k = 0
    while k < 20:
        i = 0
        while i < 19 and k < 20:
            url = f"https://fr.openfoodfacts.org/category/{category}/{page}.json"
            response = requests.get(url)
            if(response.ok):
                jData = json.loads(response.content)
                if len(jData.get('products')[i].get('nutrition_grades_tags')[0])\
                        is not 1:
                    i = i + 1
                elif jData.get('products')[i].get('product_name_fr') is None:
                    i = i + 1
                elif len(jData.get('products')[i].get('product_name_fr')) < 1:
                    i = i + 1
                else:
                    product_name = str(jData.get('products')[i].get(
                        'product_name_fr')).replace('\'', '\'\'')
                    product_name = product_name.replace('\\', '')
                    quantity = str(jData.get('products')[i].get(
                        'quantity')).replace('\'', '\'\'')
                    quantity = quantity.replace('\\', '')
                    dangers = str(jData.get('products')[i].get(
                        'traces')).replace('\'', '\'\'')
                    dangers = dangers.replace('\\', '')
                    stores = str(jData.get('products')[i].get(
                        'stores')).replace('\'', '\'\'')
                    stores = stores.replace('\\', '')
                    nutri_score = str(jData.get('products')[i].get(
                        'nutrition_grades_tags')[0]).replace('\'', '\'\'')
                    nutri_score = nutri_score.replace('\\', '')
                    link = str(jData.get('products')[i].get(
                        'url')).replace('\'', '\'\'')
                    my_insert = "INSERT INTO food ( name_food, quantity_food, \
                    dangers_food, store_food, nutri_score_food, link_food ) VALUES (\'"\
                    + product_name + "\', \'"\
                        + quantity + "\', \'"\
                        + dangers + "\', \'"\
                        + stores + "\', \'"\
                        + nutri_score + "\', \'"\
                        + link + "\')"
                    db.send_insert(my_insert)
                    my_insert = "INSERT INTO foodcate SELECT f.id_food, c.id_categories \
                    FROM ( SELECT id_food FROM Food \
                    WHERE id_food = (SELECT MAX(id_food) FROM Food) ) \
                    AS f CROSS JOIN ( SELECT id_categories \
                    FROM Categories WHERE name_Categories = \'" + category + "\' ) AS c"
                    db.send_insert(my_insert)
                    k = k + 1
                    i = i + 1
        page = page + 1

