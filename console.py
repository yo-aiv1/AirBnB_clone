#!/usr/bin/python3
""""programme : The entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class."""
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        'Exit the program when EOF'
        print()
        return True

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        print()
        return True

    def emptyline(self):
        'Emptyline line do nothing\n'
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
