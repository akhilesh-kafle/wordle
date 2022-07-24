import random
from colorama import *

words = ["seven","hello","crown","plant","money","earth","eight","other"]
word_number = random.randint(0,len(words)-1)
word = words[word_number]
print("Rules of the game")
print("Guess the WORDLE in six tries.")
print("Each guess must be a valid five-letter word. Hit the enter button to submit.")
print("After each guess, the color of the tiles will change to show how close your guess was to the word.")
print("Green: The letter W is in the word and in the correct spot.")
print("Yellow: The letter I is in the word but in the wrong spot.")
print("Black:The letter U is not in the word in any spot.")
print("")

def start_game():
    play = True 
    while play:
        attempt = 0 
        while attempt < 6:
            guess = input("Guess the word: ")
            output = ""
            if len(guess) != 5:
                print("Guess 5 lettered word")
            else:
                for i in range(word.__len__()):
                    if word[i] == guess[i]:
                        output = output + Back.GREEN + guess[i] + Back.RESET
                    elif guess[i] in word:
                        output = output + Back.YELLOW + guess[i] + Back.RESET
                    elif guess[i] not in word:
                        output = output + Back.BLACK + guess[i] + Back.RESET
                    else:
                        output = output + guess[i] + Back.RESET
                print(output)
                if guess == word:
                    print("Congrats! you did it")
                    break
            attempt = attempt + 1
        ask = input("Do you want to play again? y/n: ")
        if ask == "n":
            play = False
start_game()
