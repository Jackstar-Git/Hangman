import time
import random
from colorama import *
from inspect import getmembers, isfunction

from main import reset

# define colors
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW

version = "4.3.2"


def commands_main():
    x = []
    for i in getmembers(Commands, isfunction):
        x.append("!" + i[0])
    print("-" * 50)
    print(yellow + "The commands are:")
    [print(blue + "- " + i) for i in x]
    print(blue + "- !help (to show this again!)")
    print("-" * 50)

    def command_select():
        y = ""
        while y not in x and y != "e" and y != "!help":
            y = input("What command do you want to use? (\"e\" to exit): ")

        if y == "e":
            print("-" * 50)
            return

        elif y == "!help":
            commands_main()

        elif y == x[0]:
            cmds.add_word()
            command_select()

        elif y == x[1]:
            cmds.changelog()
            command_select()

        elif y == x[2]:
            cmds.fix()
            command_select()

        elif y == x[3]:
            cmds.info()
            command_select()

        elif y == x[4]:
            cmds.sort_words()
            command_select()

        elif y == x[5]:
            cmds.view_words()
            command_select()
        else:
            return

    command_select()


class Commands():
    def add_word(self):
        x = None
        while x is None or len(x) < 3 or len(x) > 10 or not x.isalpha():
            print("-" * 30)
            x = input("Input the word you want to add (3-10 characters): ")
            if not x.isalpha():
                print("-" * 30)
                print(red + "Only use letters!")
            elif len(x) < 3:
                print("-" * 30)
                print(red + "Your word must be" + yellow + " at least 3" + red + " characters long!")
            elif len(x) > 10:
                print("-" * 30)
                print(red + "Your word" + yellow + "  can't be longer than 10 " + red + "characters!")

        print("-" * 30)
        y = input("Are you sure you want to add \"" + x + "\" to the word-list? (y/n): ")
        if y.lower() == "n":
            self.add_word()
        if y.lower() == "y":
            with open("words.txt", "a") as file:
                file.writelines(x.lower() + "\n")
        print("-" * 30)
        print(green + "Successfully added your word to the list!")
        print("-" * 30)

    def changelog(self):
        print("-" * 50)

        with open("modules/changelog.txt") as data:
            cl = data.read()
            print(blue + "Changelog for version " + version + "\n\n" + cl)
        print("-" * 50)

    def fix(self):
        print("-" * 50)
        print(red + "The program tries to fix the error, please wait a few seconds!")

        time.sleep(random.random()*4)
        print(blue + "Done!")
        reset()
        print("-" * 50)

    def info(self):
        print("-" * 50)
        print(blue + "Version: " + yellow + version)
        print(blue + "Developer: Jackstar#2002")
        print(blue + "Lines of code: 603")
        print(blue + "Hours of development: 26.5")
        print("-" * 50)

    def sort_words(self):
        print("-" * 30)
        i = ""
        while i.lower() not in ["y", "n"]:
            i = input("Are you sure you want to sort the list of words? (y/n): ")
        if i == "n":
            print("-" * 30)
            return

        else:
            list = []
            with open("words.txt.", "r") as data:
                for x in data.readlines():
                    list.append(x.lower())

            list.sort()
            with open("words.txt", "w") as file:
                for x in list:
                    file.write(x)
        print(green + "Successfully sorted your list of words!")
        print("-" * 30)

    def view_words(self):
        with open("words.txt", "r") as data:
            for idx, i in enumerate(data.readlines()):
                print(blue + str(idx + 1) + ". " + i, end="")
        print()
        print("-" * 30)


cmds = Commands()
