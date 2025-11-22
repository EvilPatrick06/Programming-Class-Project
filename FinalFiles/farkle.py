# CtrlUno Arcade - Farkle Game
# Classic dice game where players push their luck to score points
# Players roll dice and must score points or lose their turn

# Import Random module for dice rolling
import random

# Import turtle for graphical text input
import turtle

# Import turtle graphics helper for message display
from gui import show_game_message, show_help_message

#------------------------------------------------------
# GLOBAL VARIABLES - FARKLE GAME
# Dice-rolling game with risk/reward mechanics
#------------------------------------------------------

# Target score to win the game
FARKLE_TARGET = 1500

#------------------------------------------------------
# FARKLE GAME FUNCTIONS
# Classic dice game with push-your-luck mechanics
#------------------------------------------------------

def roll_dice(num):
    """
    Rolls specified number of dice.

    Args:
        num (int): Number of dice to roll

    Returns:
        list: List of dice values (1-6)
    """
    dice = []
    for i in range(num):
        dice.append(random.randint(1, 6))  # Roll a die (1-6)
    return dice

def score(dice):
    """
    Calculates score for a set of dice according to Farkle rules.

    Scoring Rules:
    - Three 1s = 1000 points
    - Three of any other number = number × 100 points
    - Single 1 = 100 points
    - Single 5 = 50 points

    Args:
        dice (list): List of dice values

    Returns:
        int: Total points for the dice
    """
    points = 0
    counts = {i: dice.count(i) for i in range(1, 7)}  # Count each number

    # First handle three-of-a-kind
    for i in range(1, 7):
        if counts[i] >= 3:
            if i == 1:
                points += 1000
            else:
                points += i * 100
            counts[i] -= 3  # Remove those dice so they aren't counted again

    # Remaining single 1s and 5s
    points += counts[1] * 100
    points += counts[5] * 50

    return points

def play_turn(player):
    """
    Executes a single player's turn with rolling, scoring, and decision-making.

    Turn Mechanics:
    - Start with 6 dice
    - Roll and choose dice to keep for points
    - Can keep rolling with remaining dice
    - If roll scores 0 points, turn ends with 0 (Farkle!)
    - Hot dice rule: Using all 6 dice resets to 6 again

    Args:
        player (str): Player name/identifier

    Returns:
        int: Total points earned this turn
    """
    show_game_message("Farkle", f"{player}, let's test your luck!", wait_for_ok=True)
    total = 0
    remaining_dice = 6  # Start with 6 dice

    while True:
        dice = roll_dice(remaining_dice)
        dice_display = " ".join([f"[{d}]" for d in dice])

        if score(dice) == 0:
            show_game_message("Farkle!", f"You rolled: {dice_display}\n\nWomp Womp! No points this turn.", wait_for_ok=True)
            return 0

        roll_score = score(dice)
        message = f"You rolled: {dice_display}\n\nPoints available in this roll: {roll_score}\nCurrent turn total: {total}"
        show_game_message(f"{player}'s Turn", message, wait_for_ok=False)

        keep_input = turtle.textinput("Keep Dice", "Enter dice to keep (e.g., '1 5' or '1 1 1') or 'stop' to bank points:")
        if keep_input is None:
            show_help_message("No Input", "No input provided. Ending turn.", wait_for_ok=False)
            break

        if keep_input.lower() == "stop":
            break

        keep_list = keep_input.split()
        keep_dice = []
        for k in keep_list:
            try:
                die_value = int(k)
                if die_value in dice:
                    keep_dice.append(die_value)
                    dice.remove(die_value)  # Remove from current roll
            except ValueError:
                show_help_message("Invalid Input", f"'{k}' is not a valid die value. Skipping.", wait_for_ok=False)
                continue

        if not keep_dice:
            show_help_message("No Dice Kept", "You didn't keep any valid dice. Try again.", wait_for_ok=False)
            continue

        kept_score = score(keep_dice)
        total += kept_score
        remaining_dice -= len(keep_dice)  # Reduce dice for next roll

        if remaining_dice == 0:
            show_game_message("Hot Dice!", "You used all dice! Resetting to 6 dice.", wait_for_ok=True)
            remaining_dice = 6  # Hot dice rule

        show_game_message("Turn Update", f"Points from kept dice: {kept_score}\nCurrent turn score: {total}\nDice remaining: {remaining_dice}", wait_for_ok=False)

        roll_again_input = turtle.textinput("Continue?", "Roll again? (y/n):")
        if roll_again_input is None or roll_again_input.lower() != "y":
            break

    return total

def play_game():
    """
    Main Farkle game loop managing multiple players and win conditions.

    Game Flow:
    - Two players alternate turns
    - First to reach target score wins
    - Displays running score totals
    - Announces winner when game ends

    Target Score: Defined by FARKLE_TARGET constant (default 10000)
    """
    scores = {"Player 1": 0, "Player 2": 0}
    current = "Player 1"

    while scores["Player 1"] < FARKLE_TARGET and scores["Player 2"] < FARKLE_TARGET:
        score_message = f"Current Scores:\nPlayer 1: {scores['Player 1']}\nPlayer 2: {scores['Player 2']}\n\nTarget Score: {FARKLE_TARGET}"
        show_game_message("Farkle Scores", score_message, wait_for_ok=True)

        points = play_turn(current)
        scores[current] += points

        result_message = f"{current} earned {points} points this turn.\n\n{current} now has {scores[current]} points."
        show_game_message("Turn Complete", result_message, wait_for_ok=True)

        current = "Player 2" if current == "Player 1" else "Player 1"

    # Game Over - Determine winner
    if scores["Player 1"] >= FARKLE_TARGET:
        winner_message = f"Game Over!\n\nPlayer 1 wins with {scores['Player 1']} points!\n\nPlayer 2 had {scores['Player 2']} points."
    else:
        winner_message = f"Game Over!\n\nPlayer 2 wins with {scores['Player 2']} points!\n\nPlayer 1 had {scores['Player 1']} points."

    show_game_message("Winner!", winner_message, wait_for_ok=True)
    farkle_playagain()

def farkle_playagain():
    """
    Post-game navigation for Farkle sessions.
    Offers options to replay Farkle, return to main menu, or quit application.

    Navigation Options:
    - Continue: Start new Farkle game
    - Main Menu: Return to game selection
    - Quit: Exit application entirely

    Input validation with clear error messages for invalid choices.
    """
    while True:
        farkle_play_again_input = turtle.textinput("Play Again?", "Would you like to play again? (yes/no):")
        if farkle_play_again_input is None:
            show_help_message("No Input", "No input provided. Exiting game.", wait_for_ok=False)
            break
        farkle_play_again = farkle_play_again_input.lower()

        if farkle_play_again in ["yes", "y"]:
            what_game_input = turtle.textinput("Play Again?", "1: Keep playing Farkle? Enter: 'Continue'\n2: Main Menu, Enter: 'Main Menu'")
            if what_game_input is None:
                show_help_message("No Input", "No input provided. Returning to main menu.", wait_for_ok=False)
                return
            what_game = what_game_input.lower()

            if what_game in ["continue", "1"]:
                farkle_menu()
                break

            elif what_game in ["main menu", "2"]:
                import main_menu
                main_menu.main_menu()
                break

        elif farkle_play_again in ["no", "n"]:
            import quit_menu
            quit_menu.quit_menu()

        else:
            show_help_message("Invalid Input", "Invalid choice. Please try again. Enter y/yes or n/no.", wait_for_ok=False)

def farkle_menu():
    """
    Farkle game introduction and initialization.
    Displays game rules, explains scoring, and launches gameplay.

    Setup Sequence:
    1. Display welcome message and rules
    2. Explain scoring system
    3. Start main game loop

    Provides clear expectations about Farkle mechanics and strategy.
    """
    welcome_message = """Welcome to Farkle!

A dice game of luck and risk!

Roll 6 dice and score points.
Keep rolling to increase your score...
But be careful!

If you roll and score nothing, you FARKLE and lose all points for that turn!

Scoring:
- Three 1s = 1000 points
- Three of any other number = number × 100
- Single 1 = 100 points
- Single 5 = 50 points

First to 10,000 points wins!

Good luck!"""
    show_game_message("===== Farkle =====", welcome_message, wait_for_ok=True)

    play_game()
