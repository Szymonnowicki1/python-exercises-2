# -*- coding: utf-8 -*-
# %%
number = 1
previousNumber = 0
 
# %%
while number <= 50:
    print(number + previousNumber)
    previousNumber = number
    number += 1
    
# %%
import random
my_number = random.randint(0,20)
guess = 10
print('Guess my number')
trials = 0

while guess != my_number:
    guess = int(input())
    
    trials += 1
    if guess == my_number:
        print('Gratulacje', my_number)
    elif guess > my_number:
        print("Sorry- my number is smaller than your guess, Try again!")
    else:
        print("Sorry- my number is greater than your guess, Try again!")

