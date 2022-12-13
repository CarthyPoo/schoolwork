import random

name = input("what is your name? ")
print(f"Welcome back {name}")

print("Welcome, you will be playing a game where you just have to guess the number the computer choose from 1 to 10, you only have three chances to do so! \n ")
number = random.randint(1, 10)
for i in range(0, 3):
    user = int(input("guess the number "))
    if user == number:
        print(f"Yay, you guessed the correct number! It is {number}")
        break

if user != number:
    print(f"your guesses were incorrect, the correct number was {number}")
