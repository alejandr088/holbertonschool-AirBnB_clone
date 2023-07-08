===<<< holbertonschool-AirBnB_clone - The Console >>>===

## Objetives
In this program we have to write a command interpreter to manage our AirBnB objects.

This is very important because we will use what we builded during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

## What is a Command Interpreter?
A command interpreter is a program that allows users to interact with the project functionality through a command line interface.

## First steps
First of all the users must have all the files included in the project, to do so is enough to clone this git repository from a linux console with this command:

git clone https://github.com/solp22/holbertonschool-AirBnB_clone.git

Then the user must be located on the base folder where the project files are located, which is "holbertonschool-AirBnB_clone".

## Start with the Command Interpreter
bring execution permissions to all .py files with chmod +x (filename.py)
then execute: ./console.py


## How to Use
Once the command interpreter is running, you can enter commands to perform various actions. Available commands include:

- `create`: Creates a new instance and saves it.
- `show`: Displays the string representation of an instance based on the class name and instance ID.
- `destroy`: Deletes an instance.
- `update`: Updates an instance with new attributes or values.
- `all`: Displays the string representation of all instances or all instances of a specific class.
- `quit`: Exits the command interpreter.

To execute a command, type the command name followed by any required arguments. For example:

## Examples
- create BaseModel
this command will create an instance and prints it's unique ID.
- show BaseModel [ID]
this command will print the str representation of the instance BaseModel by the ID given.
- update BaseModel [ID] first_name "New Name"
this command will update the selected instance by ID with the new attr/values given as arguments.
- all BaseModel
this command will print the str representation of all the instance(s)
- destroy BaseModel [ID]
this command will delete the selected instance by ID.
- quit
this command will quit the program.



NOTE: this program perform EOF handling correctly.
NOTE 2: all the program unittest tests passed w/o error.s
