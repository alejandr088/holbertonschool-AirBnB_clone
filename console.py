#!/usr/bin/python3
"""HBNBCommand module"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Define class"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]

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
                del (storage.all()[key])
                storage.save()

    def do_update(self, arg):
        """Update an instance"""
        inpt = arg.split()
        if not arg:
            print("**class name missing **")
            return
        elif inpt[0] not in HBNBCommand.classes:
            print("class doesn't exist **")
            return
        elif len(inpt) < 2:
            print("** instance id missing **")
            return
        key = inpt[0] + "." + inpt[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(inpt) < 3:
            print("** attribute name missing **")
            return
        if len(inpt) < 4:
            print("** value missing **")
            return
        attr_name = inpt[2]
        attr_value = inpt[3]
        instance = storage.all()[key]
        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_all(self, arg):
        """Print all str representations of inst"""
        inpt = arg.split()
        if not arg:
            print([str(instance) for instance
                  in storage.all().values()])
        if inpt[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print([str(instance) for key, instance
              in storage.all().items() if arg[0] in key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
