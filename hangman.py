import random

def display_hangman(wrong_guesses):
    """Display the hangman based on number of wrong guesses"""
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    return stages[wrong_guesses]

def hangman_game():
    # Predefined list of words
    words = ["python", "computer", "programming", "challenge", "keyboard", "monitor", "software", "hardware", "internet", "website"]
    
    # Select a random word
    word_to_guess = random.choice(words).upper()
    word_length = len(word_to_guess)
    
    # Initialize game variables
    guessed_letters = []
    correct_guesses = ["_"] * word_length
    incorrect_guesses = []
    max_incorrect = 6
    
    print("=" * 30)
    print("   WELCOME TO HANGMAN GAME")
    print("=" * 30)
    print(f"Word has {word_length} letters")
    print("You have 6 incorrect guesses allowed")
    print()
    
    # Main game loop
    while True:
        # Display hangman
        print(display_hangman(len(incorrect_guesses)))
        
        # Display current progress
        print("Word: " + " ".join(correct_guesses))
        print(f"Incorrect guesses remaining: {max_incorrect - len(incorrect_guesses)}")
        
        if incorrect_guesses:
            print(f"Wrong letters: {', '.join(incorrect_guesses)}")
        
        if guessed_letters:
            print(f"All guessed letters: {', '.join(sorted(guessed_letters))}")
        
        print()
        
        # Check win condition
        if "_" not in correct_guesses:
            print("🎉 Congratulations! You guessed the word:", word_to_guess)
            break
        
        # Check lose condition
        if len(incorrect_guesses) >= max_incorrect:
            print(display_hangman(len(incorrect_guesses)))
            print("💀 Game Over! The hangman is complete!")
            print(f"The word was: {word_to_guess}")
            break
        
        # Get player input
        try:
            guess = input("Enter a letter: ").upper().strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGame interrupted. Goodbye!")
            break
        
        # Validate input
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue
        
        if not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        # Process the guess
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            # Correct guess
            print(f"✅ Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    correct_guesses[i] = guess
        else:
            # Incorrect guess
            print(f"❌ Sorry, '{guess}' is not in the word.")
            incorrect_guesses.append(guess)
        
        print("-" * 30)
    
    # Ask to play again
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
        if play_again in ['y', 'yes']:
            hangman_game()
            break
        elif play_again in ['n', 'no']:
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

# Start the game
if __name__ == "__main__":
    hangman_game()