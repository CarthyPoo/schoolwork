import random

print("welcome to a password generator\n")
name = input("what is your name? ")
print(f"Welcome back {name}")

password = int(input("please enter how long you would like your password to be "))

a = "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()?"
p = "".join(random.sample(a, password))
print(p)
