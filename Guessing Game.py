# Guessing Game
import random
print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty =  input("Choos a difficulty. Type 'easy' or 'hard':").lower().strip()
computer_guess = random.choice(range(100))
user_guess = int(input("Make a guess: "))
attemp = 5
guess_over = False
while not guess_over:
    if user_guess > computer_guess:
        print("too high")
        print("Guess again")
        attemp -= 1
        print(f"You have {attemp} remaining to guess the number.")
    elif user_guess < computer_guess:
        print("too low")
        print("Guess again")
        attemp -= 1
        print(f"You have {attemp} remaining to guess the number.")
    elif user_guess == computer_guess:
        print("You win.")
        guess_over = True
    if attemp == 0:
        print("You lose attemps")
        break