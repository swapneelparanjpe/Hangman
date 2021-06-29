import random
import re
from colorama import Fore, Style

def linebreak():
    print(Fore.WHITE, "\n===============================================\n")

name = input(Fore.CYAN + "\nPlease enter your name: ")
print(Fore.MAGENTA + "\nWelcome " + name + "!")
print("Let's play Hangman!")

linebreak()
fname = 'movies.txt'
fh = open(fname)
movies = []
for line in fh:
    line = line.split('\n')
    movies.append(line[0])
word = random.choice(movies).upper()
word = word.replace(":", "").replace(",", "").replace("-", "").replace(".", "")
no_words = len(word)
placeholder = []
movie_letters = 0
for i in word:
    if i == ' ':
        placeholder.append(' ')
    else:
        movie_letters = movie_letters + 1
        placeholder.append('-')
placeholder = ''.join(placeholder)
print(Fore.YELLOW + "\nYour movie: " + placeholder)
print("Number of letters: " + str(movie_letters))
linebreak()

guessed_characters = []
upd = placeholder
life = 10
update = []
i = 0
while life > 0:
    done = False
    fill = 0
    present = 0
    placeholder = ''.join(placeholder)
    if len(guessed_characters) != 0:
        print(Fore.CYAN + "\nPrevious guesses: " + ", ".join(guessed_characters))
    print(Fore.CYAN + "You have " + str(life) + " lives left\n")
    ch = input("Enter your guess: ")
    ch = ch.upper()

    if ch == word:
        done = True
    else:

        if ch not in guessed_characters:
            if len(ch) != 1 or re.match("[^A-Z]", ch):
                print(Fore.MAGENTA + "\nYou must enter only one alphabet")
                linebreak()
                print(Fore.YELLOW + "Your movie: " + upd)
                continue
            guessed_characters.append(ch)
            
        else:
            print(Fore.MAGENTA + "\nYou have already guessed this character before")
            linebreak()
            print(Fore.YELLOW + "Your movie: " + upd)
            continue

        for letter, character in zip(placeholder, word):
            if letter == ' ':
                letter = ' '
            else:
                if letter == '-':
                    if character == ch:
                        letter = ch
                        present = 1
                        fill = fill + 1
                    else:
                        letter = '-'
                else:
                    fill = fill + 1
                    letter = character
            update.append(letter)
        if present == 1:
            print(Fore.GREEN + "\nCorrect guess!")
        else:
            print(Fore.RED + "\nWrong guess!")
            life = life - 1
        updsample = update[i:i + no_words]
        placeholder = updsample
        upd = ''.join(updsample)
        linebreak()
        print(Fore.YELLOW + "Your movie: " + upd)
        i = i + no_words
        if fill == movie_letters:
            done = True
    if done:
        break


if life == 0:
    print(Fore.RED + "\nYou lost...Game over")
    print("The movie was: " + word)
else:
    print(Fore.GREEN + "\nCorrect guess!")
    print("Congratulations! You win!!")

print(Style.RESET_ALL)
linebreak()



