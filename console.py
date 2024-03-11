#!/usr/bin/python3
"""

console.py which contains the entry point of the command interpreter:
"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex
import json
import re


class HBNBCommand(cmd.Cmd):
    """
    This is the entry point of the HBNBCommand command
    interpreter.
    """

    prompt = "(hbnb) "

    def default(self, line):
        """
        Called when an unrecognized command is entered
        """
        if not re.search(r"\.(\w+)\(", line):
            return
        cl_name = line.split(".")[0]
        cmd = line.split(".")[1].split("(")[0]
        term = line.split("(")[1][:-1]

        if cl_name == "":
            print("** class name missing **")
            return
        elif cl_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if cmd == "all":
            self.do_all(cl_name)

        elif cmd == "count":
            count = sum(1 for k, v in storage.all().items() if
                        v.to_dict()["__class__"] == cl_name)
            print()

        elif cmd == "show":
            self.do_show(cl_name + " " + condition.strip("\""))

        elif cmd == "destroy":
            self.do_destroy(cl_name + " " + condition.strip("\""))

        elif cmd == "update":
            if re.match('"[^"]+", {.+}', condition):
                condition = condition.replace("\'", "\"")
                term_dict = json.loads(condition.split(", ", 1)[1])
                term_id = cl_name + "." + condition.split(", ")[0].strip("\"")
                if term_id not in storage.all().keys():
                    print("** no instance found **")
                    return
                for k, v in term_dict.items():
                    setattr(storage.all()[term_id], k, v)
            else:
                condition = condition.split(", ")
                if condition == ['']:
                    print("** instance id missing **")
                    return
                key = "{}.{}".format(cl_name, condition[0].strip("\""))
                if key not in storage.all().keys():
                    print("** no instance found **")
                    return
                if len(condition) < 2:
                    print("** attribute name missing **")
                    return
                if len(condition) < 3:
                    print("** value missing **")
                    return
                self.do_update(cl_name + " " + condition[0].strip("\"") + " " +
                               condition[1].strip("\"") + " " + condition[2])
        else:
            super().default(line)

    def emptyline(self):
        """
        This method to do nothing when an empty line is inputed.
        """
        pass

    def do_update(self, line):
        """
        Update an instance based on class name and id.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return
        condition = shlex.split(line, posix=False)
        if condition[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        elif len(condition) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(condition[0], condition[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(condition) < 3:
            print("** attribute name missing **")
            return
        elif len(condition) < 4:
            print("** value missing **")
            return
        condition[3] = condition[3].strip("\"")
        storage.all()[key].__dict__[condition[2]] = condition[3]
        storage.save()

    def do_show(self, line):
        """
        shows an instance by id.
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            condition = line.split(' ')
            if condition[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(condition) < 2 or condition[1] == "":
                print("** instance id missing **")
            else:
                key = "{}.{}".format(condition[0], condition[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        Destroys an instance based on the class name and id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            condition = line.split(' ')
            if condition[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(condition) < 2 or condition[1] == "":
                print("** instance id missing **")
            else:
                key = "{}.{}".format(condition[0], condition[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """
        Displays all instances, display all of a class of instances.
        """
        if line != "":
            condition = line.split(' ')
            if condition[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj_list = [str(obj) for key, obj in storage.all().items() if
                            type(obj).__name__ == condition[0]]
                print(obj_list)
        else:
            obj_list = [str(obj) for key, obj in storage.all().items()]
            print(obj_list)

    def do_create(self, line):
        """
        forms a new instance
        """
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            inst = storage.classes()[line]()
            inst.save()
            print(inst.id)

    def do_EOF(self, line):
        """
        this EOF command exits the program.
        """
        pass
        return True

    def do_quit(self, line):
        """
        quit command exits the program.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
