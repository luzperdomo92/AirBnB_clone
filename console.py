#!/usr/bin/python3
"""Creating a new class"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """ Class that the entry point of the command interpreter """
    available_class_names = ("BaseModel", "User", "State", "City",
                             "Amenity", "Place", "Review")
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """d"""
        pass

    def do_create(self, agrs_string=""):
        """df"""
        agrs = shlex.split(agrs_string)
        if not agrs_string:
            print("** class name missing **")
            return

        class_name = agrs[0]
        if class_name not in self.available_class_names:
            print("** class doesn't exist **")
            return
        elif class_name == "User":
            new_instance = User()
        elif class_name == "State":
            new_instance = State()
        elif class_name == "City":
            new_instance = City()
        elif class_name == "Amenity":
            new_instance = Amenity()
        elif class_name == "Place":
            new_instance = Place()
        elif class_name == "Review":
            new_instance = Review()
        else:
            new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, agrs_string=""):
        """d"""
        agrs = shlex.split(agrs_string)
        if len(agrs) == 0:
            print("** class name missing **")
            return
        class_name = agrs[0]

        if class_name not in self.available_class_names:
            print("** class doesn't exist **")
            return

        if len(agrs) < 2:
            print("** instance id missing **")
            return
        id = agrs[1]

        instance = models.storage.find(class_name, id)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, agrs_string=""):
        """d"""
        agrs = shlex.split(agrs_string)
        if len(agrs) < 1:
            print("** class name missing **")
            return
        class_name = agrs[0]

        if class_name not in self.available_class_names:
            print("** class doesn't exist **")
            return

        if len(agrs) < 2:
            print("** instance id missing **")
            return
        id = agrs[1]

        instance = models.storage.find(class_name, id)
        if not instance:
            print("** no instance found **")
        else:
            models.storage.destroy(instance)

    def do_all(self, agrs_string=""):
        """d"""
        agrs = shlex.split(agrs_string)
        if len(agrs) < 1:
            print(list(models.storage.all().values()))
            return
        class_name = agrs[0]

        if class_name in self.available_class_names:
            print(list(models.storage
                       .filter_by_class_name(class_name).values()))
        else:
            print("** class doesn't exist **")

    def do_update(self, agrs_string=""):
        """d"""
        agrs = shlex.split(agrs_string)
        if len(agrs) < 1:
            print("** class name missing **")
            return
        class_name = agrs[0]

        if class_name not in self.available_class_names:
            print("** class doesn't exist **")
            return

        if len(agrs) < 2:
            print("** instance id missing **")
            return
        id = agrs[1]

        instance = models.storage.find(class_name, id)
        if not instance:
            print("** no instance found **")
            return

        if len(agrs) < 3:
            print("** attribute name missing **")
            return
        attr_name = agrs[2]

        if len(agrs) < 4:
            print("** value missing **")
            return
        value = agrs[3]
        instance.set_attribute(attr_name, value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
