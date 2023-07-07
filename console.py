#!/usr/bin/python3
"""HBNBCommand module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Define class"""
    prompt = "(hbnb) "
    
    def do_EOF(self, arg):
        """Exit the program with EOF"""
        exit()

    def do_quit(self, arg):
        """Command to exit the program"""
        exit()
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
