#!/usr/bin/python3
""""programme : The entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage as storage


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

    def do_create(sef, arg):
        'Creates a new instance of BaseModel and Save it\n'
        if arg:
            try:
                ins = eval(arg)()
                ins.save()
                print(ins.id)
            except NameError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        'Prints the string representation of an instance based on the class\n'
        tot = arg.split()

        if not arg:
            print("** class name missing **")
        elif tot[0] not in ['BaseModel', 'FileStorage']:
            print("** class doesn't exist **")
        elif len(tot) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(tot[0], tot[1])
            ins = storage.all(self)

            if key in ins:
                print(ins[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name'
        tot = arg.split()

        if not arg:
            print("** class name missing **")
        elif tot[0] not in ['BaseModel', 'storage']:
            print("** class doesn't exist **")
        elif len(tot) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(tot[0], tot[1])
            ins = storage.all(self)

            if key in ins:
                ins.pop[key]
            else:
                print("** no instance found **")
            storage.save()

    def do_all(self, arg):
        'Prints all string representation of all instances based\n'
        if not arg:
            print([str(o) for o in storage.all(self)])
        elif arg not in ['BaseModel', 'FileStorage']:
            print("** class doesn't exist **")
        else:
            v = [str(o) for o in storage.all(self) if o.split('.')[0] == arg]
            print(v)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
