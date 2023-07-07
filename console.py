#!/usr/bin/python3
"""HBNBCommand module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Define class"""
    prompt = "(hbnb) "
    
    def do_EOF(self, arg):
        """Exit the program with EOF"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self, arg):
        """an empty line doesn't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
