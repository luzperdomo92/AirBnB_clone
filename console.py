#!/usr/bin/python3
"""Creating a new class"""
import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

    def do_create(self, class_name=""):
        """df"""
        if class_name in self.available_class_names:
            if class_name == "User":
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
        elif not class_name:
            print("** class name missing **")
            return
        else:
            print("** class doesn't exist **")

    def do_show(self, agrs_string=""):
        """d"""
        agrs = shlex.split(agrs_string)
        try:
            class_name = agrs[0]
        except IndexError:
            print("** class name missing **")
            return
        if class_name not in self.available_class_names:
            print("** class doesn't exist **")
            return

        try:
            id = agrs[1]
        except IndexError:
            print("** instance id missing **")
            return

        instance = FileStorage().find(class_name, id)
        if not instance:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, agrs_string=""):
        """d"""
        agrs = shlex.split(agrs_string)
        try:
            class_name = agrs[0]
        except IndexError:
            print("** class name missing **")
            return
        if class_name not in self.available_class_names:
            print("** class doesn't exist **")
            return

        try:
            id = agrs[1]
        except IndexError:
            print("** instance id missing **")
            return

        instance = FileStorage().find(class_name, id)
        if not instance:
            print("** no instance found **")
        else:
            FileStorage().destroy(instance)

    def do_all(self, class_name=""):
        """d"""
        if not class_name:
            print(list(FileStorage().all().values()))
        elif class_name in self.available_class_names:
            print(list(FileStorage()
                       .filter_by_class_name(class_name).values()))
        else:
            print("** class doesn't exist **")

    def do_update(self, agrs_string=""):
        """d"""
        agrs = shlex.split(agrs_string)
        try:
            class_name = agrs[0]
        except IndexError:
            print("** class name missing **")
            return
        if class_name not in self.available_class_names:
            print("** class doesn't exist **")
            return

        try:
            id = agrs[1]
        except IndexError:
            print("** instance id missing **")
            return

        attr_name = agrs[2]
        value = agrs[3]

        instance = FileStorage().find(class_name, id)
        if not instance:
            print("** no instance found **")
            return

        try:
            attr_name = agrs[2]
        except IndexError:
            print("** attribute name missing **")
            return

        try:
            value = agrs[3]
        except IndexError:
            print("** value missing **")
            return

        instance.set_attribute(attr_name, value)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
