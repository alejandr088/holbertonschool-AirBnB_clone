<div align="center">
  
<img src= "https://github.com/solp22/holbertonschool-AirBnB_clone/assets/124692695/ed8ff7dd-177e-40b0-bbd2-812d2f3c5aa2" width=500 />

</div>
<h1 align="center"> AirBnB clone - The console </h1>

## Description
The HBNB Console is based on the BaseModel class, which serves as the foundation for all other classes. It uses a file-based storage system to persist data, with instances stored in a JSON file.

## Objetives
In this program we have to write a command interpreter to manage our AirBnB objects.

This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what we built during this project with all other following projects: HTML/CSS templating, database storage, API, and front-end integration.

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This abstraction will also allow us to change the type of storage easily without updating all of our codebase. The console will be a tool to validate this storage engine.

<div align="center">

<img src="https://github.com/solp22/holbertonschool-AirBnB_clone/assets/124692695/e7330e1e-8d8b-456a-82e1-96a91ef7c1f4" width=600 />

</div>

## What is a Command Interpreter?
A command interpreter is a program that allows users to interact with the project functionality through a command line interface. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Project Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files should end with a new line
* The first line of all files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Code should use the pycodestyle (version 2.7.*)
* All files must be executable
* All modules should have a documentation 
* All classes should have a documentation
* All functions (inside and outside a class) should have a documentation
* All test files should be inside a folder tests
* Use the unittest module
* All test files should be python files (extension: .py)
* All test files and folders should start by test_
* File organization in the tests folder should be the same as the project
* All tests should be executed by using this command: python3 -m unittest discover tests

## First steps
First of all the users must have all the files included in the project, to do so is enough to clone this git repository from a linux console with this command:

`git clone` https://github.com/solp22/holbertonschool-AirBnB_clone.git

Then the user must be located on the base folder where the project files are located, which is "holbertonschool-AirBnB_clone".

## Start with the Command Interpreter
Bring execution permissions to console file with `chmod +x console.py`
then execute: `./console.py`


## Definitions
Once the command interpreter is running, you can enter commands to perform various actions. Available commands include:

- `create`: Creates a new instance and saves it.
- `show`: Displays the string representation of an instance based on the class name and instance ID.
- `destroy`: Deletes an instance.
- `update`: Updates an instance with new attributes or values.
- `all`: Displays the string representation of all instances or all instances of a specific class.
- `quit`: Exits the command interpreter.

## How to Use
To execute a command, type the command name followed by any required arguments. The syntaxis is as follows:

- `[command] [class] [attributes(if needed)]`
* [command]: The name of the command you want to execute (e.g., create, show, destroy, update, all).
* [class]: The name of the class you want to perform the command on (e.g., User, State, City, etc.).
* [attributes] (if needed): Additional attributes or values required for specific commands (e.g., email, password for the create command).

## Examples
- `create BaseModel`
This command will create an instance and prints it's unique ID.
- `show BaseModel [ID]`
This command will print the str representation of the instance BaseModel by the ID given.
- `update BaseModel [ID] first_name "New Name"`
This command will update the selected instance by ID with the new attr/values given as arguments.
- `all BaseModel`
This command will print the str representation of all the instance(s)
- `destroy BaseModel [ID]`
This command will delete the selected instance by ID.
- `quit` and `EOF`
This commands will exit the program.

## Testing
All unitests can be exceuted with the command `python3 -m unittest discover tests` in interactive mode and the command `echo "python3 -m unittest discover tests" | bash` in non-interactive mode.

<hr>

<p align="center">Authors:</p>
<p align="center"><a href= "https://github.com/solp22">Sol Puente</a></p>
<p align="center"><a href= "https://github.com/alejandr088">Alejandro Rivello</a></p>

