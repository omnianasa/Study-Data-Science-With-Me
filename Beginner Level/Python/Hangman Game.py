# Gues The number game
# omnia ayman
# Structure: 
# we will implement some functions to do the game into a big function called play
# functions will be needed: 1- random 2- check 3- play

import random

# First We need to identify the three channels of the game in lists
fruits = ["Banana", "Apple", "Strawberry", "Avocado", "Pineapple", "Watermelon",
          "Mango", "Kiwi", "Orange", "Berry", "Blueberry", "Cherry", "Lemon", "Apricot",
          "Figs", "Plum", "Papaya", "Grapefruit"]
transport = ["Car",	"Bike",	"Truck","Train","Bullet" ,	"Subway" ,"Gondola", "Rickshaw",
             "Horse Carriage",	"Sled"]
countries = ["Brazil", "Japan", "Egypt", "Canada", "Australia", "Kenya", "Germany", 
             "Thailand", "Mexico", "Sweden"] 

# Welcome the user with number input of the channel he wants to ply
print("Hi!! Nice to meet You in Hangman Game :>\nwhich type do you wnat to play?")
print("1- Fruits\n2- Transports\n3- Countries")
nameList = int(input("Enter the NUMBER you want to play by: "))

# Make The secret Word with random to get it from 
#inside the list using the user number input 
def Get_Random(nameList):
    match nameList:
        case 1:
            index = random.randint(0, 9)
            return fruits[index]
        case 2:
            index = random.randint(0, 9)
            return transport[index]
        case 3:
            index = random.randint(0, 9)
            return countries[index] 
        

# Start the Game by representing the boundaries of the word in secret        
def start_word(word):
    print("_ "* len(word))

# Uodate the word after every change from the user 
def show_Res(word, guessed_letters):
    #string is immutable so we convert it into a list
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display))

# Check every input letter from the user with the actual one    
def show_secret(secret_word,guessed_letters, check_letter = None):
    guessed_letters.append(check_letter)
    for i in secret_word:
        if i == check_letter:
            show_Res(secret_word, guessed_letters)
            return True
    else:
        return False

# General Function         
def play(value):
    
    Hung_word = Get_Random(value).lower()
    start_word(Hung_word)
    guessed_letters = []
    chances = len(Hung_word)
    
    while(chances != 0):
        letter = input("The Letter You Guess: ").lower()
        if show_secret(Hung_word,guessed_letters, letter):
            if all([char in guessed_letters for char in Hung_word]):
                print(f"Congrats! You've guessed the word '{Hung_word}' correctly!")
                break
        else:
            chances -= 1
            print(f"Wrong Guess :< Now you have {chances} chances left.")
        
        if chances == 0:
            print(f"You Are The Hangman!! The word was '{Hung_word}'. Goodbye.")
            break

            
        
        
play(nameList)

        
    
    
    

