#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This module is
"""

def main_menu():
    """
        Function that display the main menu
    """
    print("#################################")
    print("Bonjour, bienvenu dans le programme de PurBeurre")
    print("Veuillez choisir une option en tapant '1' ou '2'")
    print("1 - Trouver un substitue")
    print("2 - Montrer mes substitues \n")

    chose = 0

    while True:
        try:
            chose = int(input("Entrer un chiffre :   "))
            if chose == 1 or chose == 2:
                break
            else:
                print("Le choix doit etre 1 ou 2 \n")
        except:
            print("Vous n'avez pas saisi un nombre \n")
            chose = -1

    return chose


def my_sub_menu():
    """
        Function that show user substitute
    """
    print("#################################")
    print("Voici vos aliments sauvegardé")

    # TODO: develop this function

def categories_menu():
    """
        Function that display the category menu
    """
    print("#################################")
    print("Veuillez choisir une catégorie")
    print("1 - Fruit")
    print("2 - Légume \n")

    while True:
        try:
            chose = int(input("Entrer un chiffre :   "))
            if chose == 1 or chose == 2:
                break
            else:
                print("Le choix doit etre 1 ou 2 \n")
        except:
            print("Vous n'avez pas saisi un nombre \n")
            chose = -1

    return chose

if __name__ == '__main__':
    main_menu()
