# Phase 3 CLI+ORM Project - Charity-Gram

## Introduction
Welcome to my end of Phase 3 project for FlatIron school. 
The idea I had was to combine my professional life of working/volunteering with NGO's with my educational life of coding.
I wanted to create a CLI that adheres to an everyday web user and show them "client facing" information

I chose to focus on three categories:
    (1) -> Charity Categories, such as food, environment e.t.c.
    (2) -> Charities, such as Unicef (as well as what categories they fell under)
    (3) -> Donors, and who they donated to
Each instance of these categories/classes can be updated or deleted.
In addition we can add new instances to each class/category thanks to the __init__ methods in all classes.

Please when using this app, run the commands:
```console
pipenv install
pipenv shell
```

## cli.py
This file is where the Command Line Interface(CLI) is run.
The CLI is a text-based interface where you can input commands that interact with a computer's operating system.
All menus and inputs the user interacts with in this app have been created using this page. 
To access it from the console please enter:
```console
$python lib/cli.py
```
With the help of "helper functions" I have been able to create code that allows for easy navigation through the CLI in the users terminal. It creates all the menus the user sees, highlighting which options they can choose which is implemented by the helper functions.

## helpers.py
This file holds all the code that forms the backbone of the CLI.
The code written here allows users to update, delete and create new instances of each class, and thanks to the ORM methods in each classes function it will update the tables in our database. 
The functions created in this file are imported to the cli.py file so they can work in unison to create easy navigation for the user.

## debug.py
This file handles the creation and deletion of our database. 
To access it you must enter:
```console
$python lib/debug.py
```
This will check to see if a table exists for each class, if it does delete it, and create it again to its default standard.
In addition I have also included some seeded data to fill the table upon initialization.
This data can be altered or deleted, but when you call $python li/debug.py again they shall be brought back

## __init__.py
This file contains a connection to the database (via CONN variable), and allow us to interact with database and execute SQL respectively(via CURSOR variable). 

## charity_type.py
This file contais the class Charity_Type, and via the __init__ method allows us to create instances of the Charity_Type class
It contains other methods that adhere to ORM methods (all written in SQL) that help access relational data such as allowing us to create and drop the corresponding table, and update, delete and add instances to the  class.
To adhere to the rule of Single Source of Truth the Charity_Type class holds methods that store the relationship between it and the Charity class, as well as it and the Donor class

## charity.py
This file contains the class Charity, and via the __init__ method allows us to create instances of the Charity class.
It contains other methods that adhere to ORM methods (all written in SQL) that help access relational data such as allowing us to create and drop the corresponding table, and update, delete and add instances to the  class.
To adhere to the rule of Single Source of Truth the Charity class holds methods that store the relationship between it and the Donor class.

## donor.py
This file contains the class Donor, and via the __init__ method allows us to create instances of the Donor class.
It contains other methods that adhere to ORM methods (all written in SQL) that help access relational data such as allowing us to create and drop the corresponding table, and update, delete and add instances to the  class.