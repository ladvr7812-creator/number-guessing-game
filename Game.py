"""
Number Guessing Game
====================
A simple interactive game where the computer picks a random number 
and the player tries to guess it with hints.
"""
import random

# Display welcome message to the player
print("=" * 50)
print("   WELCOME TO NUMBER GUESSING GAME!!")
print("=" * 50)
print()  # empty line

# Outer loop - allows playing multiple games
while True:
    # Generate a random secret number between 1 and 10
    secretNo = random.randint(1, 10)
    
    print("I'm thinking of a number between 1 to 10")
    print()
    
    # Initialize attempt counter to track how many guesses the player makes
    attempts = 0
    
    # Inner loop - continues until player guesses correctly
    while True:
        # Get player's guess and convert to integer
        guess = int(input("Enter your guess: "))
        
        # Increment attempt counter
        attempts += 1
        
        # Check Condition
        if guess < secretNo:
            print("Too Low! Try Again")
            print()
        elif guess > secretNo:
            print("Too High! Try Again")
            print()
        else:
            print()
            print("🎉 Congratulations! You Win! 🎉")
            print(f"You guessed the number in {attempts} attempts!")
            print()
            break  # Exit the inner game loop
    
    # Ask if player wants to play again (AFTER inner loop ends)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    # Check player's response
    if play_again == "yes" or play_again == "y":
        print()
        print("=" * 50)
        print("   STARTING NEW GAME!")
        print("=" * 50)
        print()
        # Loop continues automatically
    else:
        print()
        print("Thanks for playing! Goodbye! 👋")
        break  # Exit outer game loop
