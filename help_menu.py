# CtrlUno Arcade - Help Menu
# Comprehensive game documentation and rule explanations

# Import turtle for graphical text input
import turtle

# Import turtle graphics helper for message display
from gui import show_help_message

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
    menu_message = """
    Choose a help topic:

1. Wordy Rules
2. Tres Rules
3. Hangman Rules
4. Gambling Gauntlet Rules
5. Return to Main Menu
6. Quit"""

    show_help_message("===== CtrlUno Arcade Help Menu =====", menu_message, wait_for_ok=False)

    choice_input = turtle.textinput("Help Menu", "What would you like help with? (Enter 1-6 or game name)")
    if choice_input is None:
        show_help_message("No Input", "No input provided. Returning to main menu.", wait_for_ok=False)
        return "main"
    choice = choice_input.lower()

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
        return "main"  # Return to main menu
    elif choice in ["6", "quit"]:
        quit_menu.quit_menu()
    else:
        error_msg = "Invalid option. Please try again."
        show_help_message("Error", error_msg)
        help_menu()

def display_wordy_help():
    wordy_help = """
    Welcome to Wordy!
Wordy is a word-guessing game inspired by Wordle, with difficulty twists.

BASIC RULES:
- Words are randomly selected from a predefined list
- Choose difficulty: Easy (4 letters), Medium (6), Hard (8)
- You have 6 attempts to guess the word
- Any English word allowed, including proper nouns
- No special characters

FEEDBACK SYSTEM:
After each guess, you'll receive:
- Number of letters in correct position
- Number of correct letters in wrong position

STRATEGY TIPS:
- Start with common letters and vowels
- Use feedback to eliminate impossible letters
- Pay attention to letter positions

Good luck guessing the secret word!"""
    
    show_help_message("===== Wordy Help =====", wordy_help, wait_for_ok=False)


def display_tres_help():
    tres_help = """Tres is a card game where players compete to be the first to play all of their cards. 
Do this by matching either colors or numbers. 
The game draws inspiration from Uno, but introduces a unique mechnic: 
when a player reaches exactly three cards, a punishment round is triggered.

TRES BASIC RULES:
- Match cards by either color or number
- Be the first to play all your cards to win
- Skip Card: Play a skip card to skip the next player's turn
- Wild Card: Play a wild card to change the current color to any color of your choice
- +2 Card: Play a +2 card to force the next player to draw two cards
- +4 Card: Play a +4 card to force the next player to draw four cards and change the current color
- Reverse Card: Play a reverse card to change the order of play
- You may stack +2 and +4 cards, has to be with the same type of card
- When you have exactly 3 cards, the punishment mechanic activates

PUNISHMENT MECHANIC:
When you have exactly 3 cards, you can initiate a punishment round:

1. Choose a Number: Select a number between 1 and 100
2. Secret Number: The game randomly generates a secret number between 1 and 100
   - If your number is higher, you draw punishment cards
   - If your number is lower or exact, all other players draw punishment cards
   - If you match the exact secret number, the punishment effect is doubled (2x multiplier)
3. Punishment Amount: The game randomly generates a number between 1 and 5 cards to draw
   - If you guessed the exact secret number, this amount is doubled
   - The punishment is applied either to you (if higher) or to all other players (if lower or exact)

This mechanic adds suspense and strategic depth whenever a player reaches three cards. Good luck!"""

    show_help_message("===== Tres Help =====", tres_help, wait_for_ok=False)

def display_hangman_help():
    hangman_help = """Hangman is a classic word-guessing game where you try to guess a secret word letter by letter.

HANGMAN BASIC RULES:
- A random word is selected from a large word list
- You see blank spaces representing each letter of the word
- Guess one letter at a time
- Correct guesses reveal the letter(s) in their position(s)
- Incorrect guesses add a body part to the hangman figure
- You have 6 incorrect guesses before losing
- No special characters or numbers

STRATEGY TIPS:
- Start with common vowels (A, E, I, O, U)
- Try frequently used consonants (R, S, T, L, N)
- Use the word length as a clue
- Pay attention to letter patterns

Good luck saving the hangman!"""
    
    show_help_message("===== Hangman Help =====", hangman_help, wait_for_ok=False)

def display_gauntlet_help():
    gauntlet_help = """The Gambling Gauntlet is a progressive casino game where you start with $1,000 and try to reach millionaire status.

GAMBLING GAUNTLET BASIC RULES:
- Start with $1,000 bankroll
- Progress through 6 tables plus a final all-in round
- Each table has different odds and a bankroll target to unlock the next table
- Go broke at any time and you're out

TABLE PROGRESSION:
1. Heads or Tails (1:1) - Reach $3,000
2. Color Wheel (3:1) - Reach $15,000
3. Five Cups (8.5:1) - Reach $50,000
4. Clock Game (12:1) - Reach $125,000
5. Rat Race (20:1) - Reach $250,000
6. Secret Number (50:1) - Reach $500,000
7. Make or Break (All-in) - Win big or lose everything

STRATEGY TIPS:
- Manage your bankroll carefully
- Don't bet more than you can afford to lose
- Higher risk tables have higher payouts
- The final table is all or nothing

May the odds be ever in your favor!"""

    show_help_message("===== Gambling Gauntlet Help =====", gauntlet_help, wait_for_ok=False)

def more_help():
    choice_input = turtle.textinput("More Help?", "Would you like help with anything else? (y/n):")
    if choice_input is None:
        return
    choice = choice_input.lower()
    if choice in ["y", "yes"]:
        help_menu()
    elif choice in ["n", "no"]:
        return  # Exit help menu
    else:
        show_help_message("Invalid Input", "Invalid option. Please try again.", wait_for_ok=False)
        more_help()
    