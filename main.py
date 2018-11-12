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

    return manage_entries(1, 2)


def my_substitute_menu(database):
    """
        Function that show user substitute
    """
    print("\n#################################")
    print("Voici vos aliments sauvegardé")
    print("----------------------------")

    my_query = "SELECT sub.id_food, sub.name_food, issub.name_food \
    FROM `saved` s, `Food` sub, `Food`issub \
    WHERE sub.id_food = s.Food_id_foodsub \
    AND issub.id_Food = s.Food_id_foodissub "
    my_result = database.send_query(my_query)

    row = 0
    print("# - Substitue ---> Substitué")
    print("----------------------------")
    for line in my_result:
        print(str(row + 1) + " - " + line[1] + " ---> " + line[2])
        row = row + 1

    print("----------------------------")
    print("Entrer un numéro pour voir les détails d'un substitue ")
    print("(tapez '0' pour quitter)")
    chose = manage_entries(0, row)
    if chose is not 0:
        sub_id = my_result[chose - 1][0]
        sub_details = "SELECT * FROM Food WHERE id_food = \'"+ str(sub_id) + "\'"
        print(database.send_query(sub_details))
        input("Appuyez sur une touche pour continuer....")


def categories_or_food_menu(database, id_categories):
    """
        Function that display the category menu
    """

    if id_categories == 0: # If it is 0 it means we chose a Categories
        my_request = "SELECT id_categories, name_categories FROM Categories"
    else: # Otherwise we chose a food
        my_request = "SELECT DISTINCT Food.id_food, name_food FROM Food \
        INNER JOIN foodcate ON Food.id_food = foodcate.Food_id_food \
        WHERE foodcate.Categories_id_categories =" + str(id_categories)
    my_result = database.send_query(my_request)

    print("\n#################################")
    if id_categories == 0:
        print("Veuillez choisir une catégorie")
    else:
        print("Veuillez choisir un aliment")

    nb_row = 0
    for x in my_result:
        print(str(nb_row + 1) + " - " + x[1])
        nb_row = nb_row + 1

    # Get the id of the chose Category / Food
    return my_result[manage_entries(1, nb_row) - 1][0]


def find_substitute(database, id_food, id_categories):
    my_request = "SELECT nutri_score_Food FROM Food WHERE id_food=" + str(id_food)
    my_score = database.send_query(my_request)
    my_score = my_score[0][0]

    my_request = "SELECT DISTINCT id_food, name_food, nutri_score_food FROM Food \
    INNER JOIN foodcate ON Food.id_food = foodcate.Food_id_food \
    WHERE foodcate.Categories_id_categories = " + str(id_categories) + \
    " AND ASCII (Food.nutri_score_food) < " \
    + str(ord(my_score)) + " AND Food.id_food <> " + str(id_categories) \
    + " ORDER BY RAND() LIMIT 1"

    return database.send_query(my_request)


def save_substitute(substitute, id_food_is_substitute, database):
    print("\n#################################")
    if substitute == []:
        print("Votre recherche n'a donné aucun résultat")
        print("Cet aliment a déjà le meilleur \
score nutritionnel de sa catégorie ")
    else:
        print("Voici votre substitue")
        print(substitute)
        print("Voulez-vous sauveguarder votre résultat ?")
        print("1 - Oui !")
        print("2 - Non ! \n")

        chose = manage_entries(1, 2)
        if chose == 1:
            id_substitute = str(substitute[0][0])
            my_request = "SELECT * from saved WHERE \
            Food_id_foodsub = "+ id_substitute + " AND \
            Food_id_foodissub = " + str(id_food_is_substitute)
            if database.send_query(my_request) == []:
                my_insert = "INSERT INTO saved VALUES (\'" + id_substitute + "\
                \',\'" + str(id_food_is_substitute) + "\')"
                database.send_insert(my_insert)
                my_result = "SELECT sub.name_food, issub.name_food \
                FROM `Food` sub, `Food`issub \
                WHERE sub.id_food = " + id_substitute + " \
                AND issub.id_Food = " + str(id_food_is_substitute)
                print(str(database.send_query(my_result)[0][0]) + " sauvé comme\
 substitue de " + str(database.send_query(my_result)[0][1]) )
            else:
                print("Cette combinaison est déjà sauveguardée")



def quit_program():
    print("\nQue souhaitez-vous faire maintenant : ")
    print("1 - Quitter le programme")
    print("2 - Retourner au menu principal")
    if manage_entries(1,2) == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    db = Databaselink()
    db.connect_to_foodexo()
    quit = False
    while not quit:
        chose = main_menu()
        if chose == 1:
            category = categories_or_food_menu(db, 0)
            idFood = categories_or_food_menu(db, category)
            save_substitute(find_substitute(db, idFood, category), idFood, db)
            quit = quit_program()
        elif chose == 2:
            my_substitute_menu(db)
            quit = quit_program()
    db.close_all()

