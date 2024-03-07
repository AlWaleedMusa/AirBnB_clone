#!/usr/bin/python3

import cmd
import io
import sys
import shlex
from models import storage
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    classes = storage.classes()
    classes_names = [
        'BaseModel',
        'City',
        'User',
        'Place',
        'Review',
        'State',
        'Amenity',
    ]
    prompt = "(hbnb) "
    use_rawinput = False

    def default(self, line):
        """
            Process a command that is not recognized by other do_* methods.

            Args:
                line (str): The command line entered by the user.

            Returns:
                None

            Splits the command line into class name and function
            name using the '.' delimiter.
            Retrieves all data from the storage.
            Checks if the provided class name matches any of the
            classes stored in the storage.
            If so, retrieves instances of that class from the storage
            and prints their details based on the function name:
            - If the function is 'all()', prints details of all
            instances.
            - If the function is 'count()', prints the number of
            instances.
            - If the function contains 'show' and an instance ID
            enclosed in double quotes, prints details of that instance.
            - If the function contains 'destroy' and an instance ID
            enclosed in double quotes, deletes that instance and
            saves changes to storage.

            Raises:
                ValueError: If the command line does not contain
                a '.' delimiter.
        """
        empty = False
        found = False
        class_name_valid = False

        try:
            class_name, function = line.split(".")
            if class_name == "":
                empty = True
            elif class_name in self.classes_names:
                class_name_valid = True
                

        except ValueError:
            pass

        data = storage.all()
        object_list = []
        for key, value in data.items():
            name, id = key.split(".")
            if name == class_name:
                string_buffer = io.StringIO()
                sys.stdout = string_buffer
                print(value)
                printed_output = string_buffer.getvalue().strip()
                object_list.append(printed_output)
                sys.stdout = sys.__stdout__


        if class_name_valid:
            if function == "all()":
                if object_list:
                    print(object_list)
                else:
                    print("** no instance found **")
            elif function == "count()":
                print(len(object_list))
            elif "show" in function:
                try:
                    arg_id = function.split('"')
                except Exception:
                    pass

                if len(arg_id) > 2:
                    found = True

                if found:
                    instance_found = False
                    all = storage.all()
                    for key, value in all.items():
                        name, id = key.split(".")
                        if id == arg_id[1] and name == class_name:
                            instance_found = True
                            print(value)
                            break
                    if not instance_found:
                        print("** no instance found **")
                else:
                        print("** instance id missing **")
            elif "destroy" in function:
                try:
                    arg_id = function.split('"')
                except Exception:
                    pass

                if len(arg_id) > 2:
                    found = True

                if found:
                    instance_found = False
                    all = storage.all()
                    for key, value in all.items():
                        name, id = key.split(".")
                        if id == arg_id[1] and name == class_name:
                            instance_found = True
                            del all[key]
                            storage.save()
                            break
                    if not instance_found:
                        print("** no instance found **")
                else:
                        print("** instance id missing **")
        elif empty:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
            


    def do_create(self, line):
        """
            Create a new instance of a class and save it to JSON.

            Args:
                line (str): Command line passed to the program.

            Returns:
                None

            Parses the command line into arguments using
            shlex.split(). It then performs
            the following actions:
            - If no arguments are provided, it prints
            '** class name missing **'.
            - If the first argument (class name) is not
            in the list of available classes,
            it prints '** class doesn't exist **'.
            - If the class exists, it retrieves the corresponding
            class object from the
            classes dictionary. It creates a new instance
            of that class, saves it to
            JSON using the save() method, and prints the
            ID of the newly created instance.
        """

        args = shlex.split(line)

        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            for key , value in self.classes.items():
                if key == args[0]:
                    instance = value()
                    instance.save()
                    print(instance.id)


    def handle_show_or_destroy(self, line, action):
        """
            Show or destroy instance details by ID.

            Args:
                line (str): Command line passed to the program.
                action (str): Action to perform, either
                'show' or 'destroy'.

            Returns:
                None

            Prints instance details if found when
            action is 'show'.
            Deletes the instance by ID and saves
            changes to JSON when action is 'destroy'.
        """
        args = shlex.split(line)

        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            instance_found = False
            all = storage.all()
            for key, value in all.items():
                id = key.split(".")
                if id[1] == args[1]:
                    instance_found = True
                    if action == "show":
                        print(value)
                        break
                    elif action == "destroy":
                        del all[key]
                        storage.save()
                        break
            if not instance_found:
                print("** no instance found **")


    def do_show(self, line):
        """Show instance details by id"""

        self.handle_show_or_destroy(line, "show")


    def do_destroy(self, line):
        """Delete instance by id and save changes to Json"""

        self.handle_show_or_destroy(line, "destroy")


    def do_all(self, line):
        """
            Print all instances of a specified class
            or all instances if no class is provided.

            Args:
                line (str): Command line passed to the program.

            Returns:
                None

            If no class is provided in the command
            line or if the provided class exists,
            it prints details of all instances of the
            specified class or all instances
            if no class is provided. If the specified
            class doesn't exist, it prints
            '** class doesn't exist **'
        """
        args = shlex.split(line)

        if len(args) == 0 or args[0] in self.classes.keys():
            all_objs = storage.all().values()

            new_list = []
            for obj in all_objs:
                string_buffer = io.StringIO()
                sys.stdout = string_buffer
                print(obj)
                printed_output = string_buffer.getvalue().strip()
                new_list.append(printed_output)
                sys.stdout = sys.__stdout__

            if new_list:
                print(new_list)
        else:
            print("** class doesn't exist **")


    def do_update(self, line):
        """
            Process the command line and perform appropriate
            actions based on the provided arguments.

            Args:
                line (str): Command line passed to the program.

            Returns:
                None

            Parses the command line into arguments using
            shlex.split(). It then performs
            different actions based on the number and
            content of the arguments:
            - If no arguments are provided, it prints
            '** class name missing **'.
            - If the first argument (class name) is not
            in the list of available classes,
            it prints '** class doesn't exist **'.
            - If there's only one argument (class name)
            provided, it prints '** instance id missing **'.
            - If there's only two arguments provided,
            it checks if the instance with the specified
            ID exists. If not, it prints '** no instance
            found **'; otherwise, it prints
            '** attribute name missing **'.
            - If there are three arguments provided, it
            checks if the instance with the specified
            ID exists. If found, it sets the specified
            attribute to the specified value
            using setattr(), saves the changes to storage,
            and breaks the loop.
            If the instance is not found, it prints
            '** no instance found **'.
            - If there are more than three arguments
            provided, it prints '** value missing **'.
        """

        args = shlex.split(line)

        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            instance_found = False
            all = storage.all()
            for key in all.keys():
                id = key.split(".")
                if id[1] == args[1]:
                    instance_found = True
                    break
            if not instance_found:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            all = storage.all()
            for key, value in all.items():
                id = key.split(".")
                if id[1] == args[1]:
                    setattr(value, args[2], args[3])
                    storage.save()
                    break


    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quite the program when EOF is checks True"""
        print()
        return True
    
    def emptyline(self):
        """Doesn't do anything on ENTER """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
