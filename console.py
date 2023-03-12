#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """class that in herits from cmd"""

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """An end of line input"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        pass
