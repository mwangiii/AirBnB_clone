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

    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel,
               'User': User,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Place': Place,
               'Review': Review}

    valid_attrs = ['id', 'created_at', 'updated_at']
    __objects = storage.all()

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

    def help_quit(self):
        """
            Help documentation for quit command
        """
        print('Quit command: Exits the program')

    def do_EOF(self, args):
        """
        This method quits the command interpreter on EOF.
        """
        return True

    def help_EOF(self):
        """Help documentation for EOF command"""
        print('EOF command: Exits the program')

    def help_help(self):
        """Help documentation for help command"""
        print('Help command: Displays help documentation')

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

    def do_destroy(self, args):
        """
        This method deletes an instance based on the class name and id.
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
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, args):
        """
        This method prints all string representation of all instances
        based or not on the class name.
        """
        if not args:
            objects = self.__objects.values()
        else:
            class_name = args.split()[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return

            objects = [obj for obj in self.__objects.values()
                       if type(obj).__name__ == class_name]

        print([str(obj) for obj in objects])


def do_update(self, arg):
    """Updates an instance based on the class name and id by adding or
    updating attribute
    Usage: update <class name> <id> <attribute name> "<attribute value>"
    """
    args = arg.split()
    if not args:
        print("** class name missing **")
        return

    class_name = args[0]
    if class_name not in HBNBCommand.classes:
        print("** class doesn't exist **")
        return

    if len(args) < 2:
        print("** instance id missing **")
        return

    obj_id = args[1]
    obj_key = "{}.{}".format(class_name, obj_id)
    if obj_key not in storage.all():
        print("** no instance found **")
        return

    obj = storage.all()[obj_key]
    if len(args) < 3:
        print("** attribute name missing **")
        return

    attr_name = args[2]
    if len(args) < 4:
        print("** value missing **")
        return

    attr_value = " ".join(args[3:])
    if hasattr(obj, attr_name):
        attr_type = type(getattr(obj, attr_name))
        try:
            attr_value = attr_type(attr_value)
        except ValueError:
            print("** invalid value **")
            return
        setattr(obj, attr_name, attr_value)
        storage.save()
    else:
        print("** no attribute found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
