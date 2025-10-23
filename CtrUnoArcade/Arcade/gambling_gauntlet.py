# CtrlUno Arcade - Gambling Gauntlet Game
# Progressive casino simulation with 7 escalating tables

# Import Random module for game mechanics
import random

# Import quit menu for navigation
import quit_menu

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
    print("\n\nWelcome to the Gambling Gauntlet Casino.\n")
    print("You have $1,000 and a chance to leave a millionaire.\n")
    print("Each table has its own rules and odds. Achieve the bankroll target, and you unlock the next game.\n")
    print("The farther you progress in the gauntlet, the higher the bet minimums are.")
    print("Be warned: the house doesn't like losers. Go broke, and you're out.\n")
    input("Press 'ENTER' to begin the first table...")

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
            wager = int(input("How much would you like to bet? $"))
        except ValueError:
            print()
            print("Invalid input. Please enter a valid dollar amount.")
            print()
            continue
        
        if wager > gauntlet_bankroll:
            print(f"Stop playing around. You only have ${gauntlet_bankroll:,.2f}. Place your bet.")
            continue
        
        if wager <= 0:
            print()
            print(f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.")
            print()
            continue
        
        bet = input("\n1: Heads\n2: Tails\n\n").lower()
        
        if bet in ["1", "heads"]:
            bet = 1
        elif bet in ["2", "tails"]:
            bet = 2
        else:
            print()
            print("That's a bad bet friend. Try again.")
            print()
            continue
        
        if result == bet:
            gauntlet_bankroll += wager
            print(f"You win!\n\nBankroll: ${gauntlet_bankroll:,.2f}")
        else:
            gauntlet_bankroll -= wager
            print(f"You lose...\n\nBankroll: ${gauntlet_bankroll:,.2f}")
        
        if gauntlet_bankroll <= 0:
            print("\n\nYa gone broke kid... take out a loan")
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
            wager = int(input("\n\nHow much do you want to bet buddy?\n\n$"))
        
        except ValueError:
            print()
            print("Invalid input. Please enter a valid dollar amount.")
            print()
            continue
        
        if wager > gauntlet_bankroll:
            print()
            print(f"Keep dreaming buddy... You only got ${gauntlet_bankroll:,.2f}")
            print()
            continue

        if wager <= 0:
            print()
            print(f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.")
            print()
            continue
        
        try:
            bet = int(input("Pick the color it will land on:\n1: Red\n2: Black\n3: Green\n\n"))
        
        except ValueError:
            print()
            print("\n\nThat's a losing bet friend. Give it another shot. Please enter a number (1, 2, or 3).")
            print()
            continue

        if bet == result:
            gauntlet_bankroll += (wager * 3)
            print("***********")
            print(f"\n\nYou win!\n\nBankroll: ${gauntlet_bankroll:,.2f}")
            print("***********")
            
            if gauntlet_bankroll >= 15000:
                print("You have unlocked the next table my friend... Best of luck.")
                break
        else:
            gauntlet_bankroll -= wager
            print("---------------------")
            print(f"\n\nYou lose...\n\nThe winning number was {result}\nBankroll: ${gauntlet_bankroll:,.2f}\n\n")
            print("---------------------")
            
            if gauntlet_bankroll <= 0:
                print("\n\nYa gone broke kid... take out a loan")
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
            wager = int(input("How much would you like to bet? $"))
        except ValueError:
            print()
            print("Invalid input. Please enter a valid dollar amount.")
            print()
            continue
        
        if wager > gauntlet_bankroll:
            print()
            print("Don't go getting funny now. You have ${gauntlet_bankroll:,.2f} to bet.")
            print()
            continue

        if wager <= 0:
            print()
            print(f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.")
            print()
            continue
        
        try:
            bet = int(input("\nPick a cup. (1-5)\n\nPAYS: 8.5:1\n\n"))
        except ValueError:
            print("Invalid input. Please enter a number (1-5).")
            continue
        
        if bet < 1 or bet > 5:
            print("Can't let you do that friendo, try again (with 1-5)...")
            print()
            continue
        
        toss = [1, 2, 3, 4, 5]
        result = random.choice(toss)
        
        if result == bet:
            gauntlet_bankroll += (wager * 8.5)
            print(f"You win!\n\nBankroll: ${gauntlet_bankroll:,.2f}")
        else:
            gauntlet_bankroll -= wager
            print("_______________________")
            print(f"You lose...\nThe winning cup was {result}\nBankroll: ${gauntlet_bankroll:,.2f}\n")
        
        if gauntlet_bankroll <= 0:
            print("\n\nYa gone broke kid... take out a loan")
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
            wager = int(input("How much are you betting?\n\n$"))
        except ValueError:
            print()
            print("Invalid input. Please enter a valid dollar amount.")
            print()
            continue
        
        if wager > gauntlet_bankroll:
            print()
            print("Don't go getting funny now. You have ${gauntlet_bankroll:,.2f} to bet.")
            print()
            continue
        
        if wager <= 0:
            print()
            print(f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.")
            print()
            continue

        try:
            bet = int(input("Guess which hour the clock will land on. (1-12)\n\n"))
        except ValueError:
            print("Invalid input. Please enter a number (1-12).")
            continue
        
        if bet < 1 or bet > 12:
            print()
            print("Can't let you do that friendo, try again...")
            print()
            continue
        
        if bet == actual_time:
            gauntlet_bankroll += (wager * 12)
            print()
            print(f"You win!!! ${gauntlet_bankroll:,.2f}")
            print()
            
            if gauntlet_bankroll > 125000:
                print(f"You have unlocked the next table with ${gauntlet_bankroll:,.2f} to play with.\nGood luck!")
                break
        else:
            gauntlet_bankroll -= wager
            print("\n__________________________________________________________________________________________________")
            print(f"You lost buddy.\nThe right hour was {actual_time}.\nYour remaining bankroll is ${gauntlet_bankroll:,.2f}.\n\n")
            
            if gauntlet_bankroll <= 0:
                print()
                print("Ya gone broke kid... Take out a loan.")
                print()
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
            wager = int(input("How much would you like to bet? $"))
        
        except ValueError:
            print()
            print("Invalid input. Please enter a valid dollar amount.")
            print()
            continue
        
        if wager > gauntlet_bankroll:
            print()
            print("You ain't that rich yet...")
            print(f"You only have ${gauntlet_bankroll:,.2f} to bet.")
            print()
            continue
        
        if wager <= 0:
            print()
            print(f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.")
            print()
            continue

        try:
            bet = int(input("Choose the number of the winning rat. (1-16)\n\n"))
        
        except ValueError:
            print("Invalid input. Please enter a number (1-16).")
            continue
        
        if bet > 16 or bet < 1:
            print("That is a losing bet my friend. There's only 16 rats to bet on...")
            continue
        
        if bet == winner:
            gauntlet_bankroll += wager * 20
            print(f"You win!\n\nBankroll: ${gauntlet_bankroll:,.2f}\n")
        else:
            gauntlet_bankroll -= wager
            print(f"You lose... Bankroll: ${gauntlet_bankroll:,.2f}\nThe winning rat was #{winner}")
        
        if gauntlet_bankroll <= 0:
            print("\n\nYa gone broke kid... take out a loan")
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
            wager = int(input("How much would you like to bet?\n\n$"))
        
        except ValueError:
            print()
            print("Invalid input. Please enter a valid dollar amount.")
            print()
            continue
        
        if wager > gauntlet_bankroll:
            print(f"These are very high stakes, stop messing around... You have ${gauntlet_bankroll:,.2f} to play with")
            continue

        if wager <= 0:
            print(f"Stop playing around. Bet at least $1. Remember you have ${gauntlet_bankroll:,.2f}. Place your bet.")
            continue
        
        while True:
            try:
                bet = int(input("\n\nPick the secret number between 1 and 50\n\n"))
            
            except ValueError:
                print("Invalid input. Please enter a number (1-50).")
                continue
            
            if bet < 1 or bet > 50:
                print("Too close to the end to make a mistake like that...")
                continue
            
            if bet > correct_number:
                print()
                print("Your guess is too high 👆")
                attempts += 1
                
                if attempts >= 3:
                    gauntlet_bankroll -= wager
                    print(f"Unfortunately not this time. The correct number was {correct_number}\n\nYour bankroll is ${gauntlet_bankroll:,.2f}")
                    
                    if gauntlet_bankroll <= 0:
                        print("\n\nYa gone broke kid... take out a loan")
                        gauntlet_replay()
                        return
                    break
                continue
            
            elif bet < correct_number:
                print()
                print("Your guess is too low 👇")
                attempts += 1
                
                if attempts >= 3:
                    gauntlet_bankroll -= wager
                    print(f"\n\nUnfortunately not this time. The correct number was {correct_number}\n\nYour bankroll is ${gauntlet_bankroll:,.2f}")
                    
                    if gauntlet_bankroll <= 0:
                        print("\n\nYa gone broke kid... take out a loan")
                        gauntlet_replay()
                        return
                    break
                continue
            
            elif bet == correct_number:
                gauntlet_bankroll += (wager * 50)
                print("***********************************")
                print(f"Congratulations, you are victorious.💰\n\nYour bankroll is ${gauntlet_bankroll:,.2f}")
                print("***********************************")
                break
        
        if gauntlet_bankroll >= 500000:
            print("Fantastic, quite incredible what you've done. Allow me to show you to our final table... Best of luck")
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
        
        print("You are all in on this hand. Finishing how you started... May the Gauntlet be in your favor")
        
        bet = input("\n1: Heads\n2: Tails\n\n").lower()
        
        if bet in ["1", "heads"]:
            bet = 1
        
        elif bet in ["2", "tails"]:
            bet = 2
        
        else:
            print()
            print("That's a bad bet friend. Try again.")
            print()
            continue
        
        if result == bet:
            gauntlet_bankroll += wager
            print()
            print(f"You have completed the gauntlet!! You get to cash out all your winnings.\n\nBankroll: ${gauntlet_bankroll:,.2f}")
            print(f"After taxes of course that only leaves you with ${gauntlet_bankroll/2:,.2f}.")
            
            gauntlet_bankroll = gauntlet_bankroll / 2
            gauntlet_bankroll = gauntlet_bankroll - 20000 - 10000 - 5000 - 100000

            print(f"Oh and of course the gratuity, drink fee, parking, and a well...\n\nDon't worry about the rest.\nThis is your profits from today. Bye.\n\nProfits: ${gauntlet_bankroll:,.2f}")
            gauntlet_replay()
            break
        
        else:
            gauntlet_bankroll -= wager
            print(f"You lose...\n\nBankroll: ${gauntlet_bankroll:,.2f}")
        
        if gauntlet_bankroll <= 0:
            print("\n\nYa gone broke kid... take out a loan")
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
    
    print("_____________________________________")
    print("\n\nTABLE 1: HEADS OR TAILS\n")
    print("The warm-up. A coin toss. 50/50.\n")
    print("Double or nothing until you hit $3,000. No frills, just guts.")
    input("No minimum bet.\n\nPress 'Enter' to begin.")
    gauntlet_heads_or_tails()
    
    print("\n\nTABLE 2: COLOR WHEEL\n")
    print("Three colors. One spin. Red, Black, or Green.\n")
    print("Pick right, triple your bet. Reach $15,000 and the next table opens.")
    print(f"you have ${gauntlet_bankroll:,.2f}")
    gauntlet_color_wheel()
    
    print("\n\nTABLE 3: FIVE CUPS\n")
    print("Five cups. One hides the jackpot.\n")
    print("The odds are steep, but the payout's sweet. Hit $50,000 to move on.")
    print(f"you have ${gauntlet_bankroll:,.2f}")
    gauntlet_cups()
    
    print("\n\nTABLE 4: CLOCK GAME\n")
    print("Twelve hours. One guess.\n")
    print("Time is money. Guess the hour, win big. Reach $125,000 to unlock the next challenge.")
    gauntlet_clock()
    
    print("\n\nTABLE 5: RAT RACE\n")
    print("Sixteen rats. One winner.\n")
    print("Place your bet. If your rat wins, you're one step closer to the big leagues. $250,000 gets you through.")
    gauntlet_rat_race()
    
    print("\n\nTABLE 6: SECRET NUMBER\n")
    print("One number between 1 and 50. Three guesses.\n")
    print("This is where legends are made. Hit the jackpot and reach $500,000 to face the final table.")
    gauntlet_num_guess()
    
    print("*****************************")
    print("\n\nFINAL TABLE: MAKE OR BREAK\n")
    print(f"One coin toss. Heads or Tails. Win, and you walk out with ${gauntlet_bankroll:,.2f}.\nLose, and the house takes everything.\n")
    input("Ready to flip the coin? Press ENTER to go all in...")
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
        gauntlet_play_again = input("\nWould you like to play again? (yes/no): ").lower()

        if gauntlet_play_again in ["yes", "y"]:
            what_game = input("\n1: Keep playing Gambler's Gauntlet?, Enter: \"Continue\"\n2: Main Menu, Enter: \"Main Menu\"\n\n").lower()

            if what_game in ["continue", "1"]:
                gauntlet_menu()
                break
            
            elif what_game in ["main menu", "2"]:
                return
        
        elif gauntlet_play_again in ["no", "n"]:
            quit_menu.quit_menu()
        
        else:
            print()
            print("Invalid choice. Please try again. Enter y/yes or n/no.")
