import random
def game(int):
    a = int(input("Enter the guessing number:"))
    for i in range(1,6):
        x = random.randint(1,10)
    if a==x:
        print("You guessed it correct.")
    else:
        print("You guessed it wrong.")
