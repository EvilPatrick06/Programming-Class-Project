# ============================================================
# TRES GAME MODULE - CtrlUno Arcade Card Matching Game
# ============================================================
# Card matching game with unique punishment mechanics and multi-player support
# Features: 2-4 players, special cards (SKIP/DRAWTWO/REVERSE/WILD), Tres punishment mechanic

# EXTERNAL LIBRARY IMPORTS - Random number generation for shuffling and gameplay, turtle for card visuals
import random
import turtle

# SHARED MENU IMPORTS - Navigation to quit and help menus
import quit_menu
import help_menu

# Import turtle graphics helper for message display
from gui import show_game_message, verify_player_turn, tg_print, SCREEN_CLEAR

# ============================================================
# GAME CONSTANTS SECTION - Configuration values and shortcuts
# ============================================================

PUNISHMENT_THRESHOLD = 40  # TRES PUNISHMENT THRESHOLD - Maximum distance for successful punishment guess (1-100 range)

CARD_SHORTCUTS = {
    "W": "WILD", "W4": "WILD+4",
    "RD2": "RDRAWTWO", "GD2": "GDRAWTWO", "BD2": "BDRAWTWO", "YD2": "YDRAWTWO",
    "RS": "RSKIP", "GS": "GSKIP", "BS": "BSKIP", "YS": "YSKIP",
    "RR": "RREVERSE", "GR": "GREVERSE", "BR": "BREVERSE", "YR": "YREVERSE"
}

# ============================================================
# CARD TYPE DEFINITIONS - All card types in the Tres deck
# ============================================================

# NUMBERED CARDS - Standard playing cards with colors and values
COLOR_CARDS = [f"{c}{n}" for c in "RGBY" for n in range(1, 10)]  # NUMBERED CARDS 1-9: R/G/B/Y colors (72 total - 2 of each)
ZERO_CARDS = [f"{c}0" for c in "RGBY"]  # ZERO CARDS: Special cards with value 0, one per color (4 total)

# ACTION CARDS - Special effect cards that modify gameplay
SKIP_CARDS = [f"{c}SKIP" for c in "RGBY"]  # SKIP CARDS: Skip next player's turn (8 total - 2 per color)
DRAWTWO_CARDS = [f"{c}DRAWTWO" for c in "RGBY"]  # DRAW TWO CARDS: Force next player to draw 2 cards (8 total - 2 per color, stackable)
REVERSE_CARDS = [f"{c}REVERSE" for c in "RGBY"]  # REVERSE CARDS: Reverse turn order direction (8 total - 2 per color)

# WILD CARDS - Color-changing cards with special powers
WILD_CARDS = ["WILD"]  # WILD CARDS: Change color to any choice (4 total in deck)
WILD_DRAW4_CARDS = ["WILD+4"]  # WILD DRAW FOUR CARDS: Change color and force next player to draw 4 (4 total, stackable)

# CARD COLLECTIONS - Grouped card types for deck generation
WILDS = WILD_CARDS + WILD_DRAW4_CARDS  # ALL WILD CARDS: Combined wild and wild+4 types
SPECIAL_CARDS = SKIP_CARDS + DRAWTWO_CARDS + REVERSE_CARDS  # ALL SPECIAL ACTION CARDS
CARDS = COLOR_CARDS + ZERO_CARDS + SPECIAL_CARDS + WILDS  # COMPLETE CARD TYPE LIST: All possible card types

# ============================================================
# GAME STATE VARIABLES - Track current game status
# ============================================================

# GAME CONTROL FLAGS - Boolean flags for game flow and effects
t = True  # LOOP CONTROL FLAG: Controls main game loop execution
skip_in_effect = False  # SKIP EFFECT FLAG: True when next player should be skipped
drawtwo_in_effect = False  # DRAW TWO EFFECT FLAG: True when draw two is pending on next player
wild_plus_4_in_effect = False  # WILD PLUS FOUR EFFECT FLAG: True when wild+4 is pending on next player
drawtwo_accum = 0  # DRAW TWO ACCUMULATOR: Tracks stacked draw two penalties
wild_plus_4_accum = 0  # WILD PLUS FOUR ACCUMULATOR: Tracks stacked wild+4 penalties
reverse_order = False  # REVERSE ORDER FLAG: True when turn order is reversed (clockwise/counterclockwise)

# PLAYER STATE VARIABLES - Track player information and hands
real_player_count = 0  # ACTIVE PLAYER COUNT: Number of players in current game (2-4)
player_hands = []  # PLAYER HANDS LIST: Master list containing all player hands [player1, player2, player3, player4]
current_card = ""  # CURRENT CARD IN PLAY: Top card of the discard pile
current_player = 1  # CURRENT PLAYER NUMBER: Which player's turn it is (1-4)

# INDIVIDUAL PLAYER HAND REFERENCES - Direct access to each player's cards
player1_hand = []  # PLAYER ONE HAND: List of cards for player 1
player2_hand = []  # PLAYER TWO HAND: List of cards for player 2
player3_hand = []  # PLAYER THREE HAND: List of cards for player 3
player4_hand = []  # PLAYER FOUR HAND: List of cards for player 4

# ============================================================
# CORE GAME FUNCTIONS - Deck management and game setup
# ============================================================

def gen_deck():
    """
    Creates and shuffles a complete Tres deck.
    
    Deck: 72 color cards, 4 zeros, 8 skips, 8 draw-twos, 8 reverses, 8 wilds (100 total)
    """
    deck = (
        [card for card in COLOR_CARDS for _ in range(2)] +
        ZERO_CARDS +
        [card for card in SKIP_CARDS + DRAWTWO_CARDS + REVERSE_CARDS for _ in range(2)] +
        [card for card in WILD_CARDS + WILD_DRAW4_CARDS for _ in range(4)]
    )
    random.shuffle(deck)
    return deck

# DECK AND DISCARD PILE GLOBALS - Module-level game state persistence
deck = []  # MAIN DECK: Cards available to draw from
played_cards = []  # DISCARD PILE: Cards that have been played


def starting_hands():
    """
    Deals 7 cards to each player and removes them from deck.
    """
    global player_hands, deck
    get_real_player_count()
    
    player_hands = [[], [], [], []]
    for p in range(real_player_count):
        player_hands[p] = list(deck[p * 7:(p + 1) * 7])
    deck = deck[real_player_count * 7:]

def player_order():
    """Returns current player sequence based on reverse_order flag."""
    order = list(range(1, real_player_count + 1))
    return order[::-1] if reverse_order else order

def game_starting():
    """
    Displays game starting banner and waits for player readiness.
    """
    # GAME STARTING BANNER - ASCII art display for game countdown
    banner_line = "If all players are ready the Game will be starting..."
    border = f"               |{' ' * 172}|"
    content = f"               |          {banner_line:70}  {banner_line:70}                    |"
    print(f"\n{border}\n{border}\n{(content + chr(10)) * 15}{border}\n{border}\n")
    
    # Display in turtle graphics as well
    starting_message = "If all players are ready,\nthe game will be starting...\n\nGet ready to play Tres!"
    show_game_message("Game is Starting!", starting_message)
    print(SCREEN_CLEAR)

def setup_first_card():
    """
    Places first card from deck into play and starts game countdown.
    """
    global current_card, deck, played_cards
    current_card = deck.pop(0)
    played_cards.append(current_card)
    game_starting()

def draw_uno_card(x, y, card_name, width=60, height=90):
    """
    Draws a single UNO-style card at the specified position.
    
    Args:
        x (int): X coordinate for card center
        y (int): Y coordinate for card center
        card_name (str): Card identifier (e.g., "R5", "GWILD", "BDRAWTWO")
        width (int): Card width in pixels
        height (int): Card height in pixels
    """
    # Parse card color and value
    color_map = {
        'R': ('red', 'white'),
        'G': ('green', 'white'),
        'B': ('blue', 'white'),
        'Y': ('#FDDA0D', 'black')
    }
    
    if card_name.startswith(('R', 'G', 'B', 'Y')):
        color_char = card_name[0]
        card_value = card_name[1:]
        fill_color, text_color = color_map[color_char]
    else:
        # Uncolored wild cards
        fill_color, text_color = 'black', 'white'
        card_value = card_name
    
    # Draw rounded rectangle helper function
    def draw_rounded_rect(x_pos, y_pos, w, h, radius, color):
        turtle.penup()
        turtle.goto(x_pos - w/2 + radius, y_pos - h/2)
        turtle.setheading(0)
        turtle.pendown()
        turtle.color(color)
        turtle.begin_fill()
        
        # Bottom edge
        turtle.forward(w - 2*radius)
        # Bottom-right corner
        turtle.circle(radius, 90)
        # Right edge
        turtle.forward(h - 2*radius)
        # Top-right corner
        turtle.circle(radius, 90)
        # Top edge
        turtle.forward(w - 2*radius)
        # Top-left corner
        turtle.circle(radius, 90)
        # Left edge
        turtle.forward(h - 2*radius)
        # Bottom-left corner
        turtle.circle(radius, 90)
        
        turtle.end_fill()
    
    # Draw card outline (white border) with rounded corners
    draw_rounded_rect(x, y, width, height, 8, "white")
    
    # Draw card inner rectangle (colored) with rounded corners
    draw_rounded_rect(x, y, width - 6, height - 6, 6, fill_color)
    
    # Draw white oval in center
    turtle.penup()
    turtle.goto(x, y)
    turtle.color("white")
    turtle.dot(50)
    
    # Display card value/text
    turtle.penup()
    turtle.goto(x, y - 12)
    turtle.color(fill_color)
    
    # Simplify card display text
    display_text = card_value
    if "DRAWTWO" in card_value:
        display_text = "+2"
    elif "WILD+4" in card_value:
        display_text = "+4"
    elif "WILD" in card_value:
        display_text = "W"
    elif "SKIP" in card_value:
        display_text = "⊘"
    elif "REVERSE" in card_value:
        display_text = "⇄"
    
    font_size = 16 if len(display_text) <= 2 else 10
    turtle.write(display_text, align="center", font=("Arial", font_size, "bold"))
    
    turtle.penup()

def card_visuals(current_player, feedback_message=""):
    """
    Displays current player's hand and the top card using turtle graphics.
    """
    global current_card, player_hands

    screen = turtle.Screen()
    turtle.clearscreen()
    screen.tracer(0)
    screen.title(f"Tres - Player {current_player}'s Turn")
    turtle.hideturtle()
    screen.setup(width=1500, height=1000)
    
    # Display Current Player Indicator
    turtle.penup()
    turtle.goto(0, 320)
    turtle.color("black")
    turtle.write(f"Player {current_player}'s Turn", align="center", font=("Arial", 20, "bold"))

    # Display current card in play with visual
    turtle.penup()
    turtle.goto(0, 260)
    turtle.write("Current Card in Play:", align="center", font=("Arial", 14, "bold"))
    
    # Draw the current card visually
    draw_uno_card(0, 170, current_card, width=70, height=100)
    
    # Display feedback message if any (multi-line support)
    if feedback_message:
        turtle.penup()
        turtle.color("blue")
        # Split message into lines if it's too long
        lines = feedback_message.split('\n')
        start_y = 80
        for i, line in enumerate(lines):
            if line.strip():  # Only display non-empty lines
                turtle.goto(0, start_y - (i * 15))
                turtle.write(line, align="center", font=("Arial", 10, "normal"))

    # Display current player's hand label
    turtle.color("black")
    turtle.goto(0, 30)
    turtle.write("Your Hand:", align="center", font=("Arial", 14, "bold"))
    
    # Draw cards in player's hand
    hand = player_hands[current_player - 1]
    num_cards = len(hand)
    
    # Calculate spacing and starting position
    card_width = 60
    card_spacing = 70
    total_width = num_cards * card_spacing
    start_x = -total_width / 2 + card_spacing / 2
    card_y = -60
    
    for i, card in enumerate(hand):
        card_x = start_x + i * card_spacing
        draw_uno_card(card_x, card_y, card, width=card_width, height=90)
    
    # Instructions
    turtle.goto(0, -180)
    turtle.write("Enter your card choice below, or 'draw/d' to draw a card", align="center", font=("Arial", 10, "italic"))
    
    # Help text
    turtle.goto(0, -200)
    turtle.color("gray")
    turtle.write("(Type 'h' for help or 'q' to quit)", align="center", font=("Arial", 8, "italic"))
    
    turtle.update()
    
    # Ask user which card they want to play
    card_input = turtle.textinput(f"Player {current_player}'s Turn", "Which card would you like to play? Or 'draw/d' to draw a card from the deck:")

    return card_input

def draw_card():
    """
    Draws a card from deck; reshuffles discard pile if deck is empty.
    
    Returns drawn card or None if no cards available.
    """
    global deck, played_cards, current_card
    
    if deck:
        return deck.pop(0)
    
    # DECK EXHAUSTION HANDLING - Reshuffle discard pile when deck is empty
    if len(played_cards) > 1:
        print("The deck is empty! Reshuffling the discard pile...")
        cards_to_reshuffle = played_cards.copy()
        if current_card in cards_to_reshuffle:
            cards_to_reshuffle.remove(current_card)
        
        if cards_to_reshuffle:
            random.shuffle(cards_to_reshuffle)
            deck = cards_to_reshuffle
            played_cards = [current_card]
            return deck.pop(0)
    
    # ERROR CONDITION - No cards available in deck or discard pile
    hand_display = player1_hand if 'player1_hand' in globals() else "unknown"
    print(f"Error: No cards left to draw. There is no way this should happen. Please play a card if you can.\nReminder your hand is: {hand_display}\nThe current card in play is: {current_card}\n\n")
    return None

def tres_menu():
    """Displays welcome message and game rules."""
    welcome_message = """
Compete with other players to be the first to play all of your cards.
Match either colors or numbers.
But beware - when someone reaches exactly three cards,
the punishment mechanic could activate!

Good luck and may the odds be in your favor!

PS: You can quit at anytime by typing 'q/quit',
or get help by typing 'h/help' during your turn.

Card Shortcuts (lower case accepted):
- W for WILD
- W4 for WILD+4
- [Color]D2 for Draw Two (e.g., RD2, GD2, BD2, YD2)
- [Color]S for SKIP (e.g., RS, GS, BS, YS)
- [Color]R for REVERSE (e.g., RR, GR, BR, YR)"""
    
    show_game_message("Welcome to Tres!", welcome_message, wait_for_ok=False)

def draw_cards_and_display(current_player, num_cards, show_each=True, reason=None):
    """
    Draws multiple cards for a player and displays updated hand.
    
    Args:
        current_player (int): The player drawing cards
        num_cards (int): Number of cards to draw
        show_each (bool): Whether to print each card as it's drawn
        reason (str): Optional reason for drawing (e.g., "WILD+4 Attack", "Draw Two Attack")
    """
    drawn_cards_list = []
    
    for _ in range(num_cards):
        drawn_card = draw_card()
        if drawn_card:
            player_hands[current_player - 1].append(drawn_card)
            drawn_cards_list.append(drawn_card)
            if show_each:
                print(f"You drew: {drawn_card}")
    
    # Create feedback message with all drawn cards
    if drawn_cards_list:
        cards_str = ", ".join(drawn_cards_list)
        
        if reason:
            # Show reason along with drawn cards
            feedback_message = f"{reason}\n\nYou drew {num_cards} card{'s' if num_cards > 1 else ''}:\n\n{cards_str}\n\nYour new hand has {len(player_hands[current_player - 1])} cards"
        else:
            feedback_message = f"You drew {num_cards} card{'s' if num_cards > 1 else ''}:\n{cards_str}\n\nYour new hand has {len(player_hands[current_player - 1])} cards"
        
        # Show the drawn cards in turtle graphics
        show_game_message(f"Player {current_player} - Cards Drawn", feedback_message)
        
        print(f"Your new hand is: {player_hands[current_player - 1]}")

def advance_turn(player_sequence, current_index, clear_screen=True):
    """
    Advances to next player with pause and optional screen clear.
    """
    next_index = (current_index + 1) % len(player_sequence)
    turtle.textinput("Continue", "Press Enter when ready to continue...")
    if clear_screen:
        print(SCREEN_CLEAR)
    return next_index

# ============================================================
# TRES PUNISHMENT MECHANIC - Special 3-card punishment system
# ============================================================

def check_and_execute_tres(current_player, player_sequence):
    """
    Checks for Tres condition (3 cards) and offers optional punishment.
    
    Returns True if punishment executed, False otherwise.
    """
    if len(player_hands[current_player - 1]) == 3:
        tres_msg = f"Player {current_player} has exactly THREE cards!\n\nTRES!"
        show_game_message("TRES!", tres_msg, wait_for_ok=False)
        response = turtle.textinput("Tres Punishment", "Would you like to trigger the Tres punishment mechanic? (Y/Yes or N/No):")
        if response is None:
            print("No input provided. Tres punishment mechanic skipped.")
            turtle.textinput("Continue", "Press Enter when ready to continue...")
            return False
        response = response.lower()
        if response in ["y", "yes"]:
            execute_tres_punishment(current_player, player_sequence)
            return True
        print("Tres punishment mechanic skipped.")
        turtle.textinput("Continue", "Press Enter when ready to continue...")
        return False
    return False

def check_win_and_tres(current_player, player_sequence):
    """
    Checks for win (0 cards) or Tres (3 cards) conditions.
    
    Returns True if player won, False otherwise.
    """
    hand_size = len(player_hands[current_player - 1])
    if hand_size == 0:
        win_msg = f"Congratulations!\n\nPlayer {current_player} WINS!"
        show_game_message("WINNER!", win_msg)
        return True
    if hand_size == 3:
        check_and_execute_tres(current_player, player_sequence)
    return False

def execute_tres_punishment(current_player, player_sequence):
    """
    Executes Tres punishment: guess 1-100, others draw if you're close, you draw if not.
    
    - Exact match: Others draw 2x punishment
    - Within 40: Others draw normal punishment  
    - Outside 40: You draw punishment
    """
    print("Tres punishment mechanic activated!")
    secret_number = random.randint(1, 100)
    
    while True:
        try:
            guess_input = turtle.textinput("Tres Punishment", "Guess a number between 1 and 100:")
            if guess_input is None:
                print("\n\nNo input provided. Please try again.\n\n")
                continue
            guess = int(guess_input)
            if 1 <= guess <= 100:
                break
            print("\n\nInvalid input. Please guess a number between 1 and 100.\n\n")
        except ValueError:
            print("\n\nInvalid input. Please enter a valid integer between 1 and 100.\n\n")
    
    # PUNISHMENT CALCULATION - Determine who draws cards and how many
    others = [p for p in player_sequence if p != current_player]
    if guess == secret_number:
        result_msg = f"Incredible! You guessed the EXACT number!\n\nThe secret number was {secret_number}!\n\nEveryone else will be punished DOUBLE!"
        punishment_amount, targets = random.randint(1, 10) * 2, others
    elif abs(guess - secret_number) <= PUNISHMENT_THRESHOLD:
        result_msg = f"Good guess! You were within {PUNISHMENT_THRESHOLD}!\n\nThe secret number was {secret_number}!\nYour guess was {guess}!\n\nEveryone else will be punished!"
        punishment_amount, targets = random.randint(1, 10), others
    else:
        result_msg = f"You failed! Your guess was not within {PUNISHMENT_THRESHOLD}!\n\nThe secret number was {secret_number}!\nYour guess was {guess}!\n\nYOU will be punished!"
        punishment_amount, targets = random.randint(1, 10), [current_player]
    
    # Show result message
    show_game_message("Tres Punishment Result", result_msg)
    
    # PUNISHMENT APPLICATION - Draw cards for targeted players
    drawn_cards_msg = []
    for p in targets:
        cards_drawn = []
        for _ in range(punishment_amount):
            drawn_card = draw_card()
            if drawn_card:
                player_hands[p - 1].append(drawn_card)
                cards_drawn.append(drawn_card)
                if p == current_player:
                    print(f"You drew: {drawn_card}")
        
        if p == current_player:
            drawn_cards_msg.append(f"You drew {punishment_amount} cards: {', '.join(cards_drawn)}")
        else:
            drawn_cards_msg.append(f"Player {p} drew {punishment_amount} cards")
    
    # Show punishment summary
    punishment_summary = f"{'Everyone else' if current_player not in targets else 'You'} must draw {punishment_amount} cards!\n\n" + "\n".join(drawn_cards_msg)
    if current_player in targets:
        punishment_summary += f"\n\nYour new hand has {len(player_hands[current_player - 1])} cards"
    
    show_game_message("Punishment Applied", punishment_summary)

# ============================================================
# TURN HANDLING FUNCTIONS - Player turn processing and validation
# ============================================================

def handle_player_turn(current_player, player_sequence):
    """
    Processes one player's turn: display hand, accept card/draw input, validate play, check win.
    
    Returns: (game_over, player_sequence, reverse_played)
    """
    global current_card, played_cards, skip_in_effect, drawtwo_in_effect
    global wild_plus_4_in_effect, drawtwo_accum, wild_plus_4_accum, reverse_order
    global player1_hand, player2_hand, player3_hand, player4_hand
    
    # PLAYER VERIFICATION - Show blank screen to prevent hand peeking
    verify_player_turn(current_player)
    
    print(SCREEN_CLEAR)
    print(f"It is Player {current_player}'s turn.\nCurrent card on top: {current_card}\nYour hand is currently: {player_hands[current_player - 1]}\n\n")

    valid_move = False
    game_over = False
    reverse_played = False
    feedback_message = ""
    
    while not valid_move:
        card_input = card_visuals(current_player, feedback_message)  # Display current player's hand and the top card using turtle graphics
        feedback_message = ""  # Clear feedback after displaying
        
        if card_input is None:
            feedback_message = "No input provided. Please try again."
            print("\n\nNo input provided. Please try again.\n\n")
            continue
            
        card_input = card_input.upper()

        # DRAW CARD OPTION - Player chooses to draw instead of playing
        if card_input in ("DRAW", "D"):
            drawn_card = draw_card()
            if drawn_card:
                player_hands[current_player - 1].append(drawn_card)
                feedback_message = f"You drew: {drawn_card}"
                print(f"\n\nYou drew: {drawn_card}\nYour new hand is: {player_hands[current_player - 1]}\nRemember, the card on top is still: {current_card}\n\n")
            continue

        # MENU NAVIGATION OPTIONS - Quit or help during turn
        if card_input in ("Q", "QUIT"):
            quit_menu.quit_menu()
            continue
        if card_input in ("H", "HELP"):
            help_menu.help_menu()
            continue
        
        # CARD INPUT PROCESSING - Convert shortcuts and validate card play
        card_input = CARD_SHORTCUTS.get(card_input, card_input)

        if card_input in player_hands[current_player - 1]:
            is_valid, updated_card = is_valid_play(card_input, current_card)
            if is_valid:
                player_hands[current_player - 1].remove(card_input)
                
                # CARD PLAY EXECUTION - Update game state with played card
                current_card = updated_card if card_input in ("WILD", "WILD+4") else card_input
                played_cards.append(card_input)

                # SPECIAL CARD EFFECTS - Activate card-specific effects
                if card_input.endswith("SKIP"):
                    skip_in_effect = True
                elif card_input.endswith("DRAWTWO"):
                    drawtwo_in_effect = True
                    drawtwo_accum += 2
                elif card_input.endswith("WILD+4"):
                    wild_plus_4_in_effect = True
                    wild_plus_4_accum += 4
                elif card_input.endswith("REVERSE"):
                    reverse_order = not reverse_order
                    player_sequence = player_order()
                    reverse_played = True
                
                valid_move = True

                # WIN AND TRES CONDITION CHECKS - Check for game end or punishment
                if len(player_hands[current_player - 1]) == 0:
                    print(f"Player {current_player} wins!")
                    game_over = True
                    break
                check_and_execute_tres(current_player, player_sequence)
        
        # INVALID MOVE ERROR - Display error message for illegal plays
        if not valid_move:
            feedback_message = f"Invalid move! Card must match color, number, or type and must be in your hand. Try again. Card on top: {current_card}"
            print(f"\n\nInvalid move! Try again.\nRemember, the card on top is still: {current_card}\nRemember your hand is currently: {player_hands[current_player - 1]}\n\n")
    
    update_player_hands()
    return game_over, player_sequence, reverse_played

# ============================================================
# PLAYER SETUP FUNCTIONS - Player count and hand management
# ============================================================

def get_real_player_count():
    """
    Prompts for and validates player count (2-4).
    """
    global real_player_count, t
    while t:
        try:
            player_count_input = turtle.textinput("Player Count", "Enter the number of players (2-4):")
            if player_count_input is None:
                print("\n\nNo input provided. Please try again.\n\n")
                continue
            real_player_count = int(player_count_input)
            if 2 <= real_player_count <= 4:
                break
            print("\n\nInvalid input. Please enter a number between 2 and 4.\n\n")
        except ValueError:
            print("\n\nInvalid input. Please enter a valid number between 2 and 4.\n\n")

def update_player_hands():
    """
    Syncs individual player_hand variables with player_hands list.
    """
    global player1_hand, player2_hand, player3_hand, player4_hand
    player1_hand, player2_hand = player_hands[0], player_hands[1]
    if real_player_count >= 3:
        player3_hand = player_hands[2]
    if real_player_count == 4:
        player4_hand = player_hands[3]

# ============================================================
# CARD VALIDATION FUNCTIONS - Play legality and wild card handling
# ============================================================

def prompt_wild_color(card):
    """
    Prompts player to choose color for wild card (R/G/B/Y).
    
    Returns color-prefixed card (e.g., "RWILD", "GWILD+4").
    """
    while True:
        choice = turtle.textinput("Wild Card Color", f"You played {card}! What color do you want to choose? (R, G, B, Y):")
        if choice is None:
            print("\n\nNo input provided. Please try again.\n\n")
            continue
        choice = choice.upper()
        if choice in ["R", "G", "B", "Y"]:
            updated_card = choice + card
            color_names = {"R": "RED", "G": "GREEN", "B": "BLUE", "Y": "YELLOW"}
            print(f"You chose {choice} as the new color.\nThe card on top is now: {updated_card}")
            return updated_card
        print("\n\nInvalid color choice. Please choose R, G, B, or Y.\n\n")

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
    card = card.upper()  # INPUT NORMALIZATION - Convert to uppercase for matching

    # SPECIAL CARD ON TOP VALIDATION - SKIP, DRAWTWO, REVERSE card rules
    if current_card.endswith(("SKIP", "DRAWTWO", "REVERSE")):
        # WILD CARD EXCEPTION - Wild cards can be played on any card
        if card in ("WILD", "WILD+4"):
            return True, prompt_wild_color(card)
        # COLOR MATCH RULE - Same color cards are valid
        if card[0] == current_card[0]:
            return True, current_card
        # DRAWTWO STACKING RULE - Any DRAWTWO can stack on another DRAWTWO
        if current_card.endswith("DRAWTWO") and card.endswith("DRAWTWO"):
            return True, current_card
        # INVALID PLAY ERROR MESSAGE - Generate specific error for card type
        card_type = "SKIP" if current_card.endswith("SKIP") else "DRAWTWO" if current_card.endswith("DRAWTWO") else "REVERSE"
        rules = "a SKIP card of the same color, a card of the same color" if card_type == "SKIP" else "any DRAWTWO card, a card of the same color" if card_type == "DRAWTWO" else "a REVERSE card of the same color, a card of the same color"
        print(f"\n\nInvalid play. When a {card_type} is on top you must play {rules}, or a WILD card.\n\n")
        return False, current_card
    
    # WILD PLUS FOUR ON TOP VALIDATION - WILD+4 specific play rules
    if current_card.endswith("WILD+4"):
        if card == "WILD+4" or card == "WILD":
            return True, prompt_wild_color(card)
        if card[0] == current_card[0]:
            return True, current_card
        print("\n\nInvalid play. When a WILD+4 is on top you must play the same color or another WILD+4.\n\n")
        return False, current_card

    # REGULAR WILD ON TOP VALIDATION - WILD card (not WILD+4) play rules
    if current_card.endswith("WILD") and not current_card.endswith("WILD+4"):
        if card[0] == current_card[0] or card in ("WILD", "WILD+4"):
            return (True, prompt_wild_color(card)) if card in ("WILD", "WILD+4") else (True, current_card)
        print("\n\nInvalid play. When a WILD is on top you must play the same color or another WILD card.\n\n")
        return False, current_card

    # STANDARD COLOR OR WILD MATCH - Basic matching rules for numbered cards
    if card in ("WILD", "WILD+4") or card[0] == current_card[0]:
        return (True, prompt_wild_color(card)) if card in ("WILD", "WILD+4") else (True, current_card)

    # NUMBER MATCHING RULE - Cards with same number are valid regardless of color
    if card[1:].isdigit() and current_card[1:].isdigit() and card[1:] == current_card[1:]:
        return True, current_card

    return False, current_card

# ============================================================
# MAIN GAME LOOP - Core turn management and special card effects
# ============================================================

def game_loop(starting_player=1):
    """
    Main game loop: manages turns, handles special card effects (SKIP/DRAWTWO/WILD+4), checks win conditions.
    """
    global player1_hand, player2_hand, player3_hand, player4_hand, played_cards, current_card, skip_in_effect, drawtwo_in_effect, wild_plus_4_in_effect, drawtwo_accum, wild_plus_4_accum, reverse_order
    
    game_over = False
    
    # TURN ORDER INITIALIZATION - Set up player sequence and starting position
    player_sequence = player_order()
    
    # STARTING PLAYER INDEX - Find position of starting player in sequence
    current_index = player_sequence.index(starting_player)
    
    while not game_over:
        current_player = player_sequence[current_index]
        
        # WILD PLUS FOUR EFFECT PROCESSING - Handle pending WILD+4 draw penalty
        if wild_plus_4_in_effect:
            verify_player_turn(current_player)
            print(SCREEN_CLEAR)
            
            # WILD PLUS FOUR STACKING OPTION - Check if player can counter with their own WILD+4
            if "WILD+4" in player_hands[current_player - 1]:
                play_W4_input = turtle.textinput(f"Player {current_player}'s Turn", "You have a WILD+4. Would you like to play it now? (Y/Yes or N/No):")
                if play_W4_input is None:
                    print("No input provided. Defaulting to No.")
                    play_W4 = "no"
                else:
                    play_W4 = play_W4_input.lower()
                if play_W4 in ["y", "yes"]:
                    # WILD PLUS FOUR STACKING EXECUTION - Player chooses to stack their WILD+4
                    print(f"Your current hand is: {player_hands[current_player - 1]}")
                    card_input = turtle.textinput(f"Player {current_player}'s Turn", "What color WILD+4 card would you like to play? (R, G, B, Y):")
                    if card_input is None:
                        print("No input provided. Please try again.")
                        continue
                    card_input = card_input.upper()
                    while card_input not in ["R", "G", "B", "Y"]:
                        card_input = turtle.textinput(f"Player {current_player}'s Turn", "Invalid color choice. Please choose R, G, B, or Y:")
                        if card_input is None:
                            print("No input provided. Please try again.")
                            break
                        card_input = card_input.upper()
                    
                    # Check if card_input is valid before proceeding
                    if card_input is None or card_input not in ["R", "G", "B", "Y"]:
                        print("Invalid input. Please try again.")
                        continue
                    
                    colored_card = card_input + "WILD+4"

                    # WILD PLUS FOUR VALIDATION - Verify player has uncolored WILD+4 in hand
                    if "WILD+4" in player_hands[current_player - 1]:
                        player_hands[current_player - 1].remove("WILD+4")
                        current_card = colored_card
                        played_cards.append("WILD+4")  # DISCARD PILE UPDATE - Store uncolored version
                        wild_plus_4_in_effect = True
                        wild_plus_4_accum += 4  # ACCUMULATOR INCREMENT - Stack 4 more cards to penalty
                        print(f"You played {colored_card}!")

                        # WIN AND TRES CHECKS AFTER STACKING - Check game end conditions
                        game_over = check_win_and_tres(current_player, player_sequence)

                        # TURN ADVANCEMENT AFTER STACKING - Pass effect to next player
                        if not game_over:
                            current_index = (current_index + 1) % len(player_sequence)
                        continue
                    else:
                        print("\n\n Invalid card. Please play a WILD+4 card. Please try again.\n\n")
                        continue

                elif play_W4 in ["n", "no"]:
                    # WILD PLUS FOUR PENALTY ACCEPTANCE - Player accepts draw penalty
                    reason_msg = f"A WILD+4 was played against you!\nYou chose not to counter! You must draw {wild_plus_4_accum} cards."
                    draw_cards_and_display(current_player, wild_plus_4_accum, reason=reason_msg)
                    
                    # TRES CHECK AFTER DRAWING - Check if drawing cards triggered Tres
                    check_and_execute_tres(current_player, player_sequence)
                    
                    # WILD PLUS FOUR EFFECT RESET - Clear effect flags and accumulator
                    wild_plus_4_in_effect = False
                    wild_plus_4_accum = 0
                    current_index = advance_turn(player_sequence, current_index, clear_screen=False)
                    print("\n" *1)
                    continue
                else:
                    print("Invalid input. Please respond with Y/Yes or N/No.")
                    continue

            # WILD PLUS FOUR FORCED DRAW - Player has no WILD+4 to counter with
            reason_msg = f"A WILD+4 was played against you!\nYou don't have a WILD+4 to counter! You must draw {wild_plus_4_accum} cards."
            draw_cards_and_display(current_player, wild_plus_4_accum, reason=reason_msg)

            # TRES CHECK AFTER FORCED DRAW - Check if drawing cards triggered Tres
            check_and_execute_tres(current_player, player_sequence)

            # WILD PLUS FOUR EFFECT CLEANUP - Reset flags after penalty applied
            wild_plus_4_in_effect = False
            wild_plus_4_accum = 0
            current_index = advance_turn(player_sequence, current_index, clear_screen=False)
            continue
        
        # SKIP EFFECT PROCESSING - Handle pending SKIP card effect
        if skip_in_effect:
            print(SCREEN_CLEAR)
            skip_message = f"Player {current_player}'s turn is being SKIPPED!\n\nA SKIP card was played against you."
            show_game_message(f"Player {current_player} - Turn Skipped!", skip_message)
            # SKIP EFFECT RESET - Clear skip flag after consuming
            skip_in_effect = False
            # SKIP TURN ADVANCEMENT - Move to next player
            current_index = advance_turn(player_sequence, current_index, clear_screen=False)
            continue

        # DRAW TWO EFFECT PROCESSING - Handle pending DRAWTWO draw penalty
        if drawtwo_in_effect:
            print(SCREEN_CLEAR)
            verify_player_turn(current_player)
            
            # DRAW TWO STACKING OPTION - Check if player has any DRAWTWO to counter
            player_drawtwo_cards = [card for card in player_hands[current_player - 1] if card.endswith("DRAWTWO")]
            if player_drawtwo_cards:
                print(f"Your current hand is: {player_hands[current_player - 1]}")
                print(f"You have DRAWTWO card(s): {player_drawtwo_cards}")
                play_D2_input = turtle.textinput(f"Player {current_player}'s Turn", "Someone has played a DRAWTWO! You have a DRAWTWO card would you like to play one? (Y/Yes or N/No):")
                if play_D2_input is None:
                    print("No input provided. Defaulting to No.")
                    play_D2 = "no"
                else:
                    play_D2 = play_D2_input.lower()
                if play_D2 in ["y", "yes"]:
                    # DRAW TWO STACKING EXECUTION - Player chooses which DRAWTWO to play
                    valid_choice = False
                    while not valid_choice:
                        card_choice = turtle.textinput(f"Player {current_player}'s Turn", f"Which DRAWTWO card would you like to play? {player_drawtwo_cards}")
                        if card_choice is None:
                            print("No input provided. Please try again.")
                            continue
                        card_choice = card_choice.upper()
                        # SHORTCUT CONVERSION - Convert shortcuts like RD2 to RDRAWTWO
                        card_choice = CARD_SHORTCUTS.get(card_choice, card_choice)
                        
                        if card_choice in player_drawtwo_cards:
                            # DRAW TWO CARD REMOVAL - Remove played card from hand
                            player_hands[current_player - 1].remove(card_choice)
                            played_cards.append(card_choice)
                            current_card = card_choice
                            # DRAW TWO ACCUMULATION - Stack 2 more cards to penalty
                            drawtwo_in_effect = True
                            drawtwo_accum += 2
                            print(f"You stacked {card_choice}!")
                            valid_choice = True
                        else:
                            print(f"Invalid choice. Please choose from your DRAWTWO cards: {player_drawtwo_cards}")
                    
                    # WIN AND TRES CHECKS AFTER DRAW TWO - Check game end conditions
                    game_over = check_win_and_tres(current_player, player_sequence)
                    
                    # TURN ADVANCEMENT AFTER DRAW TWO STACK - Pass effect to next player
                    if not game_over:
                        current_index = (current_index + 1) % len(player_sequence)
                    continue
                elif play_D2 in ["n", "no"]:
                    # DRAW TWO PENALTY ACCEPTANCE - Player accepts draw penalty
                    reason_msg = f"A DRAW TWO was played against you!\nYou chose not to counter! You must draw {drawtwo_accum} cards."
                    draw_cards_and_display(current_player, drawtwo_accum, reason=reason_msg)
                    
                    # TRES CHECK AFTER DRAWING - Check if drawing cards triggered Tres
                    check_and_execute_tres(current_player, player_sequence)
                    
                    # DRAW TWO EFFECT RESET - Clear effect flags and accumulator
                    drawtwo_in_effect = False
                    drawtwo_accum = 0
                    current_index = advance_turn(player_sequence, current_index, clear_screen=False)
                    continue
                else:
                    print("\n\nInvalid input. Please respond with Y/Yes or N/No.\n\n")
                    continue

            # DRAW TWO FORCED DRAW - Player has no DRAWTWO to counter with
            reason_msg = f"A DRAW TWO was played against you!\nYou don't have a DRAW TWO to counter! You must draw {drawtwo_accum} cards."
            draw_cards_and_display(current_player, drawtwo_accum, reason=reason_msg)

            # TRES CHECK AFTER FORCED DRAW - Check if drawing cards triggered Tres
            check_and_execute_tres(current_player, player_sequence)

            # DRAW TWO EFFECT CLEANUP - Reset flags after penalty applied
            drawtwo_in_effect = False
            drawtwo_accum = 0
            current_index = advance_turn(player_sequence, current_index, clear_screen=False)
            continue

        # NORMAL TURN PROCESSING - No special effects active, handle regular turn
        game_over, player_sequence, reverse_played = handle_player_turn(current_player, player_sequence)
        
        if not game_over:
            # REVERSE EFFECT HANDLING - Recalculate player position after reverse
            if reverse_played:
                current_index = player_sequence.index(current_player)
            # TURN ADVANCEMENT - Move to next player in sequence
            current_index = (current_index + 1) % len(player_sequence)

    # PLAY AGAIN MENU - Prompt for game restart or return to main menu
    while True:        
        tres_play_again_input = turtle.textinput("Play Again?", "Would you like to play again? (yes/no):")
        if tres_play_again_input is None:
            print("No input provided. Exiting game.")
            break
        tres_play_again = tres_play_again_input.lower()

        if tres_play_again in ["yes", "y"]:
            what_game_input = turtle.textinput("Continue or Main Menu?", "1: Keep playing Tres? Enter: 'Continue'\n2: Main Menu, Enter: 'Main Menu'")
            if what_game_input is None:
                print("No input provided. Returning to main menu.")
                return
            what_game = what_game_input.lower()

            if what_game in ["continue", "1"]:
                tres_main()
                break
           
            elif what_game in ["main menu", "2"]:
                return

        elif tres_play_again in ["no", "n"]:
            quit_menu.quit_menu()
            break
        else:
            print("\n\nInvalid choice. Please try again. Enter y/yes or n/no.")

# ============================================================
# GAME INITIALIZATION - Main entry point and setup
# ============================================================

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
    global deck, played_cards, player_hands, player1_hand, player2_hand, player3_hand, player4_hand, skip_in_effect, drawtwo_in_effect, wild_plus_4_in_effect, current_card, drawtwo_accum, wild_plus_4_accum, current_player, reverse_order, t
    
    # DECK RESET - Generate fresh shuffled deck for new game
    deck = gen_deck()
    played_cards = []
    player_hands = [[], [], [], []]  # PLAYER HANDS RESET - Clear all player hands
    
    # INDIVIDUAL HAND GLOBALS RESET - Clear direct player hand references
    player1_hand = player2_hand = player3_hand = player4_hand = []
    
    # GAME STATE FLAGS RESET - Clear all special card effects
    skip_in_effect = drawtwo_in_effect = wild_plus_4_in_effect = False
    drawtwo_accum = wild_plus_4_accum = 0
    reverse_order = False
    t = True  # LOOP CONTROL RESET - Enable game loop
    
    tres_menu()
    starting_hands()
    update_player_hands()
    setup_first_card()
    
    starting_player = 1  # STARTING PLAYER DEFAULT - Player 1 begins unless first card changes it
    
    # STARTING CARD EFFECT HANDLING - Apply effects if first card is special
    if isinstance(current_card, str) and current_card.endswith("SKIP"):
        card_visuals(starting_player)
        skip_in_effect = True
    if isinstance(current_card, str) and current_card.endswith("DRAWTWO"):
        card_visuals(starting_player)
        drawtwo_in_effect = True
        drawtwo_accum = 2
    
    # WILD CARD STARTING COLOR - Player 1 chooses color if wild is first card
    if current_card in ("WILD", "WILD+4"):
        card_visuals(starting_player)
        is_wild4 = current_card == "WILD+4"
        print(f"{'WILD+4' if is_wild4 else 'Wild'} card {'drawn as first card! Player 1,' if is_wild4 else 'played!'} what color do you want to choose? (R, G, B, Y): ")
        while True:
            card_input = turtle.textinput("Wild Card Starting Color", f"Choose color for {current_card}: (R, G, B, Y)")
            if card_input is None:
                print("\n\nNo input provided. Please try again.\n\n")
                continue
            card_input = card_input.upper()
            if card_input in ["R", "G", "B", "Y"]:
                current_card = card_input + current_card
                print(f"You chose {card_input} as the new color. \n\nThe card on top is now: {current_card}")
                if is_wild4:
                    # WILD PLUS FOUR STARTING EFFECT - Apply draw 4 penalty and start at player 2
                    wild_plus_4_in_effect = True
                    wild_plus_4_accum = 4
                    starting_player = 2
                else:
                    print(f"Reminder your hand is currently: {player1_hand}\n\n")
                break
            print("\n\nInvalid color choice. Please choose R, G, B, or Y.\n\n")
    
    # REVERSE STARTING EFFECT - Reverse turn order if reverse is first card
    if current_card.endswith("REVERSE"):
        card_visuals(starting_player)
        reverse_order = True
        reverse_msg = "A REVERSE card was drawn as the first card!\n\nThe play order has been REVERSED!"
        show_game_message("REVERSE Card!", reverse_msg)
        print("REVERSE drawn as first card! Play order has been reversed!")
        print(SCREEN_CLEAR)
    
    # GAME LOOP EXECUTION - Start main game with determined starting player
    game_loop(starting_player)