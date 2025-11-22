# CtrlUno Arcade - Multi-Game Collection, Main Entry Point
# A comprehensive arcade game application featuring five distinct games and navigation menus
#
# Games Included:
# - Wordy: A word-guessing game with multiple difficulty levels (4, 5, or 8 letter words)
# - Tres: A card matching game inspired by Uno with unique punishment mechanics
# - Hangman: Classic word-guessing game with visual hangman display
# - Gambling Gauntlet: Progressive casino simulation with 7 tables and escalating stakes
# - Farkle: Classic dice game where players push their luck to score points
#
# Menus:
# - Main Menu: Central hub for game and menu selection
# - Help Menu: Comprehensive rules and instructions for all games
# - Quit Menu: Confirmation system for exiting the application
#
# Authors: Team CtrlUno (Gavin Knotts, Jabriel Neal, Joshua Casey)
# Version Control: GitHub for collaboration and project management

# Import turtle graphics library for user input dialogs
import turtle

# Import game modules
from wordy import wordy_menu
from tres import tres_main
from hangman import hangman_menu
from gambling_gauntlet import gauntlet_menu
from farkle import farkle_menu

# Import menu modules
from help_menu import help_menu
from quit_menu import quit_menu

# Import turtle graphics helper for message display
from gui import show_help_message

#------------------------------------------------------
# MAIN MENU FUNCTIONS
# Central navigation hub and application entry point
#------------------------------------------------------

def main_menu():
    """
    Primary navigation interface and application entry point.
    Provides access to all games, help system, and exit functionality.
    
    Available Options:
    1. Wordy: Word-guessing game with multiple difficulties
    2. Tres: Multi-player card matching game
    3. Hangman: Classic word-guessing with visual feedback
    4. Gambling Gauntlet: Progressive casino simulation
    5. Farkle: Dice game with push-your-luck mechanics
    6. Help: Comprehensive game documentation
    7. Quit: Confirmed application exit

    Features:
    - Clear option presentation with multiple input formats
    - Robust input validation and error handling
    - Seamless navigation between all application components
    - Fallback error handling for invalid selections

    Input Flexibility:
    - Accepts both numeric (1-7) and text-based inputs
    - Case-insensitive text matching
    - Alternative names supported (e.g., "gauntlet" for Gambling Gauntlet)
    """
    while True:
        menu_message = """
Choose a game or option:

1. Wordy
2. Tres
3. Hangman
4. Gambling Gauntlet
5. Farkle
6. Help
7. Quit"""

        show_help_message("===== CtrlUno Arcade - Main Menu =====", menu_message, wait_for_ok=False)

        game_input = turtle.textinput("Main Menu", "What would you like to play, or get help with? (Enter 1-7 or game name)")
        if game_input is None:
            show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
            continue
        game = game_input.lower()

        if game in ["wordy", "1"]:
            wordy_menu()
        elif game in ["tres", "2"]:
            tres_main()
        elif game in ["hangman", "3"]:
            hangman_menu()
        elif game in ["gambling gauntlet", "gambler's gauntlet", "gauntlet", "4"]:
            gauntlet_menu()
        elif game in ["farkle", "5"]:
            farkle_menu()
        elif game in ["help", "6"]:
            help_menu()
        elif game in ["quit", "7"]:
            quit_menu()
        else:
            show_help_message("Invalid Input", "Invalid option. Please try again.", wait_for_ok=False)

if __name__ == "__main__":
    main_menu()



