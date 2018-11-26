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
    The user then choose either 1 or 2 (entries check with "manage_entries" function)  


If "Check my substitutes has been selected  
It will launch my_substitute_menu  

Function - my_substitute_menu(database)  
Request the DB to get the list of substitute saved.  
Show the list of all substitute saved (and their substituted food).  
User has the possiblity to get details on a substitute (check entries with "manage_entries" function)  
Display all informations of the selected food.  


### Find a substitute process
If "Find a substitute" has been selected    
It will start the process of finding a substitute.  
This process will use 3 functions:  
    -   connect_to_foodexo  
    -	categories_or_food_menu  
    -	find_substitute   
    -   save_substitute  
    

Function - connect_to_foodexo()  
    Connect the user to the DB so we can do requests.  


Function – categories_or_food_menu(database, id_categories)  
    Check what type of menu to display:  
    id_categories = 0 -> categories menu. Otherwise food menu  
    Request the DB to get all categories' or food's name.  
    Display the results.  
    The user enters a number related to a category or food.  
    Manage errors (see function "manage_entries()").  
    The category or food id is then returned  

 

Function - find_substitute(database, id_food, id_categories, sign)  
    Request the DB to get the nutri_score of the choosen food  
    Request the DB to find one food in the same category with a nutri_score higher or smaller (related to sign)  
    
     
Function - save_substitute(substitute, id_food_is_substitute, database, category)  
    Ask the user if he wants to save his search result  
    If yes, save the two id_food (substitute and substituted) in DB  
     
     
Function - manage_entries(conditions)  
    Check that the user enter something according to the conditions.  
    
    

### Other functions  
Function - quit_program()  
    Ask the user if he wants to quit the program.  
    
    
Function - display_result(food, type)  
    Display main information about a food.  
    
    
### Database  
The relation with database are manage throught databaselink.py  
You need to set the correct configuration in the "self.config"

There is then 2 function to send query:
-	send_query -> simple query to request the database  
-	send_insert -> specific query to insert data in the database and comit the result  

The close_all function is there to close the connection at the end of the program.  

