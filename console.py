#!/usr/bin/python3
"""Creating a new class"""
import cmd
import os.path
import inspect
import models


class HBNBCommand(cmd.Cmd):
    """ Class that the entry point of the command interpreter """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, class_name):
        """df"""
        if 'class_name' not in inspect.getmembers(models):
            print("** class doesn't exist **")
        else:
            print("exist")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
