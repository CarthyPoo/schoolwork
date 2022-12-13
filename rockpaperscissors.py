import random

name = input("what is your name? ")
print("Welcome to Rock, Paper, Scissors", name + "!")
print("""In this game you will either pick Rock, Paper, or Scissors and the computer will pick one of those too!\n""")

option = ['rock', 'paper', 'scissors']

again = "yes"

while again == "yes":
    opt = random.randint(0, 2)

    computer = option[opt]

    player = input("pick rock, paper, or scissors. ")

    print(f"You picked {player}, and computer picked {computer}")
    if player == computer:
        print(f"Both of you picked {player}, It is a tie!")
    elif player == 'rock':
        if computer == 'paper':
            print("you lost")
    elif player == 'paper':
        if computer == 'scissors':
            print("you win")
        if computer == 'rock':
            print("you lose")
    elif player == 'scissors':
        if computer == 'rock':
            print("you lose")
        if computer == 'paper':
            print("you win")

    again = input("would you like to play again? ")
    if again == "no":
        print("thanks for playing")
        break
    elif not again == "yes":
        print("please say yes or no")
        again = input("would you like to play again? ")
