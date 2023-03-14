#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """
    A command interpreter for the HBNB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def help_quit(self):
        """Help documentation for quit command"""
        print('Quit command: Exits the program')

    def help_EOF(self):
        """Help documentation for EOF command"""
        print('EOF command: Exits the program')

    def help_help(self):
        """Help documentation for help command"""
        print('Help command: Displays help documentation')

    #!/usr/bin/python3
"""
This module defines a command interpreter class that
parses and executes commands entered by the user.
"""

import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This class defines a command interpreter.
    """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel}
    valid_attrs = ['id', 'created_at', 'updated_at']

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
        if key not in self.__objects:
            print("** no instance found **")
            return

        del self.__objects[key]
        self.save()

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
