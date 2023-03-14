#!/usr/bin/env python3
"""
This module contains the entry point of the command interpreter.
"""

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
