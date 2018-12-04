#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from databaselink import Databaselink


"""
    This module is the main module of the program
    It allows you to run all functionalities
"""


def manage_entries(min, max):
    """
        This function is to manage the keyboard entries
        from the user
    """
    while True:
        try:
            chose = int(input("Entrer un chiffre :   "))
            if chose >= min and chose <= max:
                break
            else:
                print("Le choix doit etre compris entre "
                      + str(min) + " et " + str(max) + " \n")
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
    print("1 - Trouver un substitut")
    print("2 - Montrer mes substituts \n")

    return manage_entries(1, 2)


def display_result(food, type):
    """
        Function that display the information of a food
    """
    food = str(food[0]).replace("\"", "\'").split("\',")
    quantity = str(food[1]).replace('\'', '')
    traces = str(food[2]).replace('\'', '')
    store = str(food[3]).replace('\'', '')
    link = str(food[5]).replace('\'', '')
    print(type)
    print("-------------------")
    print("Nom : " + str(food[0]).split(',')[1].replace('\'', ''))
    if str(quantity) == " None":
        print("Quantité : Non indiquée")
    else:
        print("Quantité : " + quantity)
    if traces == " None":
        print("Traces : Non indiquées")
    else:
        print("Traces : " + traces)
    if store == " None":
        print("Magasin : Non indiqué")
    else:
        print("Magasin : " + store)
    print("Score : " + str(food[4]).replace('\'', ''))
    if link == " None":
        print("Lien : Non indiqué")
    else:
        print("Link : " + link)


def my_substitute_menu(database):
    """
        Function that show user's substitute
    """
    print("\n#################################")
    print("Voici vos aliments sauvegardé")
    print("----------------------------")

    my_query = "SELECT sub.id_food, sub.name_food, issub.name_food, issub.id_food \
    FROM `saved` s, `Food` sub, `Food`issub \
    WHERE sub.id_food = s.Food_id_foodsub \
    AND issub.id_Food = s.Food_id_foodissub "
    my_result = database.send_query(my_query)

    row = 0
    print("# - Substitut ---> Substitué")
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
        issub_id = my_result[chose - 1][3]
        sub_details = "SELECT * FROM Food WHERE id_food = \'" + \
            str(sub_id) + "\'"
        issub_details = "SELECT * FROM Food WHERE id_food = \'" + \
            str(issub_id) + "\'"
        sub_result = database.send_query(sub_details)
        issub_result = database.send_query(issub_details)
        display_result(sub_result, "Substitut")
        display_result(issub_result, "Substitué")
        input("Appuyez sur une touche pour continuer....")


def categories_or_food_menu(database, id_categories):
    """
        Function that display the category or food menu
    """

    if id_categories == 0:  # If it is 0 it means we chose a Categories
        my_request = "SELECT id_categories, name_categories FROM Categories"
    else:  # Otherwise we chose a food
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
    if nb_row == 0:
        print("Il n'y a pas de catégorie/aliment")
        return "quit"
    else:
        # return the ID of the food or category
        return my_result[manage_entries(1, nb_row) - 1][0]


def find_substitute(database, id_food, id_categories, signe):
    """
        Function that find a substitute according to the condition (signe)
    """
    my_request = "SELECT nutri_score_Food FROM Food WHERE id_food=" + \
        str(id_food)
    my_score = database.send_query(my_request)
    my_score = my_score[0][0]

    if signe == ">":
        ordering = " ORDER BY Food.nutri_score_food LIMIT 1"
    else:
        ordering = " ORDER BY RAND() LIMIT 1"

    my_request = "SELECT DISTINCT * FROM Food \
    INNER JOIN foodcate ON Food.id_food = foodcate.Food_id_food \
    WHERE foodcate.Categories_id_categories = " + str(id_categories) + \
        " AND ASCII (Food.nutri_score_food) " + signe + " " \
        + str(ord(my_score)) + " AND foodcate.Food_id_food <> " + str(id_food) \
        + " " + ordering

    return database.send_query(my_request), signe


def save_substitute(substitute, id_food_is_substitute, database, category, signe):
    """
        Function that check if a substitute has been found
        If not, it will ask user if he wants to use another condition
        Then, it display the substitute and ask if the user want to save it
    """
    print("\n#################################")
    if substitute == []:
        if signe == "<":
            print("Votre recherche n'a donné aucun résultat")
            print("Cet aliment a déjà le meilleur \
    score nutritionnel de sa catégorie ")
            print("Désirez-vous trouver un substitut de même valeur ?")
            print("1 - Oui !")
            print("2 - Non ! \n")
            chose = manage_entries(1, 2)
            if chose == 2:
                input("Appuyez sur une touche pour continuer....")
            else:
                substitute, signe = find_substitute(database, id_food_is_substitute,
                                                    category, "=")
                save_substitute(substitute, id_food_is_substitute,
                                database, category, signe)
        elif signe == "=":
            print("Cet aliment n'a pas de substitut de même valeur")
            print("Désirez-vous trouver un substitut de valeur inférieur ?")
            print("1 - Oui !")
            print("2 - Non ! \n")
            chose = manage_entries(1, 2)
            if chose == 2:
                input("Appuyez sur une touche pour continuer....")
            else:
                substitute, signe = find_substitute(database, id_food_is_substitute,
                                                    category, ">")
                save_substitute(substitute, id_food_is_substitute,
                                database, category, signe)
        else:
            print("Aucun résultat possible")
            input("Appuyez sur une touche pour continuer....")
    else:
        print("Voici votre substitut")
        display_result(substitute, "")
        print("Voulez-vous sauveguarder votre résultat ?")
        print("1 - Oui !")
        print("2 - Non ! \n")

        chose = manage_entries(1, 2)
        if chose == 1:
            id_substitute = str(substitute[0][0])
            my_request = "SELECT * from saved WHERE \
            Food_id_foodsub = " + id_substitute + " AND \
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
 substitut de " + str(database.send_query(my_result)[0][1]))
                input("Appuyez sur une touche pour continuer....")
            else:
                print("Cette combinaison est déjà sauveguardée")
                input("Appuyez sur une touche pour continuer....")


def quit_program():
    """
        Function that allows the user to leave the program
    """
    print("\nQue souhaitez-vous faire maintenant : ")
    print("1 - Quitter le programme")
    print("2 - Retourner au menu principal")
    if manage_entries(1, 2) == 1:
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
            if idFood == "quit":
                quit = quit_program()
            else:
                substitute, signe = find_substitute(db, idFood, category, "<")
                save_substitute(substitute, idFood, db, category, signe)
                quit = quit_program()
        elif chose == 2:
            my_substitute_menu(db)
            quit = quit_program()
    db.close_all()

