from colorama import *

red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW


class Hangman():
    def fail1(self, lives):
        print("=" * 25)
        print("___|___\n")
        print(red + "You have " + yellow + lives + " lives" + red + " remaining!")
        print("=" * 25)

    def fail2(self, lives):
        print("=" * 25)
        print("    _____ \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "___|___\n")
        print(red + "You have " + yellow + lives + " lives" + red + " remaining!")
        print("=" * 25)

    def fail3(self, lives):
        print("=" * 25)
        print("    _____ \n"
              "   |     |\n"
              "   |     |\n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "___|___\n")
        print(red + "You have " + yellow + lives + " lives" + red + " remaining!")
        print("=" * 25)

    def fail4(self, lives):
        print("    _____ \n"
              "   |     |\n"
              "   |     |\n"
              "   |     O\n"
              "   |      \n"
              "   |      \n"
              "   |      \n"
              "___|___\n")
        print(red + "You have " + yellow + lives + " lives" + red + " remaining!")
        print("=" * 25)

    def fail5(self, lives):
        print("    _____   \n"
              "   |     |  \n"
              "   |     |  \n"
              "   |     O  \n"
              "   |    /|\ \n"
              "   |        \n"
              "   |        \n"
              "___|___\n")
        print(red + "You have " + yellow + lives + " lives" + red + " remaining!")
        print("=" * 25)

    def fail6(self, lives):
        print("    _____   \n"
              "   |     |  \n"
              "   |     |  \n"
              "   |     O  \n"
              "   |    /|\ \n"
              "   |     |  \n"
              "   |    / \ \n"
              "___|___\n")
        print(red + "You have " + yellow + lives + " lives" + red + " remaining!")
        print("=" * 25)

    def img_print(self, fails, lives):
        if fails == 1:
            hm.fail1(lives)
            return
        elif fails == 2:
            hm.fail2(lives)
            return
        elif fails == 3:
            hm.fail3(lives)
            return
        elif fails == 4:
            hm.fail4(lives)
            return
        elif fails == 5:
            hm.fail5(lives)
            return
        elif fails == 6:
            hm.fail6(lives)
            return
        else:
            return


hm = Hangman()
