#!/usr/bin/python3
"""HBNBCommand module"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define class"""
    prompt = "(hbnb) "
    classes = {"BaseModel"}
    
    def do_EOF(self, arg):
        """Exit the program with EOF"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """An empty line doesn't execute anything"""
        pass
    
    def do_create(self, arg):
        """Creates a new instance and saves it"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)()
            print(instance.id)
            instance.save()
    
    def do_show(self, arg):
        """string rep. of an instance based on the class name"""
        inpt = arg.split()
        if not arg:
            print("** class name missing **")
        elif inpt[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(inpt) == 1:
            print("** instance id missing **")
        else:
            key = inpt[0] + "." + inpt[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance"""
        inpt = arg.split()
        if not arg:
            print("** class name missing **")
        elif inpt[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(inpt) == 1:
            print("** instance id missing **")
        else:
            key = inpt[0] + "." + inpt[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del(storage.all()[key])
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
