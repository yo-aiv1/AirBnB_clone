#!/usr/bin/python3
"""The entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
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

    def do_create(self, arg):
        """Create a new instance of BaseModel and Save it."""
        if arg:
            try:
                dct = {
                        'BaseModel': BaseModel, 'Place': Place,
                        'City': City, 'Amenity': Amenity, 'State': State,
                        'Review': Review
                        }
                my_model = dct[arg]()
                print(my_model.id)
                my_model.save()
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
        elif all_args[0] not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        elif len(all_args) < 2:
            print("** instance id missing **")
        else:
            ins = storage.all()
            for key, value in ins.items():
                objname = value.__class__.__name__
                objid = value.id
                if objname == all_args[0] and objid == all_args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name."""
        all_args = arg.split()

        if not arg:
            print("** class name missing **")
        elif all_args[0] not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        elif len(all_args) < 2:
            print("** instance id missing **")
        else:
            ins = storage.all()
            for key, value in ins.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == all_args[0] and ob_id == all_args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Print all string representation of all instances based."""
        all_args = arg.split()

        if not arg:
            print("** class name missing **")
            return
        elif arg not in ['BaseModel', 'User']:
            print("** class doesn't exist **")
        else:
            ins = storage.all()
            instances = []
            for key, value in ins.items():
                ob_name = value.__class__.__name__
                if ob_name == all_args[0]:
                    instances += [value.__str__()]
            print(instances)

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
            ins = storage.all()
            for key, value in ins.items():
                objname = value.__class__.__name__
                objid = value.id
                if objname == all_args[0] and objid == all_args[1].strip('"'):
                    if len(all_args) == 2:
                        print("** attribute name missing **")
                    elif len(all_args) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, all_args[2], all_args[3])
                        storage.save()
                    return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
