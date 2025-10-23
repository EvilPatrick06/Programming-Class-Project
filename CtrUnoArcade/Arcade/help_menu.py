# CtrlUno Arcade - Help Menu
# Comprehensive game documentation and rule explanations

# Import quit menu for navigation
import quit_menu 

#------------------------------------------------------
# HELP MENU FUNCTIONS
# Comprehensive game documentation and rule explanations
#------------------------------------------------------

def help_menu():
    """
    Interactive help system providing detailed rules for all arcade games.
    Offers comprehensive documentation with strategies and gameplay mechanics.
    
    Available Help Topics:
    1. Wordy: Word guessing rules, difficulty levels, feedback system
    2. Tres: Card matching rules, punishment mechanics, multi-player strategy
    3. Hangman: Classic rules, strategy tips, visual progression
    4. Gambling Gauntlet: All 7 tables, odds, progression requirements
    
    Navigation Features:
    - Return to help for additional topics
    - Access main menu or quit from help system
    - Input validation with clear error handling
    
    Each help section includes:
    - Basic rules and objectives
    - Detailed gameplay mechanics
    - Strategic tips and advice
    - Special features and unique mechanics
    """
    """Display the help menu options."""
    print("\n===== CtrlUno Arcade Help Menu =====\n")
    print("1. Wordy Rules")
    print("2. Tres Rules")
    print("3. Hangman Rules")
    print("4. Gambling Gauntlet Rules")
    print("5. Return to Main Menu")
    print("6. Quit")

    choice = input("\nWhat would you like help with? ").lower()

    if choice in ["1", "wordy"]:
        display_wordy_help()
        more_help()
    elif choice in ["2", "tres"]:
        display_tres_help()
        more_help()
    elif choice in ["3", "hangman"]:
        display_hangman_help()
        more_help()
    elif choice in ["4", "gambling gauntlet", "gauntlet"]:
        display_gauntlet_help()
        more_help()
    elif choice in ["5", "main", "menu", "main menu", "return"]:
        print()
        return "main"  # Return to main menu
    elif choice in ["6", "quit"]:
        quit_menu.quit_menu()
    else:
        print()
        print("Invalid option. Please try again.")
        help_menu()

def display_wordy_help():
        print("\n===== Wordy Help =====")
        print("""\n# Welcome to Wordy!
        Wordy is a word-guessing game inspired by Wordle, but with a difficulty twists:

        # Wordy Basic Rules

            - Words are randomly selected from a predefined list and can be of any length.
            - Choose your difficulty level: Easy has 4 letters, Medium has 6 letters, and Hard has 8 letters.
            - You have a limited number of attempts to guess the word (You only get 6 of them!).
            - Be strategic with your guesses to find the secret word in as few attempts as possible.
            - Any English word is allowed, including proper nouns. 
            - No special characters.

        # Feedback System

            After each guess, you'll receive feedback:
            
                - The number of letters in the correct position.
                - The number of correct letters but in the wrong position.

        # Strategy Tips

            - Start with common letters and vowels.
            - Use the feedback to eliminate impossible letters.
            - Pay attention to letter positions to narrow down possibilities.

        Good luck guessing the secret word!""")


def display_tres_help():
    print("\n===== Tres Help =====")
    print(""" Tres is a card game where players compete to be the first to play all of their cards. 
        Do this by matching either colors or numbers. 
        The game draws inspiration from Uno, but introduces a unique mechnic: 
        when a player reaches exactly three cards, a punishment round is triggered.

        # Tres Basic Rules

            - Match cards by either color or number.
            - Be the first to play all your cards to win.
            - Skip Card: Play a skip card to skip the next player's turn.
            - Wild Card: Play a wild card to change the current color to any color of your choice.
            - +2 Card: Play a +2 card to force the next player to draw two cards.
            - +4 Card: Play a +4 card to force the next player to draw four cards. 
            Also change the current color to a color of your choice.
            - Reverse Card: Play a reverse card to change the order of play.
            - You may stack +2 and +4 cards, has to be with the same type of card.
            - When you have exactly 3 cards, the punishment mechanic activates.

        # Punishment Mechanic

            When you have exactly 3 cards, you can initiate a punishment round:

                1. **Choose a Number**: Select a number between 1 and 100.
                2. **Secret Number**: The game randomly generates a secret number between 1 and 100.
                - If your number is **higher
                - If you match the **exact** secret number, the punishment effect is doubled (2x multiplier).
                3. Punishment Amount: The game randomly generates a number between 1 and 5 cards to draw as punishment.
                - If you guessed the exact secret number, this amount is doubled.
                - The punishment is applied either to you (if higher) or to all other players (if lower or exact).

           This mechanic adds suspense and strategic depth whenever a player reaches three cards. Good luck!""")

def display_hangman_help():
    print("\n===== Hangman Help =====")
    print("""Hangman is a classic word-guessing game where you try to guess a secret word letter by letter.

        # Hangman Basic Rules

            - A random word is selected from a large word list.
            - You see blank spaces representing each letter of the word.
            - Guess one letter at a time.
            - Correct guesses reveal the letter(s) in their position(s).
            - Incorrect guesses add a body part to the hangman figure.
            - You have 6 incorrect guesses before losing.
            - No special characters or numbers.

        # Strategy Tips

            - Start with common vowels (A, E, I, O, U).
            - Try frequently used consonants (R, S, T, L, N).
            - Use the word length as a clue.
            - Pay attention to letter patterns.

        Good luck saving the hangman!""")

def display_gauntlet_help():
    print("""\n===== Gambling Gauntlet Help =====

        The Gambling Gauntlet is a progressive casino game where you start with $1,000 and try to reach millionaire status.

        # Gambling Gauntlet Basic Rules

            - Start with $1,000 bankroll.
            - Progress through 6 tables plus a final all-in round.
            - Each table has different odds and a bankroll target to unlock the next table.
            - Go broke at any time and you're out.

        # The Tables

            1. **Heads or Tails** (1:1) - Reach $3,000
            2. **Color Wheel** (3:1) - Reach $15,000
            3. **Five Cups** (8.5:1) - Reach $50,000
            4. **Clock Game** (12:1) - Reach $125,000
            5. **Rat Race** (20:1) - Reach $250,000
            6. **Secret Number** (50:1) - Reach $500,000
            7. **Make or Break** (All-in) - Win big or lose everything
    
        # Strategy Tips

            - Manage your bankroll carefully.
            - Don't bet more than you can afford to lose.
            - Higher risk tables have higher payouts.
            - The final table is all or nothing.

        May the odds be ever in your favor!""")

def more_help():
    print()
    print("\n===== More Help =====")
    print("Would you like help with anything else? (y/n)")
    choice = input().lower()
    if choice in ["y", "yes"]:
        help_menu()
    elif choice in ["n", "no"]:
        print()
        return  # Exit help menu
    else:
        print()
        print("Invalid option. Please try again.")
        more_help()
    