#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    # """class that in herits from cmd"""

    # prompt = "(hbnb)"
    # __classes = {
    #     "BaseModel",
    #     "User",
    #     "State",
    #     "City",
    #     "Place",
    #     "Amenity",
    #     "Review"
    # }

    def do_quit(self, arg):

        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """An end of line input"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        pass

    # def do_create(self, class_name):
    #     """Creates an instance.
    #     """
    #     if class_name = "":
    #         print("** class name missing **")

    #     elif class_name not in HBNBCommand.__classes:
    #         print("** class doesn't exist **")
    #     else:
    #         b = HBNBCommand.__classes.dict[class_name]()
    #         b.save()
    #         print(b.id)


#     def do_show(self, class_name):
#         """Usage: show <class> <id> or <class>.show(<id>)
#             Display the string representation of a class instance
#             of a given id.
#         """
#         if class_name == "":
#             print("**class name is missing**")

#         elif class_name not in HBNBCommand.__classes:
#             print("**class doesn't exist**")

#         elif id == "" :
#             print("**instance id is missing**")

#         else:
#             print("{} {}".format(class_name, id))
# #def do_destroy(self, ):


if __name__ == '__main__':
    HBNBCommand().cmdloop()
