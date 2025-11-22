# CtrlUno Arcade - Gambling Gauntlet Game
# Progressive casino simulation with 7 escalating tables

# Import Random module for game mechanics
import random

# Import turtle for graphical text input
import turtle

# Import turtle graphics helper for message display
from gui import show_game_message, show_help_message

#------------------------------------------------------
# GLOBAL VARIABLES - GAMBLING GAUNTLET GAME
# Progressive casino simulation with escalating stakes
#------------------------------------------------------

gauntlet_bankroll = 0    # Player's current money available for betting

#------------------------------------------------------
# GAMBLING GAUNTLET GAME FUNCTIONS
# Progressive casino simulation with 7 escalating tables
#------------------------------------------------------

def gauntlet_intro():
    """
    Sets the atmosphere for the Gambling Gauntlet experience.
    Establishes initial bankroll and explains the high-stakes progression system.
    
    Game Setup:
    - Starting bankroll: $1,000
    - Goal: Reach millionaire status through 7 tables
    - Risk: Bankruptcy ends the game immediately
    - Progressive difficulty and minimum bets
    """
    intro_message = """Welcome to the Gambling Gauntlet Casino.

You have $1,000 and a chance to leave a millionaire.

Each table has its own rules and odds.
Achieve the bankroll target, and you unlock the next game.

The farther you progress in the gauntlet,
the higher the bet minimums are.

Be warned: the house doesn't like losers.
Go broke, and you're out."""

    show_game_message("===== Gambling Gauntlet =====", intro_message, wait_for_ok=False)
    turtle.textinput("Begin the Gauntlet", "Press 'ENTER' to begin the first table...")

def gauntlet_heads_or_tails():
    """
    Table 1: Basic coin flip game with 1:1 payout odds.
    Entry-level gambling with simple 50/50 probability.
    
    Game Rules:
    - Choose heads (1) or tails (2)
    - Even money payout on wins
    - Target: Reach $3,000 to unlock next table
    - No minimum bet requirement
        
    Global Variables Modified:
        gauntlet_bankroll: Increased/decreased based on bet outcomes
    """
    global gauntlet_bankroll
    play = True
    
    while play:
        toss = [1, 2]
        result = random.choice(toss)
        
        try:
            wager_input = turtle.textinput("Table 1 Bet Amount", f"How much would you like to bet? (You have ${gauntlet_bankroll:,.2f})")
            if wager_input is None:
                show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                continue
            wager = int(wager_input)
        except ValueError:
            show_help_message("Invalid Input", "Invalid input. Please enter a valid dollar amount.", wait_for_ok=False)
            continue
        
        if wager > gauntlet_bankroll:
            show_help_message("Insufficient Funds", f"Stop playing around. You only have ${gauntlet_bankroll:,.2f}. Place your bet.", wait_for_ok=False)
            continue
        
        if wager <= 0:
            show_help_message("Invalid Bet", f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.", wait_for_ok=False)
            continue
        
        bet_input = turtle.textinput("Heads or Tails?", "1: Heads\n2: Tails")
        if bet_input is None:
            show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
            continue
        bet = bet_input.lower()
        
        if bet in ["1", "heads"]:
            bet = 1
        elif bet in ["2", "tails"]:
            bet = 2
        else:
            show_help_message("Invalid Bet", "That's a bad bet friend. Try again.", wait_for_ok=False)
            continue
        
        if result == bet:
            gauntlet_bankroll += wager
            show_game_message("You Win!", f"Bankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
        else:
            gauntlet_bankroll -= wager
            show_game_message("You Lose", f"Bankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
        
        if gauntlet_bankroll <= 0:
            show_game_message("Bankrupt!", "Ya gone broke kid... take out a loan", wait_for_ok=True)
            gauntlet_replay()
            break
        
        if gauntlet_bankroll >= 3000:
            play = False

def gauntlet_color_wheel():
    """
    Table 2: Three-color wheel with 3:1 payout odds.
    Increased risk and reward compared to coin flip.
    
    Game Rules:
    - Choose Red (1), Black (2), or Green (3)
    - Triple payout on correct guess
    - Target: Reach $15,000 to advance
    - 33.3% win probability
        """
    global gauntlet_bankroll
    play = True
    
    
    while play:
        colors = [1, 2, 3]
        result = random.choice(colors)
        
        try:
            wager_input = turtle.textinput("Table 2 Bet Amount", f"How much do you want to bet? (You have ${gauntlet_bankroll:,.2f})")
            if wager_input is None:
                show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                continue
            wager = int(wager_input)
        
        except ValueError:
            show_help_message("Invalid Input", "Invalid input. Please enter a valid dollar amount.", wait_for_ok=False)
            continue
        
        if wager > gauntlet_bankroll:
            show_help_message("Insufficient Funds", f"Keep dreaming buddy... You only got ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
            continue

        if wager <= 0:
            show_help_message("Invalid Bet", f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.", wait_for_ok=False)
            continue
        
        try:
            bet_input = turtle.textinput("Color Wheel", "Pick the color it will land on:\n1: Red\n2: Black\n3: Green")
            if bet_input is None:
                show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                continue
            bet = int(bet_input)
        
        except ValueError:
            show_help_message("Invalid Input", "That's a losing bet friend. Give it another shot. Please enter a number (1, 2, or 3).", wait_for_ok=False)
            continue

        if bet == result:
            gauntlet_bankroll += (wager * 3)
            show_game_message("You Win!", f"Bankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
            
            if gauntlet_bankroll >= 15000:
                show_game_message("Table Unlocked!", "You have unlocked the next table my friend... Best of luck.", wait_for_ok=False)
                break
        else:
            gauntlet_bankroll -= wager
            show_game_message("You Lose", f"The winning number was {result}\n\nBankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
            
            if gauntlet_bankroll <= 0:
                show_game_message("Bankrupt!", "Ya gone broke kid... take out a loan", wait_for_ok=True)
                gauntlet_replay()
                break

def gauntlet_cups():
    """
    Table 3: Five-cup shell game with 8.5:1 payout odds.
    Classic casino game with moderate difficulty.
    
    Game Rules:
    - Choose cup 1-5 hiding the prize
    - 8.5× payout on correct guess
    - Target: Reach $50,000 to advance
    - 20% win probability
        """
    global gauntlet_bankroll
    play = True
    
    while play:
        try:
            wager_input = turtle.textinput("Table 3 Bet Amount", f"How much would you like to bet? (You have ${gauntlet_bankroll:,.2f})")
            if wager_input is None:
                show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                continue
            wager = int(wager_input)
        except ValueError:
            show_help_message("Invalid Input", "Invalid input. Please enter a valid dollar amount.", wait_for_ok=False)
            continue
        
        if wager > gauntlet_bankroll:
            show_help_message("Insufficient Funds", f"Don't go getting funny now. You have ${gauntlet_bankroll:,.2f} to bet.", wait_for_ok=False)
            continue

        if wager <= 0:
            show_help_message("Invalid Bet", f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.", wait_for_ok=False)
            continue
        
        try:
            bet_input = turtle.textinput("Five Cups", "Pick a cup. (1-5)\n\nPAYS: 8.5:1")
            if bet_input is None:
                show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                continue
            bet = int(bet_input)
        except ValueError:
            show_help_message("Invalid Input", "Invalid input. Please enter a number (1-5).", wait_for_ok=False)
            continue
        
        if bet < 1 or bet > 5:
            show_help_message("Invalid Choice", "Can't let you do that friendo, try again (with 1-5)...", wait_for_ok=False)
            continue
        
        toss = [1, 2, 3, 4, 5]
        result = random.choice(toss)
        
        if result == bet:
            gauntlet_bankroll += (wager * 8.5)
            show_game_message("You Win!", f"Bankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
        else:
            gauntlet_bankroll -= wager
            show_game_message("You Lose", f"The winning cup was {result}\n\nBankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
        
        if gauntlet_bankroll <= 0:
            show_game_message("Bankrupt!", "Ya gone broke kid... take out a loan", wait_for_ok=True)
            gauntlet_replay()
            break
        
        if gauntlet_bankroll >= 50000:
            play = False

def gauntlet_clock():
    """
    Table 4: Clock hour guessing with 12:1 payout odds.
    Time-themed game with increased complexity.
    
    Game Rules:
    - Guess which hour (1-12) the clock lands on
    - 12× payout on correct guess
    - Target: Reach $125,000 to unlock the next challenge
    - 8.33% win probability
        """
    global gauntlet_bankroll
    hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    
    while True:
        actual_time = random.choice(hours)
        
        try:
            wager_input = turtle.textinput("Table 4 Bet Amount", f"How much are you betting? (You have ${gauntlet_bankroll:,.2f})")
            if wager_input is None:
                show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                continue
            wager = int(wager_input)
        except ValueError:
            show_help_message("Invalid Input", "Invalid input. Please enter a valid dollar amount.", wait_for_ok=False)
            continue
        
        if wager > gauntlet_bankroll:
            show_help_message("Insufficient Funds", f"Don't go getting funny now. You have ${gauntlet_bankroll:,.2f} to bet.", wait_for_ok=False)
            continue
        
        if wager <= 0:
            show_help_message("Invalid Bet", f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.", wait_for_ok=False)
            continue

        try:
            bet_input = turtle.textinput("Clock Game", "Guess which hour the clock will land on. (1-12)")
            if bet_input is None:
                show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                continue
            bet = int(bet_input)
        except ValueError:
            show_help_message("Invalid Input", "Invalid input. Please enter a number (1-12).", wait_for_ok=False)
            continue
        
        if bet < 1 or bet > 12:
            show_help_message("Invalid Choice", "Can't let you do that friendo, try again...", wait_for_ok=False)
            continue
        
        if bet == actual_time:
            gauntlet_bankroll += (wager * 12)
            show_game_message("You Win!!!", f"Bankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)

            if gauntlet_bankroll > 125000:
                show_game_message("Table Unlocked!", f"You have unlocked the next table with ${gauntlet_bankroll:,.2f} to play with.\n\nGood luck!", wait_for_ok=False)
                break
        else:
            gauntlet_bankroll -= wager
            show_game_message("You Lose", f"The right hour was {actual_time}.\n\nYour remaining bankroll is ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
            
            if gauntlet_bankroll <= 0:
                show_game_message("Bankrupt!", "Ya gone broke kid... Take out a loan.", wait_for_ok=True)
                gauntlet_replay()
                break

def gauntlet_rat_race():
    """
    Table 5: Sixteen-rat race with 20:1 payout odds.
    High-stakes animal racing simulation.
    
    Game Rules:
    - Choose winning rat number (1-16)
    - 20× payout on correct guess
    - Target: Reach $250,000 to advance
    - 6.25% win probability
        """
    global gauntlet_bankroll
    
    while True:
        winner = random.randint(1, 16)
        
        try:
            wager_input = turtle.textinput("Table 5 Bet Amount", f"How much would you like to bet? (You have ${gauntlet_bankroll:,.2f})")
            if wager_input is None:
                show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                continue
            wager = int(wager_input)
        
        except ValueError:
            show_help_message("Invalid Input", "Invalid input. Please enter a valid dollar amount.", wait_for_ok=False)
            continue
        
        if wager > gauntlet_bankroll:
            show_help_message("Insufficient Funds", f"You ain't that rich yet...\n\nYou only have ${gauntlet_bankroll:,.2f} to bet.", wait_for_ok=False)
            continue
        
        if wager <= 0:
            show_help_message("Invalid Bet", f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.", wait_for_ok=False)
            continue

        try:
            bet_input = turtle.textinput("Rat Race", "Choose the number of the winning rat. (1-16)")
            if bet_input is None:
                show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                continue
            bet = int(bet_input)
        
        except ValueError:
            show_help_message("Invalid Input", "Invalid input. Please enter a number (1-16).", wait_for_ok=False)
            continue
        
        if bet > 16 or bet < 1:
            show_help_message("Invalid Choice", "That is a losing bet my friend. There's only 16 rats to bet on...", wait_for_ok=False)
            continue
        
        if bet == winner:
            gauntlet_bankroll += wager * 20
            show_game_message("You Win!", f"Bankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
        else:
            gauntlet_bankroll -= wager
            show_game_message("You Lose", f"The winning rat was #{winner}\n\nBankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
        
        if gauntlet_bankroll <= 0:
            show_game_message("Bankrupt!", "Ya gone broke kid... take out a loan", wait_for_ok=True)
            gauntlet_replay()
            break
        
        if gauntlet_bankroll >= 250000:
            break

def gauntlet_num_guess():
    """
    Table 6: Secret number guessing with 50:1 payout and multiple attempts.
    Most complex table with interactive gameplay.
    
    Game Rules:
    - Guess secret number between 1-50
    - 3 attempts with "higher/lower" clues
    - 50× payout on correct guess within attempts
    - Target: Reach $500,000 to advance to final table
    - Variable win probability based on strategy
        """
    global gauntlet_bankroll
    
    while True:
        attempts = 0
        correct_number = random.randint(1, 50)
        
        try:
            wager_input = turtle.textinput("Table 6 Bet Amount", f"How much would you like to bet? (You have ${gauntlet_bankroll:,.2f})")
            if wager_input is None:
                show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                continue
            wager = int(wager_input)
        
        except ValueError:
            show_help_message("Invalid Input", "Invalid input. Please enter a valid dollar amount.", wait_for_ok=False)
            continue
        
        if wager > gauntlet_bankroll:
            show_help_message("Insufficient Funds", f"These are very high stakes, stop messing around... You have ${gauntlet_bankroll:,.2f} to play with", wait_for_ok=False)
            continue

        if wager <= 0:
            show_help_message("Invalid Bet", f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.", wait_for_ok=False)
            continue
        
        while True:
            try:
                bet_input = turtle.textinput("Secret Number", "Pick the secret number between 1 and 50")
                if bet_input is None:
                    show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
                    continue
                bet = int(bet_input)
            
            except ValueError:
                show_help_message("Invalid Input", "Invalid input. Please enter a number (1-50).", wait_for_ok=False)
                continue
            
            if bet < 1 or bet > 50:
                show_help_message("Invalid Choice", "Too close to the end to make a mistake like that...", wait_for_ok=False)
                continue
            
            if bet > correct_number:
                show_game_message("Too High! 👆", "Your guess is too high", wait_for_ok=False)
                attempts += 1
                
                if attempts >= 3:
                    gauntlet_bankroll -= wager
                    show_game_message("Out of Attempts", f"Unfortunately not this time.\n\nThe correct number was {correct_number}\n\nYour bankroll is ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
                    
                    if gauntlet_bankroll <= 0:
                        show_game_message("Bankrupt!", "Ya gone broke kid... take out a loan", wait_for_ok=True)
                        gauntlet_replay()
                        return
                    break
                continue
            
            elif bet < correct_number:
                show_game_message("Too Low! 👇", "Your guess is too low", wait_for_ok=False)
                attempts += 1
                
                if attempts >= 3:
                    gauntlet_bankroll -= wager
                    show_game_message("Out of Attempts", f"Unfortunately not this time.\n\nThe correct number was {correct_number}\n\nYour bankroll is ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
                    
                    if gauntlet_bankroll <= 0:
                        show_game_message("Bankrupt!", "Ya gone broke kid... take out a loan", wait_for_ok=True)
                        gauntlet_replay()
                        return
                    break
                continue
            
            elif bet == correct_number:
                gauntlet_bankroll += (wager * 50)
                show_game_message("VICTORIOUS! 💰", f"Congratulations, you are victorious!\n\nYour bankroll is ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
                break
        
        if gauntlet_bankroll >= 500000:
            show_game_message("Final Table Unlocked!", "Fantastic, quite incredible what you've done.\n\nAllow me to show you to our final table...\n\nBest of luck", wait_for_ok=False)
            break

def gauntlet_make_or_break():
    """
    Final Table: All-in coin flip determining ultimate victory or total loss.
    Climactic finale where entire bankroll is wagered on single flip.
    
    Game Rules:
    - Mandatory all-in bet (entire bankroll)
    - Simple heads or tails choice
    - Win: Double bankroll and complete gauntlet
    - Lose: Lose everything and end game
    - 50% win probability
    
    Post-Game: Humorous "fees and taxes" reduce final winnings significantly.
    """
    global gauntlet_bankroll
    play = True
    
    while play:
        toss = [1, 2]
        result = random.choice(toss)
        wager = gauntlet_bankroll
        
        show_game_message("ALL IN!", "You are all in on this hand.\n\nFinishing how you started...\n\nMay the Gauntlet be in your favor", wait_for_ok=False)
        
        bet_input = turtle.textinput("All In", "1: Heads\n2: Tails")
        if bet_input is None:
            show_help_message("No Input", "No input provided. Please try again.", wait_for_ok=False)
            continue
        bet = bet_input.lower()
        
        if bet in ["1", "heads"]:
            bet = 1
        
        elif bet in ["2", "tails"]:
            bet = 2
        
        else:
            show_help_message("Invalid Bet", "That's a bad bet friend. Try again.", wait_for_ok=False)
            continue
        
        if result == bet:
            gauntlet_bankroll += wager
            show_game_message("GAUNTLET COMPLETE!", f"You have completed the gauntlet!!\n\nYou get to cash out all your winnings.\n\nBankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
            
            after_tax = gauntlet_bankroll / 2
            show_game_message("Taxes...", f"After taxes of course that only leaves you with ${after_tax:,.2f}.", wait_for_ok=False)
            
            gauntlet_bankroll = gauntlet_bankroll / 2
            gauntlet_bankroll = gauntlet_bankroll - 20000 - 10000 - 5000 - 100000

            show_game_message("Final Profits", f"Oh and of course the gratuity, drink fee, parking, and a well...\n\nDon't worry about the rest.\n\nThis is your profits from today. Bye.\n\nProfits: ${gauntlet_bankroll:,.2f}", wait_for_ok=True)
            gauntlet_replay()
            break
        
        else:
            gauntlet_bankroll -= wager
            show_game_message("You Lose", f"Bankroll: ${gauntlet_bankroll:,.2f}", wait_for_ok=False)
        
        if gauntlet_bankroll <= 0:
            show_game_message("Bankrupt!", "Ya gone broke kid... take out a loan", wait_for_ok=True)
            gauntlet_replay()
            break

def gauntlet_menu():
    """
    Main Gambling Gauntlet orchestrator managing progression through all tables.
    Guides players through complete casino experience from start to finish.
    
    Table Progression:
    1. Introduction and rules explanation
    2. Table 1: Heads or Tails (reach $3K)
    3. Table 2: Color Wheel (reach $15K) 
    4. Table 3: Five Cups (reach $50K)
    5. Table 4: Clock Game (reach $125K)
    6. Table 5: Rat Race (reach $250K)
    7. Table 6: Secret Number (reach $500K)
    8. Final Table: Make or Break (all-in)
    
    Each table unlocks only after reaching the previous table's target bankroll.
    
    Global Variables Modified:
        gauntlet_bankroll: Reset to $1,000 at start, modified throughout progression
    """
    global gauntlet_bankroll
    gauntlet_bankroll = 1000
    
    gauntlet_intro()
    
    table1_msg = """TABLE 1: HEADS OR TAILS

The warm-up. A coin toss. 50/50.

Double or nothing until you hit $3,000.
No frills, just guts.

No minimum bet."""
    show_game_message("===== Table 1 =====", table1_msg, wait_for_ok=False)
    turtle.textinput("Begin Table 1", "Press 'Enter' to begin.")
    gauntlet_heads_or_tails()
    
    table2_msg = f"""TABLE 2: COLOR WHEEL

Three colors. One spin.
Red, Black, or Green.

Pick right, triple your bet.
Reach $15,000 and the next table opens.

You have ${gauntlet_bankroll:,.2f}"""
    show_game_message("===== Table 2 =====", table2_msg, wait_for_ok=False)
    turtle.textinput("Begin Table 2", "Press 'Enter' to begin.")
    gauntlet_color_wheel()
    
    table3_msg = f"""TABLE 3: FIVE CUPS

Five cups. One hides the jackpot.

The odds are steep, but the payout's sweet.
Hit $50,000 to move on.

You have ${gauntlet_bankroll:,.2f}"""
    show_game_message("===== Table 3 =====", table3_msg, wait_for_ok=False)
    turtle.textinput("Begin Table 3", "Press 'Enter' to begin.")
    gauntlet_cups()
    
    table4_msg = """TABLE 4: CLOCK GAME

Twelve hours. One guess.

Time is money.
Guess the hour, win big.
Reach $125,000 to unlock the next challenge."""
    show_game_message("===== Table 4 =====", table4_msg, wait_for_ok=False)
    turtle.textinput("Begin Table 4", "Press 'Enter' to begin.")
    gauntlet_clock()
    
    table5_msg = """TABLE 5: RAT RACE

Sixteen rats. One winner.

Place your bet.
If your rat wins, you're one step closer
to the big leagues.

$250,000 gets you through."""
    show_game_message("===== Table 5 =====", table5_msg, wait_for_ok=False)
    turtle.textinput("Begin Table 5", "Press 'Enter' to begin.")
    gauntlet_rat_race()
    
    table6_msg = """TABLE 6: SECRET NUMBER

One number between 1 and 50.
Three guesses.

This is where legends are made.
Hit the jackpot and reach $500,000
to face the final table."""
    show_game_message("===== Table 6 =====", table6_msg, wait_for_ok=False)
    turtle.textinput("Begin Table 6", "Press 'Enter' to begin.")
    gauntlet_num_guess()
    
    final_msg = f"""FINAL TABLE: MAKE OR BREAK

One coin toss. Heads or Tails.

Win, and you walk out with ${gauntlet_bankroll:,.2f}.
Lose, and the house takes everything."""
    show_game_message("===== FINAL TABLE =====", final_msg, wait_for_ok=False)
    turtle.textinput("Final Table", "Ready to flip the coin? Press ENTER to go all in...")
    gauntlet_make_or_break()

def gauntlet_replay():
    """
    Post-gauntlet navigation offering replay or menu return options.
    Handles player choice for continuing gambling or exploring other games.
    
    Navigation Options:
    - Continue: Restart Gambling Gauntlet from beginning
    - Main Menu: Return to game selection hub
    - Quit: Exit application
    
    Input validation ensures proper choice handling.
    """
    while True:
        gauntlet_play_again_input = turtle.textinput("Play Again?", "Would you like to play again? (yes/no):")
        if gauntlet_play_again_input is None:
            show_help_message("No Input", "No input provided. Exiting game.", wait_for_ok=False)
            break
        gauntlet_play_again = gauntlet_play_again_input.lower()

        if gauntlet_play_again in ["yes", "y"]:
            what_game_input = turtle.textinput("Continue or Main Menu?", "1: Keep playing Gambler's Gauntlet? Enter: 'Continue'\n2: Main Menu, Enter: 'Main Menu'")
            if what_game_input is None:
                show_help_message("No Input", "No input provided. Returning to main menu.", wait_for_ok=False)
                return
            what_game = what_game_input.lower()

            if what_game in ["continue", "1"]:
                gauntlet_menu()
                break

            elif what_game in ["main menu", "2"]:
                import main_menu
                main_menu.main_menu()
                return
        
        elif gauntlet_play_again in ["no", "n"]:
            import quit_menu
            quit_menu.quit_menu()

        else:
            show_help_message("Invalid Input", "Invalid choice. Please try again. Enter y/yes or n/no.", wait_for_ok=False)
