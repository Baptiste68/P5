#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from databaselink import Databaselink

"""
    This module is
"""

def manage_entries(min, max):
    while True:
        try:
            chose = int(input("Entrer un chiffre :   "))
            if chose >= min and chose <= max:
                break
            else:
                print("Le choix doit etre compris entre " \
                + str(min) + " et "+ str(max) + " \n")
        except:
            print("Vous n'avez pas saisi un nombre \n")
            chose = -1

    return chose


def main_menu():
    """
        Function that display the main menu
    """
    print("#################################")
    print("Bonjour, bienvenu dans le programme de PurBeurre")
    print("Veuillez choisir une option en tapant '1' ou '2'")
    print("1 - Trouver un substitue")
    print("2 - Montrer mes substitues \n")

    chose = manage_entries(1, 2)

    return chose


def my_substitute_menu():
    """
        Function that show user substitute
    """
    print("#################################")
    print("Voici vos aliments sauvegardé")

    # TODO: develop this function

def categories_or_food_menu(database, id_Categories):
    """
        Function that display the category menu
    """

    if id_Categories == 0: # If it is 0 it means we chose a Categories
        my_request = "SELECT id_Categories, name_Categories FROM Categories"
    else: # Otherwise we chose a food
        my_request = "SELECT DISTINCT Food.id_Food, name_Food FROM Food \
        INNER JOIN foodcate ON Food.id_Food = foodcate.id_Food \
        WHERE foodcate.id_Categories =" + str(id_Categories)
    my_result = database.send_query(my_request)

    print("#################################")
    if id_Categories == 0:
        print("Veuillez choisir une catégorie")
    else:
        print("Veuillez choisir un aliment")

    nb_row = 0
    for x in my_result:
        print(str(nb_row + 1) + " - " + x[1])
        nb_row = nb_row + 1

    chose = manage_entries(1, nb_row)

    chose_one = my_result[chose - 1] # Get the id of the chose Category / Food

    return chose

def find_substitute(database, id_Food, id_Categories):
    my_request = "SELECT nutri_score_Food FROM Food WHERE id_Food=" + str(id_Food)
    my_score = database.send_query(my_request)
    my_score = my_score[0][0]

    my_request = "SELECT DISTINCT * FROM Food \
    INNER JOIN foodcate ON Food.id_Food = foodcate.id_Food \
    WHERE foodcate.id_Categories = " + str(id_Categories) + \
    " AND Food.nutri_score_Food < " + str(my_score)

    # TODO: Link letter to a number
    my_result = database.send_query(my_request)

    print(my_result)

if __name__ == '__main__':
    db = Databaselink()
    db.connect_to_foodexo()
    chose = main_menu()
    if chose == 1:
        category = categories_or_food_menu(db, 0)
        idFood = categories_or_food_menu(db, category)
        find_substitute(db, category, idFood)

