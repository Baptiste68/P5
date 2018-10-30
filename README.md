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


Function – DisplayMainMenu()  
    This function display the main menu.  
    In this main menu you have 2 choices:  
    1	Find a substitute  
    2	Check my substitutes  
    The user then choose either 1 or 2  


Function – FindSubstitute()  
    This function will start the process of finding a substitute.  
    This function will use 4 functions:  
    -	SelectCategory   
    -	SelectFood   
    -	GetListFood   
    -	ShowListFood   


Function – SelectCategory    
    First display the different Category  
    The user enters a number related to a category.  
    Manage errors.  
    The category is then returned  


Function – SelectFood   
    First display the different foods  
    The user enters a number related to a food.  
    Manage errors.  
    The aliment is then returned  

