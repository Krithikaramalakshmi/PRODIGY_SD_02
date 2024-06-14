import random
def generate(start=1, end=100):
    return random.randint(start, end)
def userguess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter an integer.")
def provide_feedback(guess, target):
    if guess < target:
        print("Too low! Try again.")
        return False
    elif guess > target:
        print("Too high! Try again.")
        return False
    else:
        print(f"Congratulations! You guessed the number {target} correctly.")
        return True
def play_guessing_game():
    number_to_guess = generate()
    attempts = 0
    guessed_correctly = False
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess the number!")
    while not guessed_correctly:
        guess = userguess()
        attempts += 1
        guessed_correctly = provide_feedback(guess, number_to_guess)
    print(f"It took you {attempts} attempts.")
if __name__ == "__main__":
    play_guessing_game()
