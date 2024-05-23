"""
Your module description
"""
import random

number = random.randint(1,10)

isGuessCorrect = False

while isGuessCorrect != True:
    guess = input("Please enter a number from  1-10: ")
    if int(guess)==number:
        isGuessCorrect = True
        print(f"You have guessed {guess}. Your guess is correct! You win!")
    else:
        print(f"You have guessed {guess}. Your guess is incorrect. Please try again")

#print(number)
