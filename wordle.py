import random
from colorama import *

words = ["seven","hello","crown","plant","money","earth","eight","other"]
word_number = random.randint(0,len(words)-1)
word = words[word_number]

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
            attempt = attempt + 1
        ask = input("Do you want to play again? y/n: ")
        if ask == "n":
            play = False
start_game()