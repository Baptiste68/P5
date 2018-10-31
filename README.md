# Utilisez les données publiques de l'OpenFoodFacts

This program is here to help you find substitute of your daily life aliments.


It is split in two part


## Part 1 – Substitute an Aliment
In this part, you will want to find a specific aliment. To do so you will need to follow the process under:
-	Select a Category. Here, you choose in which category is the aliment you want to substitute (Vegetable, Fruits,…)
-	Select a Food. You choose the exact aliment you want to substitute. Then you will get a list of aliments that can be a substitute.
-	*Optional* Save the result. You have the possibility to save your search result to consult it later.


## Part 2 – Consult your substitute  
In this part, you can simply watch the substitute you had chosen.


## Functions description


Function – main_menu()  
    This function display the main menu.  
    In this main menu you have 2 choices:  
    1	Find a substitute  
    2	Check my substitutes  
    The user then choose either 1 or 2  


Function – sub_menu()  
    This function will start the process of finding a substitute.  
    This function will use 4 functions:  
    -   connect_db
    -	select_category   
    -	select_food   
    -	get_substitute   
    

Function - connect_db()
    Connect the user to the DB so we can do requests.  

Function – select_category()  
    Request the DB to get all categories' name.  
    Display the different Category.  
    The user enters a number related to a category.  
    Manage errors (see function "manage_entries()".  
    The category is then returned  


Function – select_food(category)   
    Request the DB to get all food related to the category  
    Display the different foods  
    The user enters a number related to a food.  
    Manage errors (see function "manage_entries()".  
    The category and the nutri_score is then returned  

Function - get_substitute(category, nutri_score)  
    Request the DB to find a food with a higher nutri_score in the category  
    Display the result  
    
    
    
