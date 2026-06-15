#to generate a random number and asks the user to guess it
import random
number=random.randint(1, 100)
guesses = 0
num=-1
while num != number:
    guesses +=1
    num=int(input("Guess a number between 1 and 100: "))
    if num < number:
        print("Too low! Try again.")
    elif num > number:
        print("Too high! Try again.")

print("Congratulations! You guessed the number.")
print(f"The number of attempts:{guesses} ")