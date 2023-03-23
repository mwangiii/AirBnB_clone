#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.__init__ import storage


def type_parser(arg):
    """Check data type of arg and cast it"""
    if arg.isalpha():
        pass
    elif arg.isdigit():
        arg = int(arg)
    elif isfloat(arg):
        arg = float(arg)
    return arg


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

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            if not line[0] in self.__classes:
                print("** class doesn't exist **")
            elif len(line) != 2:
                print("** instance id missing **")
            else:
                search_key = line[0] + "." + line[1]
                check = False
                for key, value in storage.all().items():
                    if search_key == key:
                        check = True
                        del storage.all()[key]
                        storage.save()
                        break
                if not check:
                    print("** no instance found **")

    def help_destroy(self):
        """Help output for the destroy command"""
        print("Deletes an instance based on the class name and id\
 (save the change into the JSON file)")
        print()

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        """
        # Finding the dict in arguments
        match = re.search(r"{(.*)}", arg)
        if match is not None:
            # Splitting arg upto where the dictionary starts
            line = arg[:match.span()[0]].split()
            # Adding the dictionary to the list
            line.append(match.group())

            ag = re.sub(':', ' ', ag)
            # These two lines disassemble the dictionary to
            # just arguments separated by white space
            ag = re.sub('[}{\',]', '', line[2])

            ag = ag.split()
            it = iter(ag)
            # These two lines make the list a dictionary
            ag = dict(zip(it, it))

            # reinitializing the dictionary
            line[2] = ag
        else:
            line = arg.split()
        if len(line) == 0:
            print("** class name missing **")
        else:
            if not line[0] in self.__classes:
                print("** class doesn't exist **")
            elif len(line) == 1:
                print("** instance id missing **")
            else:
                check = False
                for key, value in storage.all().items():
                    id_no = key.split(".")
                    if id_no[1] == line[1] and id_no[0] == line[0]:
                        check = True
                        if len(line) == 2:
                            print("** attribute name missing **")

                            # An argument list with a dict has len of 3
                        elif len(line) == 3:
                            # Converting string to dictionary
                            dict_inst = line[2]
                            # Checking if it is a dictionary
                            if isinstance(dict_inst, dict):
                                for input_key, input_val in dict_inst.items():
                                    input_value = type_parser(input_val)
                                    setattr(value, input_key, input_value)
                                    storage.save()
                            else:
                                print("** value missing **")
                        else:
                            line[3] = type_parser(line[3])
                            setattr(value, line[2], line[3])
                            storage.save()
                if not check:
                    print("** no instance found **")

    def help_update(self):
        """Help output for the update command"""
        print("Updates an instance based on the class name and id by\
        adding or updating attribute (save the change into the JSON file)")
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
