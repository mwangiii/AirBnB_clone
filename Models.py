
def do_create(self, class_name):
        """Creates an instance.
        """
        if class_name == "":
            print("** class name missing **")

        elif class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            b = HBNBCommand.__classes.dict[class_name]()
            b.save()
            print(b.id)
