# First Python Game

import random

my_num = random.randint(1,100)
guess = 0
counter = 0
    
while guess != my_num and guess != "exit":
    guess = input("Enter a guess between 1 to 100")

    if guess == "exit":
        break
    guess = int(guess) 
    counter += 1

    if guess < my_num:
        print("Nope!, Too Low, Try Again.")
    elif guess > my_num:
        print("Oh Man, Too High")
    else:
        print("You Got it!")        
        print("Awesome, it Only Took You", counter, "tries!")
input()
