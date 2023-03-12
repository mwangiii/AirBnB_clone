#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """class that in herits from cmd"""

    prompt = "(hbnb)"
    classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, line):

        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """An end of line input"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        pass

    def do_create(self, class_name):
        """Creates an instance"""
        if class_name == "":
            print("** class name missing **")

        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            b = HBNBCommand.classes.dict[class_name]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """show Method"""
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
            all_objs = storage.all()
            key = class_name + "." + instance_id
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
        """
        args = arg.split()

        if len(args) == 0:
            print("**class name is missing**")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        class_name = args[0]
        instance_id = args[1]
        if class_name and instance_id:
            all_objs = storage.all()
            key = class_name + "." + instance_id
            if key in all_objs:
                del all_objs[key]
                print(all_objs[key])
                storage.save()
            else:
                print("** no instance found **")
        else:
            ("**class doesn't exist**")

    def do_all(self, arg):
        """do all method"""
        all_obj = storage.all()
        args = arg.split()
        if len(args) == 0:
            for key in all_obj([key]):
                print(all_obj[key])

        elif args[0] in all_obj:
            for key in all_obj.keys():
                if type(all_obj[key]).__name__ == args[0]:
                    print(all_obj[key])
        if arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update <class name> <id> <attribute name>
        "<attribute value>"
       """
        args = arg.split()
        if len(args) == 0:
            print("**class name is missing**")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing ** ")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        class_name = args[0]
        instance_id = args[1]
        attr_name = args[2]
        attr_value = args[3]
        if class_name and instance_id and attr_name and attr_value:
            all_objs = storage.all()
            key = class_name + "." + instance_id
            if key in all_objs:
                obj = all_objs[key]
                setattr(obj, attr_name, attr_value)
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
