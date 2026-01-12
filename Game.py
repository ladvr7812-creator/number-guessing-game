"""
Number Guessing Game
====================
A simple interactive game where the computer picks a random number 
and the player tries to guess it with hints.
"""
import random
# Generate a random secret number between 1 and 10
secretNo = random.randint(1,10)
# Display welcome message to the player
print("Welcome to Number Guessing Game!!")
print("I think the number between 1 to 10")
print()  # Empty line

# Initialize attempt counter to track how many guesses the player makes
attempts=0

# Main game loop - continues until player guesses correctly
while True:
    # Get player's guess and convert to integer
    guess = int(input(f"Enter the Guessing no:"))

    # Increment attempt counter
    attempts += 1
    
    # Check Condition
    if guess < secretNo :
        print("Too Low!, Try Again")
        print()
    elif guess > secretNo :
        print("Too high!, Try Again")
        print()
    else :
        print("Congratulation You Win!")
        print(f"You Guess the No in {attempts} attempts") 

        break     # Exit the game loop 