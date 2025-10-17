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