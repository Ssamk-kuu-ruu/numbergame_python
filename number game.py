import random

name = input("Hey y/n, What should I call you?: ")
numbers = random.randint(1,100)

numguess = 1

print(f"Welcome {name.title()}. Let's play 'Guess the number'.")
print("")
print("")

while True:
    print("-------------------")
    print("")
    print(f"Guess Attempt: {str(numguess)}")
    guesses = int(input("Guess a number between 1-100: "))


    if guesses < numbers:
        print("Your number is too low. Please guess again.")
        numguess += 1

    elif guesses > numbers:
        print("Your number is too high. Please guess again.")
        numguess += 1

    else:
        numguess += 1
        break

print("축하해!! You have guessed the right number!🎉👏🎊")

print("")
print("")
print("{------ NUMBER OF ATTEMPTS ------}")
print(f"...........{name.title()} = {numguess - 2}...........")
print("{-------------------------------}")
print("")