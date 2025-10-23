# CtrlUno Arcade - Tres Game
# Card matching game with unique punishment mechanics and multi-player support

# Import random library for deck shuffling and card selection
import random

# Import quit and help menus for navigation
import quit_menu
import help_menu

#------------------------------------------------------
# CARD LISTS - Tres GAME
# Card type definitions and deck composition
#------------------------------------------------------

# Card type definitions organized by color and value
RED_CARDS = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]
GREEN_CARDS = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]
BLUE_CARDS = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
YELLOW_CARDS = ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9"]
COLOR_CARDS = RED_CARDS + GREEN_CARDS + BLUE_CARDS + YELLOW_CARDS  # Standard numbered cards (36 total)
ZERO_CARDS = ["R0", "G0", "B0", "Y0"]  # Special zero-value cards (4 total)
SKIP_CARDS = ["RSKIP", "GSKIP", "BSKIP", "YSKIP"]  # Skip cards that skip the next player's turn (4 total in deck)
DRAW2_CARDS = ["RDRAW2", "GDRAW2", "BDRAW2", "YDRAW2"]  # Draw Two cards that force next player to draw 2 cards (4 total in deck)
REVERSE_CARDS = ["RREVERSE", "GREVERSE", "BREVERSE", "YREVERSE"]  # Reverse cards that change play direction (4 total in deck)
WILD_CARDS = ["WILD"]  # Wild cards that can change color (4 total in deck)
WILD_DRAW4_CARDS = ["WILD+4"]  # Wild Draw Four cards that change color and force next player to draw 4 cards (4 total in deck)
CARDS = COLOR_CARDS + ZERO_CARDS + WILD_CARDS  # Complete card type definitions

#------------------------------------------------------
# GLOBAL VARIABLES - TRES GAME
# Card game state tracking and deck management
#------------------------------------------------------

# Game state and availability tracking
color_card_limits = {}   # Tracks remaining copies of each color card (2 per card type)
zero_card_limits = {}    # Tracks remaining copies of each zero card (1 per color)
skip_card_limit = {}     # Tracks remaining skip cards (4 total)
draw2_card_limit = {}    # Tracks remaining draw two cards (4 total)
reverse_card_limit = {}  # Tracks remaining reverse cards (4 total)
wild_card_limit = {}     # Tracks remaining wild cards (4 total)
wild_draw4_card_limit = {}  # Tracks remaining wild draw four cards (4 total)
t = True                 # Loop control flag for player count input

#------------------------------------------------------
# TRES GAME FUNCTIONS
# Card matching game with unique punishment mechanics and multi-player support
#------------------------------------------------------

def deck_limits():
    """
    Initializes card availability tracking for deck management.
    Sets up proper card distribution matching physical card game rules.
    
    Card Distribution:
    - Color cards (R1-R9, G1-G9, etc.): 2 copies each
    - Zero cards (R0, G0, B0, Y0): 1 copy each
    - Skip Cards: (RSKIP, GSKIP, BSKIP, YSKIP): 4 total copies
    - Draw Two Cards: (RDRAW2, GDRAW2, BDRAW2, YDRAW2): 4 total copies
    - Reverse Cards: (RREVERSE, GREVERSE, BREVERSE, YREVERSE): 4 total copies
    - Wild cards: (WILD) 4 total copies
    - Wild Draw Four cards: (WILD+4) 4 total copies

    Global Variables Modified:
        color_card_limits, zero_card_limits, wild_card_limit, skip_card_limits, draw2_card_limits, reverse_card_limits, wild_draw4_card_limit: Initialize availability counters
    """
    global color_card_limits, zero_card_limits, skip_card_limits, draw2_card_limits, reverse_card_limits, wild_card_limit, wild_draw4_card_limit
    color_card_limits = {card: 2 for card in COLOR_CARDS}
    zero_card_limits = {card: 1 for card in ZERO_CARDS}
    skip_card_limits = {card: 4 for card in SKIP_CARDS}
    draw2_card_limits = {card: 4 for card in DRAW2_CARDS}
    reverse_card_limits = {card: 4 for card in REVERSE_CARDS}
    wild_card_limit = {card: 4 for card in WILD_CARDS}
    wild_draw4_card_limit = {card: 4 for card in WILD_DRAW4_CARDS}

def gen_deck():
    """
    Creates and shuffles a complete Tres deck following game specifications.
    Combines all card types with proper quantities and randomizes order.
    
    Deck Composition:
    - 72 color cards (36 types × 2 copies)
    - 4 zero cards (1 per color)
    - 4 wild cards
    Total: 80 cards
    
    Returns:
        list: Shuffled deck ready for dealing
    """
    # Create the deck with appropriate card counts
    deck = []
    
    # Add color cards (2 copies each)
    for card in COLOR_CARDS:
        deck.extend([card, card])
    
    # Add zero cards (1 copy each)
    deck.extend(ZERO_CARDS)
    
    # Add skip cards (4 copies each)
    for card in SKIP_CARDS:
        deck.extend([card, card, card, card])

    # Add draw two cards (4 copies each)
    for card in DRAW2_CARDS:
        deck.extend([card, card, card, card])

    # Add reverse cards (4 copies each)
    for card in REVERSE_CARDS:
        deck.extend([card, card, card, card])

    # Add WILD cards (4 copies)
    for card in WILD_CARDS:
        deck.extend([card, card, card, card])

    # Add WILD+4 cards (4 copies)
    for card in WILD_DRAW4_CARDS:
        deck.extend([card, card, card, card])

    # Shuffle and return
    random.shuffle(deck)
    return deck

# Initialize deck and discard pile at module level for game state persistence
deck = []
played_cards = []



def starting_hands():
    """
    Distributes initial 7-card hands to all players based on player count.
    Removes dealt cards from main deck to prevent duplication.
    
    Distribution Process:
    1. Get number of real players (2-4)
    2. Deal 7 consecutive cards to each player from shuffled deck
    3. Remove dealt cards from deck (28 cards for 4 players)
    4. Store hands in indexed player_hands list
    
    Global Variables Modified:
        player_hands: Populated with starting hands
        deck: Reduced by dealt cards (28 cards removed)
    """
    global player_hands, deck
    get_real_player_count()
    
    # Deal 7 cards to each real player and remove them from the deck
    # Keep player_hands as a list of 4 lists so other code indexing player_hands[2]/[3] stays valid
    player_hands = [[], [], [], []]

    # For each real player, slice 7 cards off the top of the deck and assign
    for p in range(real_player_count):
        start = p * 7
        end = start + 7
        player_hands[p] = list(deck[start:end])

    # Remove the dealt cards from the deck
    cards_dealt = real_player_count * 7
    deck = deck[cards_dealt:]

def setup_first_card():
    """
    Establishes initial game state by placing first card in play.
    Provides player readiness confirmation and game start sequence.
    
    Process:
    1. Draw top card from deck as starting play card
    2. Add card to discard pile tracking
    3. Display card to all players with privacy warnings
    4. Confirm all players are ready based on player count
    
    Global Variables Modified:
        current_card: Set to first card in play
        played_cards: First card added to discard pile
    """
    global current_card, deck, played_cards
    
    # Take the first card from the deck
    current_card = deck.pop(0)
    
    # Add it to the discard pile
    played_cards.append(current_card)
    
    print()
    
    if real_player_count == 2:
        player_hands[0]
        player_hands[1]
        print()
        get_ready()
        print(f"""
               |                                                                                                                                       |
               |                                                                                                                                       |
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |                                                                                                                                       |
               |                                                                                                                                       |
               """)

    elif real_player_count == 3:
        player_hands[0]
        player_hands[1]
        player_hands[2]
        get_ready()
        print(f"""
               |                                                                                                                                       |
               |                                                                                                                                       |
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |                                                                                                                                       |
               |                                                                                                                                       |
               """)
    
    elif real_player_count == 4:
        player_hands[0]
        player_hands[1]
        player_hands[2]
        player_hands[3]
        get_ready()
        print(f"""
               |                                                                                                                                       |
               |                                                                                                                                       |
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |          All players are ready. Game is starting...  If you are not player 1 please look away after the first card is shown.          |  
               |                                                                                                                                       |
               |                                                                                                                                       |
               """)

def draw_card():
    """
    Handles card drawing with automatic deck reshuffling when needed.
    Implements smart deck management to prevent game stoppage.
    
    Draw Logic:
    1. If deck has cards, draw from top
    2. If deck empty but discard pile has cards, reshuffle discard pile
    3. Keep one copy of current card on top of discard pile
    4. Return error if no cards available anywhere
    
    Returns:
        str: Drawn card identifier or None if no cards available
    
    Global Variables Modified:
        deck: Cards removed when drawn or replenished from discard pile
        played_cards: Reset to only current card after reshuffling
    """
    global deck, played_cards, current_card
    
    if deck:
        return deck.pop(0)
    
    # The deck is empty, check if we can reshuffle played cards
    elif len(played_cards) > 1:  # Need at least 2 cards (current + at least 1 played)
        print("The deck is empty! Reshuffling the discard pile...")
        
        # Create new deck from all played cards EXCEPT one instance of the current card
        cards_to_reshuffle = played_cards.copy()
        
        # Remove one instance of the current card (keep it on top of discard pile)
        if current_card in cards_to_reshuffle:
            cards_to_reshuffle.remove(current_card)
        
        # If we found cards to reshuffle
        if cards_to_reshuffle:
            # Shuffle and create new deck
            random.shuffle(cards_to_reshuffle)
            deck = cards_to_reshuffle
            
            # Reset played_cards to only contain the current card (one instance)
            played_cards = [current_card]
            
            return deck.pop(0)
    
    # No cards left at all
    print("Error: No cards left to draw. There is no way this should happen. Please play a card if you can.")
    print("Reminder your hand is:", player1_hand if 'player1_hand' in globals() else "unknown")
    print("The current card in play is:", current_card)
    print()
    return None

def get_ready():
    """
    Player readiness confirmation system.
    Ensures proper turn management and prevents accidental gameplay.
    Loops until valid confirmation received.
    
    Input Validation: Accepts 'y'/'yes' or 'n'/'no' responses only
    """
    response = input("Is everyone ready? (y/yes, or n/no): ").lower()
    if response == "yes" or response == "y":
        print()
        print("Everyone is ready!")
        player_hands[0]
    elif response == "no" or response == "n":
        print()
        print("Not everyone is ready. Please get ready.")
        get_ready()
    else:
        print()
        print("Invalid input. Please enter y/yes or n/no.")
        get_ready()

def tres_menu():
    """
    Displays welcome message and core rules for Tres game.
    Sets player expectations for gameplay mechanics and victory conditions.
    
    Key Information Provided:
    - Objective: First to play all cards wins
    - Matching rules: Colors or numbers
    - Tres punishment mechanic warning
    - Multi-player competitive nature
    """
    print("\n Welcome to Tres! \n Compete with other players to be the first to play all of your cards. \n Match either colors or numbers. \n But beware - when someone reaches exactly three cards, the punishment mechanic could activate! \n Good luck and may the odds be in your favor! \n (PS: You can quit at anytime by typing 'q/quit', or get help by typing 'h/help' during your turn.) \n")

def get_real_player_count():
    """
    Collects and validates number of human players for game session.
    Supports 2-4 players with input validation and error handling.
    
    Validation:
    - Must be integer between 2 and 4
    - Handles ValueError for non-numeric input
    - Loops until valid input received
    
    Global Variables Modified:
        real_player_count: Set to validated player count
        t: Loop control flag
    """
    global real_player_count, t
    while t:
        try:
            real_player_count = int(input("Enter the number of players (2-4): "))
            if 2 <= real_player_count <= 4:
                break
            else:
                print()
                print("Invalid input. Please enter a number between 2 and 4.")
        except ValueError:
            print()
            print("Invalid input. Please enter a valid number between 2 and 4.")
            print()

def player_1_hand():
    """
    Updates Player 1's hand reference for easy access during gameplay.
    Maintains synchronization with main player_hands data structure.
    
    Global Variables Modified:
        player1_hand: Direct reference to player_hands[0]
    """
    global player1_hand
    # Player hands are already updated when cards are played, no need to filter
    player1_hand = player_hands[0]

def player_2_hand():
    """
    Updates Player 2's hand reference for easy access during gameplay.
    Maintains synchronization with main player_hands data structure.
    """
    global player2_hand
    # Player hands are already updated when cards are played, no need to filter
    player2_hand = player_hands[1]

def player_3_hand():
    """
    Updates Player 3's hand reference for easy access during gameplay.
    Only relevant when player count >= 3.
    """
    global player3_hand
    # Player hands are already updated when cards are played, no need to filter
    player3_hand = player_hands[2]

def player_4_hand():
    """
    Updates Player 4's hand reference for easy access during gameplay.
    Only relevant when player count = 4.
    """
    global player4_hand
    # Player hands are already updated when cards are played, no need to filter
    player4_hand = player_hands[3]

def is_valid_play(card, current_card):
    """
    Determines if a proposed card play is legal according to Tres rules.
    Handles color matching, number matching, and wild card logic.
    
    Validation Rules:
    - Colors must match (first character): R, G, B, Y
    - Numbers must match (remaining characters): 0-9
    - Wild cards (Wild) are always playable and change color
    - Wild cards prompt for new color selection
    
    Args:
        card (str): Card player wants to play (e.g., "R5", "WILD")
        current_card (str): Current card on top of play pile
        
    Returns:
        tuple: (is_valid_boolean, updated_current_card)
               For wild cards, updated_card includes chosen color
    """
    # Convert input to uppercase for consistency
    card = card.upper()
    
    # Check if colors match (first character)
    if card[0] == current_card[0] or card == "WILD" or card == "WILD+4":
        if card == "WILD":
            valid_color = False
            while not valid_color:
                card_input = input("Wild card played! What color do you want to choose? (R, G, B, Y): ").lower()
                wild_card_input = card_input.upper()
                if wild_card_input in ["R", "G", "B", "Y"]:
                    print(f"You chose {card_input} as the new color.")
                    updated_card = wild_card_input + "WILD"  # Create updated card with new color
                    print("The card on top is now:", updated_card)
                    valid_color = True
                    return True, updated_card
                else:
                    print("Invalid color choice. Please choose R, G, B, or Y.")
                    # Continue loop until valid input

        if card == "WILD+4":
            valid_color = False
            while not valid_color:
                card_input = input("Wild Draw Four card played! What color do you want to choose? (R, G, B, Y): ").lower()
                wild_card_input = card_input.upper()
                if wild_card_input in ["R", "G", "B", "Y"]:
                    print(f"You chose {card_input} as the new color.")
                    updated_card = wild_card_input + "WILD+4"  # Create updated card with new color
                    print("The card on top is now:", updated_card)
                    valid_color = True
                    return True, updated_card
                else:
                    print("Invalid color choice. Please choose R, G, B, or Y.")
                    # Continue loop until valid input
        return True, current_card
    
    # Check if numbers match (characters after the first)
    if card[1:] == current_card[1:] or current_card[1:] in ["R", "G", "B", "Y"]:
        return True, current_card
        
    return False, current_card

def game_loop():
    """
    Main Tres gameplay engine managing turn-based card play.
    Handles player turns, card validation, win conditions, and privacy management.
    
    Turn Management:
    - Rotates through players based on real_player_count
    - Displays privacy warnings for multi-player sessions
    - Shows current game state (hand, top card)
    - Processes card plays and draw actions
    
    Win Conditions:
    - First player to empty hand wins immediately
    - Tres condition (3 cards) triggers special announcement
    
    Privacy Features:
    - Clear screen warnings between players
    - Individual hand display only during player's turn
    
    Global Variables Modified:
        current_card: Updated when valid cards are played
        player_hands: Cards removed when played, added when drawn
        played_cards: Tracks all cards played to discard pile
    """
    global player1_hand, player2_hand, player3_hand, player4_hand, played_cards, current_card
    
    game_over = False
    current_player = 1
    
    while not game_over:
        if current_player == 1:
            print("It is Player 1's turn.")
            print("Current card on top:", current_card)
            print("Your hand is currently:", player1_hand)

            # Check if the current card is a WILD card that needs color selection
            if current_card == "WILD":
                valid_color = False
                while not valid_color:
                    card_input = input("Wild card played! What color do you want to choose? (R, G, B, Y): ").lower()
                    wild_card_input = card_input.upper()
                    if wild_card_input in ["R", "G", "B", "Y"]:
                        print(f"You chose {card_input} as the new color.")
                        updated_card = wild_card_input + "WILD"  # Create updated card with new color
                        print("The card on top is now:", updated_card)
                        current_card = updated_card
                        print("Reminder your hand is currently:", player1_hand)
                        valid_color = True  # Exit the loop after valid color selection
                    else:
                        print("Invalid color choice. Please choose R, G, B, or Y.")
                        # Loop continues automatically until valid input

            print()

            valid_move = False
            while not valid_move:
                card_input = input("Which card would you like to play? Or 'draw/d' to draw a card from the deck: ").lower()
                print()
                card_input = card_input.upper()

                if card_input == "DRAW" or card_input == "D":
                    drawn_card = draw_card()
                    if drawn_card:
                        player1_hand.append(drawn_card)
                        print()
                        print("You drew:", drawn_card)
                        print("Your new hand is:", player1_hand)
                        print("Remember, the card on top is still:", current_card)
                        print()
                    continue

                elif card_input == "Q" or card_input == "QUIT":
                    quit_menu.quit_menu()

                elif card_input == "H" or card_input == "HELP":
                    help_menu.help_menu()

                elif card_input in player1_hand:
                    is_valid, updated_card = is_valid_play(card_input, current_card)
                    if is_valid:
                        player1_hand.remove(card_input)
                        # If it's a WILD card, use the updated card with color
                        if card_input == "WILD":
                            current_card = updated_card
                        else:
                            current_card = card_input
                        played_cards.append(card_input)
                        print("Player 1 played:", card_input)
                        print()
                        valid_move = True
                    
                        # Check win condition
                        if len(player1_hand) == 0:
                            print("Player 1 wins!")
                            game_over = True
                            break
                        # Check Tres condition
                        elif len(player1_hand) == 3:
                            print("Player 1 has TRES!")
                            # Implement Tres punishment later
                    else:
                        print()
                        print("Invalid move! Try again.")
                        print("Remember, the card on top is still:", current_card)
                        print("Remember your hand is currently:", player1_hand)
                        print()
                else:
                    print()
                    print("Invalid move! Try again.")
                    print("Remember, the card on top is still:", current_card)
                    print("Remember your hand is currently:", player1_hand)
                    print()
            print("\n" * 500)
            current_player = 2
                
        elif current_player == 2:
            print("It is Player 2's turn.")
            print("Current card on top:", current_card)
            print("Your hand is currently:", player2_hand)
            print()
            
            valid_move = False
            while not valid_move:
                card_input = input("Which card would you like to play? Or 'draw/d' to draw a card from the deck: ").lower()
                print()
                card_input = card_input.upper()

                if card_input == "DRAW" or card_input == "D":
                    drawn_card = draw_card()
                    if drawn_card:
                        player2_hand.append(drawn_card)
                        print()    
                        print("You drew:", drawn_card)
                        print("Your new hand is:", player2_hand)
                        print("Remember, the card on top is still:", current_card)
                        print()
                    continue

                elif card_input in player2_hand:
                    is_valid, updated_card = is_valid_play(card_input, current_card)
                    if is_valid:
                        player2_hand.remove(card_input)
                        # If it's a WILD card, use the updated card with color
                        if card_input == "WILD":
                            current_card = updated_card
                        else:
                            current_card = card_input
                        played_cards.append(card_input)
                        print("Player 2 played:", card_input)
                        print()
                        valid_move = True
                    
                        # Check win condition
                        if len(player2_hand) == 0:
                            print("Player 2 wins!")
                            game_over = True
                            break
                        # Check Tres condition
                        elif len(player2_hand) == 3:
                            print("Player 2 has TRES!")
                            # Implement Tres punishment later
                    else:
                        print()
                        print("Invalid move! Try again.")
                        print("Remember, the card on top is still:", current_card)
                        print("Remember your hand is currently:", player2_hand)
                        print()
                else:
                    print()
                    print("Invalid move! Try again.")
                    print("Remember, the card on top is still:", current_card)
                    print("Remember your hand is currently:", player2_hand)
                    print()

            if real_player_count >= 3:
                current_player = 3
            else:
                current_player = 1
                
        elif current_player == 3:
            print("""
               |                                            If you are not player 3 please look away.                                                  |
               |                                            If you are not player 3 please look away.                                                  |
               |                                            If you are not player 3 please look away.                                                  |
               |                                            If you are not player 3 please look away.                                                  |
               |                                            If you are not player 3 please look away.                                                  |
               |                                            If you are not player 3 please look away.                                                  |
               |                                            If you are not player 3 please look away.                                                  |
               |                                            If you are not player 3 please look away.                                                  |
               |                                            If you are not player 3 please look away.                                                  |
               |                                            If you are not player 3 please look away.                                                  |
               """)
            print("It is Player 3's turn.")
            print("Current card on top:", current_card)
            print("Your hand is currently:", player3_hand)
            print()
            
            valid_move = False
            while not valid_move:
                card_input = input("Which card would you like to play? Or 'draw/d' to draw a card from the deck: ").lower()
                print()
                card_input = card_input.upper()

                if card_input == "DRAW" or card_input == "D":
                    drawn_card = draw_card()
                    if drawn_card:
                        player3_hand.append(drawn_card)
                        print()
                        print("You drew:", drawn_card)
                        print("Your new hand is:", player3_hand)
                        print("Remember, the card on top is still:", current_card)
                        print()
                    continue

                elif card_input in player3_hand:
                    is_valid, updated_card = is_valid_play(card_input, current_card)
                    if is_valid:
                        player3_hand.remove(card_input)
                        # If it's a WILD card, use the updated card with color
                        if card_input == "WILD":
                            current_card = updated_card
                        else:
                            current_card = card_input
                        played_cards.append(card_input)
                        print("Player 3 played:", card_input)
                        print()
                        valid_move = True
                    
                        # Check win condition
                        if len(player3_hand) == 0:
                            print("Player 3 wins!")
                            game_over = True
                            break
                        # Check Tres condition
                        elif len(player3_hand) == 3:
                            print("Player 3 has TRES!")
                            # Implement Tres punishment later
                    else:
                        print()
                        print("Invalid move! Try again.")
                        print("Remember, the card on top is still:", current_card)
                        print("Remember your hand is currently:", player3_hand)
                        print()
                else:
                    print()
                    print("Invalid move! Try again.")
                    print("Remember, the card on top is still:", current_card)
                    print("Remember your hand is currently:", player3_hand)
                    print()

            if real_player_count == 4:
                current_player = 4
            else:
                current_player = 1
                
        elif current_player == 4:
            print("""
               |                                            If you are not player 4 please look away.                                                  |
               |                                            If you are not player 4 please look away.                                                  |
               |                                            If you are not player 4 please look away.                                                  |
               |                                            If you are not player 4 please look away.                                                  |
               |                                            If you are not player 4 please look away.                                                  |
               |                                            If you are not player 4 please look away.                                                  |
               |                                            If you are not player 4 please look away.                                                  |
               |                                            If you are not player 4 please look away.                                                  |
               |                                            If you are not player 4 please look away.                                                  |
               |                                            If you are not player 4 please look away.                                                  |
               """)
            print("It is Player 4's turn.")
            print("Current card on top:", current_card)
            print("Your hand is currently:", player4_hand)
            print()
            
            valid_move = False
            while not valid_move:
                card_input = input("Which card would you like to play? Or 'draw/d' to draw a card from the deck: ").lower()
                print()
                card_input = card_input.upper()

                if card_input == "DRAW" or card_input == "D":
                    drawn_card = draw_card()
                    if drawn_card:
                        player4_hand.append(drawn_card)
                        print()
                        print("You drew:", drawn_card)
                        print("Your new hand is:", player4_hand)
                        print("Remember, the card on top is still:", current_card)
                        print()
                    continue

                elif card_input in player4_hand:
                    is_valid, updated_card = is_valid_play(card_input, current_card)
                    if is_valid:
                        player4_hand.remove(card_input)
                        # If it's a WILD card, use the updated card with color
                        if card_input == "WILD":
                            current_card = updated_card
                        else:
                            current_card = card_input
                        played_cards.append(card_input)
                        print("Player 4 played:", card_input)
                        print()
                        valid_move = True
                    
                        # Check win condition
                        if len(player4_hand) == 0:
                            print("Player 4 wins!")
                            game_over = True
                            break
                        # Check Tres condition
                        elif len(player4_hand) == 3:
                            print("Player 4 has TRES!")
                            # Implement Tres punishment later
                    else:
                        print()
                        print("Invalid move! Try again.")
                        print("Remember, the card on top is still:", current_card)
                        print("Remember your hand is currently:", player4_hand)
                        print()
                else:
                    print("Invalid move! Try again.")
                    print("Remember, the card on top is still:", current_card)
                    print("Remember your hand is currently:", player4_hand)
                    print()

            current_player = 1

    # Ask about playing again after game ends
    while True:        
        tres_play_again = input("Would you like to play again? (yes/no): ").lower()

        if tres_play_again in ["yes", "y"]:
            what_game = input("\n1: Keep playing Tres?, Enter: \"Continue\"\n2: Main Menu, Enter: \"Main Menu\"\n\n").lower()

            if what_game in ["continue", "1"]:
                tres_main()
                break
           
            elif what_game in ["main menu", "2"]:
                return

        elif tres_play_again in ["no", "n"]:
            quit_menu.quit_menu()
            break
        
        else:
            print()
            print("Invalid choice. Please try again. Enter y/yes or n/no.")

def tres_main():
    """
    Primary entry point for Tres game sessions.
    Handles complete game setup, execution, and cleanup.
    
    Initialization Sequence:
    1. Reset all game state variables for clean start
    2. Generate and shuffle new deck
    3. Display rules and get player count
    4. Deal starting hands and set up first card
    5. Launch main game loop
    6. Handle post-game replay options
    
    Global Variables Reset:
        deck, played_cards, player_hands: Clean slate for new game
        Individual player hand references: Reset to empty lists
    """
    global deck, played_cards, player_hands, player1_hand, player2_hand, player3_hand, player4_hand
    
    # Reset deck and discard pile for new game
    deck = gen_deck()
    played_cards = []
    player_hands = [[], [], [], []]  # Reset player hands
    
    # Reset individual player hand globals
    player1_hand = []
    player2_hand = []
    player3_hand = []
    player4_hand = []
    
    tres_menu()
    deck_limits()
    starting_hands()
    player_1_hand()
    player_2_hand()
    if real_player_count >= 3:
        player_3_hand()
    if real_player_count == 4:
        player_4_hand()
    setup_first_card()
    game_loop()