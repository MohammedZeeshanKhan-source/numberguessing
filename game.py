import random


def number_guessing_game() -> None:
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while True:
        guess_input = input("Enter your guess: ").strip()

        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break


if __name__ == "__main__":
    number_guessing_game()
