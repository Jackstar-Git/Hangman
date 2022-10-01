import random
import os
import modules.commands as commands

from modules.draw import Hangman
from colorama import *

hm = Hangman()
init(autoreset=True)

# colors
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW

# variable definitions
words = []
guess = str()
current_word = []
already_guessed = []
word = str()
lives = 6
fails = 0
got_hint1 = False
hint = None
possible_hints = []


def generate_word():
    global word
    i = 0
    with open("words.txt", "r") as f:
        for line in f.readlines():
            words.append(line)
    for _ in words:
        words[i] = words[i].strip()
        i += 1

    word = str(random.choice(words)).lower()
    return word


def reset():
    global fails
    global word
    global words
    global lives
    global already_guessed
    global guess
    global current_word
    global hint
    word = str()
    words = []
    lives = 6
    already_guessed = []
    guess = ""
    current_word = []
    hint = None
    fails = 0

    input("Press any key to restart... ")
    os.system('cls')


def empty_word():
    global current_word
    for i in range(0, len(word)):
        current_word.append("_ ")

    s = ""
    for x in current_word:
        s += x

    print(blue + "Your word is: " + yellow + s)
    print("-" * 50)


def get_hint():
    global got_hint1
    global hint
    global current_word
    global possible_hints

    hint_no = random.randint(1, 2)

    print("-" * 30)
    print(blue + "You got a hint!")

    if hint_no == 1:
        ind = 0
        for i in current_word:
            if i == "_ ":
                possible_hints += list(word[ind])
            ind += 1
        if len(possible_hints) <= 1:
            print(red + "You are only missing one letter, not hint for you!")
            print("-" * 30)
            return
        print(blue + "A letter got guessed and placed for you!")

        hint = random.choice(possible_hints)
        inx = []
        for idx, value in enumerate(word):
            if value == hint:
                inx.append(idx)

        for i in inx:
            current_word[i] = hint + " "

        got_hint1 = True

    elif hint_no == 2:
        vowel_count = 0
        for x in list(word):
            if x in ["a", "e", "i", "o", "u"]:
                vowel_count += 1
        print(blue + "Your word has: " + yellow + str(vowel_count) + blue + " vowel(s)!")

    print("-" * 30)


def guess_letter():
    global guess

    guess = None
    while guess is None or len(guess) < 1 or len(guess) >= 2 or not guess.isalpha():
        guess = input("Input your guess: ").lower()
        if len(guess) <= 0:
            print("-" * 30)
            print("Don't make an" +yellow+ " empty"+red+" guess!")
            print("-" * 30)
        elif not guess.isalpha():
            print("-" * 30)
            print(red + "Only use letters!")
            print("-" * 30)
        elif len(guess) >= 2:
            print("-" * 30)
            print(red + "Your guess must be exactly " + yellow + "one" +red + " character long!")
            print("-" * 30)
    if guess in already_guessed:
        print("-" * 20)
        print(red + "You already guessed that letter!")
        print("-" * 20)
        guess_letter()
    os.system('cls')


def check_answer():
    global word
    global got_hint1
    global hint
    global lives
    global already_guessed
    global current_word
    global guess
    global fails

    guess_letter()

    indices = []

    if guess in word:
        for idx, value in enumerate(word):
            if value == guess:
                indices.append(idx)
    else:
        lives -= 1
        fails += 1
        if lives == 2:
            get_hint()

        hm.img_print(fails, str(lives))

    for i in indices:
        current_word[i] = guess + " "

    if got_hint1:
        already_guessed.append(hint)
        got_hint1 = False
    already_guessed.append(guess)
    already_guessed.sort()
    guess = ""
    s2 = ""
    for x in current_word:
        s2 = s2 + x
    print(blue + "The current word is: " + yellow + s2)
    print("-" * 50)
    x = []
    for i in current_word:
        s3 = i.replace(" ", "")
        x.append(s3)

    if x == list(word):
        print(blue + "You guessed the word!")
        reset()
        new_game()


def new_game():
    global word
    global already_guessed

    generate_word()

    status = ""
    while status not in ["y", "n"] or status == "!help":
        status = input("Do you want to start a new game? (y/n): ").lower()
        if status == "n":
            exit()
        if status == "!help":
            commands.commands_main()

    empty_word()

    while lives != 0:
        print(green + "Already guessed letters:", already_guessed)

        check_answer()
    print(red + "You lost! The word was: " + yellow + word)
    reset()
    new_game()


def main():
    print(blue + "Welcome to my little Hangman-Game! Made with ♥ by Jackstar#2002!")
    print(blue + "You can see a list of commands, if you type \"!help\" down below")
    print("-" * 75)
    new_game()


if __name__ == "__main__":
    main()
