#!/usr/bin/python3
"""The entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage as storage
import shlex


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class."""

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit the program when EOF."""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Emptyline line do nothing."""
        pass

    def do_create(sef, arg):
        """Create a new instance of BaseModel and Save it."""
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
        """
        Print the string representation of an instance.

        based on the class.
        """
        all_args = arg.split()

        if not arg:
            print("** class name missing **")
        elif all_args[0] not in ['BaseModel', 'FileStorage']:
            print("** class doesn't exist **")
        elif len(all_args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(all_args[0], all_args[1])
            ins = storage.all(self)

            if key in ins:
                print(ins[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name."""
        all_args = arg.split()

        if not arg:
            print("** class name missing **")
        elif all_args[0] not in ['BaseModel', 'storage']:
            print("** class doesn't exist **")
        elif len(all_args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(all_args[0], all_args[1])
            ins = storage.all(self)

            if key in ins:
                ins.pop[key]
            else:
                print("** no instance found **")
            storage.save()

    def do_all(self, arg):
        """Print all string representation of all instances based."""
        if not arg:
            print([str(o) for o in storage.all(self)])
        elif arg not in ['BaseModel', 'FileStorage']:
            print("** class doesn't exist **")
        else:
            v = [str(o) for o in storage.all(self) if o.split('.')[0] == arg]
            print(v)

    def do_update(self, arg):
        """Update an instance based on the args."""
        all_args = shlex.split(arg)

        if not arg:
            print("** class name missing **")
            return
        elif all_args[0] not in ['BaseModel']:
            print("** class doesn't exist **")
        elif len(all_args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all(self)
            for key, objc in all_objs.items():
                ob_name = objc.__class__.__name__
                ob_id = objc.id
                if ob_name == all_args[0] and ob_id == all_args[1].strip('"'):
                    if len(all_args) == 2:
                        print("** attribute name missing **")
                    elif len(all_args) == 3:
                        print("** value missing **")
                    else:
                        setattr(objc, all_args[2], all_args[3])
                        storage.save(self)
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
