import random

options = ['Rock', 'Paper', 'Scissors']
computer = random.choice(options)
user = input("Enter 'r' for Rock, 'p' for Paper & 's' for scissors: ")

print("")

if user == "r":
    print("You chose Rock!")
if user == "p":
    print("You chose Paper!")
if user == "s":
    print("You chose Scissors!")

print(f"Computer played {computer}!")

if user == "r" and computer == "Scissors":
    print("===> You won the game!")
elif user == "p" and computer == "Rock":
    print("===> You won the game!")
elif user == "s" and computer == 'Paper':
    print("===> You won the game!")
elif user == "r" and computer == "Rock" or user == "p" and computer == "Paper" or user == "s" and computer == "Scissors":
    print("===> It's a draw.")
else:
    print("===> Oops, Computer won the game.")