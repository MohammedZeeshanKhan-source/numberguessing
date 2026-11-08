import random
    
com =random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("computer is thinking of a number between 1 and 100.")
tries =0

while True:
    tries = tries + 1
    human = int(input("Enter your guess: "))

    if human < 1 or human > 100:

        print("Please enter a number between 1 and 100.")
        continue

    if(com == human):
        print("Congratulations! You guessed the correct number:", com)
        print("Number of tries:", tries)
        break

    elif (human < com):
        print("Your guess is too low. Try again.")
    else:
      print("Your guess is too high. Try again.")
        
human = int(input("Enter your guess: "))




