import random

print("===== welcome to the number guessing game =====")
number = random.randint(1, 50)
max_guesses = 5

for attempt in range(1, max_guesses + 1):
    question = int(input(f"Guess a number between 1 and 50 ({attempt}/{max_guesses}): "))

    if question == number:
        print("You guessed the right number!")
        break
    elif question > number:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")

    remaining_guesses = max_guesses - attempt
    if remaining_guesses > 0:
        print(f"You have {remaining_guesses} guesses left")
else:
    print(f"You have no guesses left, the number was {number}")

