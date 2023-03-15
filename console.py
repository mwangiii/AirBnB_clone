#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """
    This class defines a command interpreter.
    """
    prompt = '(hbnb) '

    valid_attrs = ['id', 'created_at', 'updated_at']

    classes = {"BaseModel", "User", "State",
                 "City", "Amenity", "Place", "Review"}

    def emptyline(self):
        """
        This method handles empty lines.
        """
        pass

    def do_quit(self, args):
        """
        This method quits the command interpreter.
        """
        return True

    def do_EOF(self, args):
        """
        This method quits the command interpreter on EOF.
        """
        return True

    def do_create(self, args):
        """
        This method creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """
        This method prints the string representation of an
        instance based on the class name and id.
        """
        args_list = args.split()
        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in self.__objects:
            print("** no instance found **")
            return

        print(self.__objects[key])

    def do_destroy(self, line):
        """destroy method"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        instance_id = args[1]
        if class_name and instance_id:
            all_obj = storage.all()
            key = class_name + "." + instance_id
            if key in all_obj:
                del all_obj[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """do all method"""
        all_obj = storage.all()
        args = line.split()
        if len(args) == 0:
            for key in all_obj.keys():
                print(all_obj[key])
        elif args[0] in all_obj:
            for key in all_obj.keys():
                if type(all_obj[key]).__name__ == args[0]:
                    print(all_obj[key])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        This method updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        args_list = args.split()
        if not args_list:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
