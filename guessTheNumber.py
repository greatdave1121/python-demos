import random

random_Number = random.randint(1, 20)

print("I am thinking of a number between 1 and 20.")
secrete_Number = random_Number

guessed_Number = None

for guesses_Taken in range(1, 7):
    print("Take a guess.")

    try:
        guessed_Number = int(input())

    except ValueError:
        print("Invalid input! You must enter a number.")
        continue

    if guessed_Number > secrete_Number:
        print("Your guess is too high.")
    elif guessed_Number < secrete_Number:
        print("Your guess is too low.")
    else:
        break

if guessed_Number == secrete_Number:
    print(f"Good job! You guessed my number in {guesses_Taken} guesses!")
else:
    print(f"Nope! The number I was thinking of was {secrete_Number}")





    

