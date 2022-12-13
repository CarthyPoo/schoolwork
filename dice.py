import random

print("welcome to the dice roller program!\n")
name = input("what is your name? ")
print(f"Welcome back {name}")
while True:
    print('''
    Type 1 to Roll the dice.
            
    Type 2 to exit
    ''')
    user = int(input("What would you like to do?\n "))
    if user == 1:
        number = random.randint(1, 6)
        print("you rolled", number)
    else:
        break
