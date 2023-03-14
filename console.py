#!/usr/bin/python3
""" Console 0.0.1 Module"""
import cmd
import re
from models.base_model import BaseModel
from models import FileStorage
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models import storage
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
storage = FileStorage()


class HBNBCommand(cmd.Cmd):
    """Defines console class"""

    prompt = '(hbnb) '

    __classes = {"BaseModel",
                 "User",
                 "State",
                 "City",
                 "Place",
                 "Amenity",
                 "Review"}

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, line):
        """Allows different form inputs"""

        __commands = {"all": self.do_all,
                      "show": self.do_show,
                      "count": self.do_count,
                      "update": self.do_update,
                      "destroy": self.do_destroy}
        args = line.split('.')
        if len(args) < 2:
            print("*** Unknown syntax: {}".format(line))
            return False
        str1 = args[1]
        str1 = str1.replace('(', '.')
        str1 = str1.replace(')', '.')
        mycmd = str1.split('.')
        cmd = mycmd[0]
        variables = "" + args[0]
        for i in range(1, len(mycmd) - 1):
            variables = variables + " " + mycmd[i]
        variables = variables.replace(',', ' ')
        newline = str(variables.replace('"', ""))

        if cmd in __commands:
            __commands[cmd](newline)
        else:
            print("*** Unknown syntax: {}".format(line))
            return False

    def do_create(self, line):
        """Usage: create <class>"""
        """Creates a new class instance,
        saves it to the Json file and prints its id"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.__classes:
            print("** class doesn't exist **")
        else:
            my_model = eval(line)()
            storage.save()
            print(my_model.id)

    def do_show(self, line):
        """Usage: show <class name> <id>"""
        """Prints the string representation
        of an instance based on the class name and id"""
        my_args = line.split(" ")
        objects = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif my_args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(my_args) != 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(my_args[0], my_args[1])
            if key not in objects:
                print("** no instance found **")
            else:
                print("{}".format(objects[key]))

    def do_destroy(self, line):
        """Usage: show <class name> <id>"""
        """Deletes an instance based on the class name and id"""
        my_args = line.split(" ")
        objects = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif my_args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(my_args) != 2:
            print("** instance id missing **")

        else:
            key = "{}.{}".format(my_args[0], my_args[1])
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                FileStorage.__objects = objects
                storage.save()

    def do_all(self, line):
        """Usage: all <class name> or all"""
        """Prints all string representation
        of all instances based or not on the class name"""
        objects = storage.all()
        obj_out = []
        args = line.split(' ')
        if len(line) == 0:
            for v in objects.values():
                obj_out.append(v.__str__())
            print("{}".format(obj_out))
        elif args[0] in self.__classes:
            for v in objects.values():
                if args[0] == v.__class__.__name__:
                    obj_out.append(v.__str__())
            print(obj_out)

        elif line not in self.__classes:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Usage: update <class name>
        <id> <attribute name> "<attribute value>"""
        """Updates an instance based on the
        class name and id by adding or updating attribute"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print(("** value missing **"))
            else:
                obj = objects["{}.{}".format(args[0], args[1])]
                if len(args) == 4:
                    obj = objects["{}.{}".format(args[0], args[1])]
                    if args[2] in obj.__class__.__dict__.keys():
                        valtype = type(obj.__class__.__dict__[args[2]])
                        obj.__dict__[args[2]] = valtype(args[3])
                    else:
                        obj.__dict__[args[2]] = args[3]
                elif type(eval(args[2])) == dict:
                    obj = objects["{}.{}".format(args[0], args[1])]
                    for k, v in eval(args[2]).items():
                        if (k in obj.__class__.__dict__.keys() and
                            type(obj.__class__.__dict__[k])
                                in {str, int, float}):
                            valtype = type(obj.__class__.__dict__[k])
                            obj.__dict__[k] = valtype(v)
                        else:
                            obj.__dict__[k] = v
                storage.save()

    def do_count(self, line):
        """Usage: count <class name>> or <class name>.count()"""
        """Retrieves the number of instances of a class"""
        objects = storage.all()
        count = 0
        args = line.split(' ')
        if len(line) == 0:
            for v in objects.values():
                count += 1
            print(count)
        elif args[0] in self.__classes:
            for v in objects.values():
                if args[0] == v.__class__.__name__:
                    count += 1
            print(count)

        elif line not in self.__classes:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
