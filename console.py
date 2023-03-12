#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """class that in herits from cmd"""
    prompt = "(hbnb)"
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """An end of line input"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()