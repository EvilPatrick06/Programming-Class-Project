import random

RED_CARDS = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]
GREEN_CARDS = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]
BLUE_CARDS = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
YELLOW_CARDS = ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9"]
COLOR_CARDS = RED_CARDS + GREEN_CARDS + BLUE_CARDS + YELLOW_CARDS
ZERO_CARDS = ["R0", "G0", "B0", "Y0"]
CARDS = COLOR_CARDS + ZERO_CARDS

t = True
color_card_limits = {}
zero_card_limits = {}


def deck_limits():
    global color_card_limits, zero_card_limits
    color_card_limits = {card: 2 for card in COLOR_CARDS}
    zero_card_limits = {card: 1 for card in ZERO_CARDS}

def gen_deck():
    deck = COLOR_CARDS*2 + ZERO_CARDS
    random.shuffle(deck)
    return deck

deck = gen_deck()
    
def tres_main():
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


def gen_card():
    global card_limits, cor_card
    available = [card for card, count in card_limits.items() if count > 0]
    
    if available:
        cor_card = random.choice(available)
        card_limits[cor_card] -= 1
    else:
        print("Warning: No more cards available!")
        cor_card = None

def starting_hands():
    global player_hands
    get_real_player_count()
    player_hands = [
        [card for card in deck[1:8]],
        [card for card in deck[8:15]],
        [card for card in deck[15:22]],
        [card for card in deck[22:29]],
    ]

    if real_player_count == 2:
        player_hands[0]
        player_hands[1]
        print()
        get_player1()
        get_player2()
        print()
        print("All players are ready. Game is starting...")
    elif real_player_count == 3:
        player_hands[0]
        player_hands[1]
        player_hands[2]
        get_player1()
        get_player2()
        get_player3()
        print()
        print("All players are ready. Game is starting...")
    elif real_player_count == 4:
        player_hands[0]
        player_hands[1]
        player_hands[2]
        player_hands[3]
        get_player1()
        get_player2()
        get_player3()
        get_player4()
        print()
        print("All players are ready. Game is starting...")

def draw_card():
    global deck
    if deck:
        return deck.pop(0)
    else:
        print("The deck is empty! No more cards can be drawn.")
        return None

def setup_first_card():
    global current_card
    current_card = deck[0]
    print()
    print("The first card in play is:", current_card)
    print()

def get_player1():
    print()
    print("Get Player 1")
    response = input("Is player 1 ready? (y/yes, or n/no): ").lower()
    if response == "yes" or response == "y":
        print()
        print("Player 1 is ready!")
        player_hands[0]
    elif response == "no" or response == "n":
        print()
        print("Player 1 is not ready. Please get ready.")
        get_player1()
    else:
        print()
        print("Invalid input. Please enter y/yes or n/no.")
        get_player1()

def get_player2():
    print()
    print("Get Player 2")
    response = input("Is player 2 ready? (y/yes, or n/no): ").lower()
    if response == "yes" or response == "y":
        print()
        print("Player 2 is ready!")
        player_hands[1]
    elif response == "no" or response == "n":
        print()
        print("Player 2 is not ready. Please get ready.")
        get_player2()
    else:
        print()
        print("Invalid input. Please enter y/yes or n/no.")
        get_player2()

def get_player3():
    print()
    print("Get Player 3")
    response = input("Is player 3 ready? (y/yes, or n/no): ").lower()
    if response == "yes" or response == "y":
        print()
        print("Player 3 is ready!")
        player_hands[2]
    elif response == "no" or response == "n":
        print()
        print("Player 3 is not ready. Please get ready.")
        get_player3()
    else:
        print()
        print("Invalid input. Please enter y/yes or n/no.")
        get_player3()

def get_player4():
    print()
    print("Get Player 4")
    response = input("Is player 4 ready? (y/yes, or n/no): ").lower()
    if response == "yes" or response == "y":
        print()
        print("Player 4 is ready!")
        player_hands[3]
    elif response == "no" or response == "n":
        print()
        print("Player 4 is not ready. Please get ready.")
        get_player4()
    else:
        print()
        print("Invalid input. Please enter y/yes or n/no.")
        get_player4()

def tres_menu():
    print("\n Welcome to Tres! \n Compete with other players to be the first to play all your cards. \n Match either colors or numbers. \n But beware - when someone reaches exactly three cards, the punishment mechanic could activate! \n Good luck and may the odds be in your favor! \n")

    
def get_real_player_count():
    global real_player_count, t
    while t:
        try:
            real_player_count = int(input("Enter the number of players (2-4): "))
            if 2 <= real_player_count <= 4:
                break
            else:
                print()
                print("Invalid input. Please enter a number between 2 and 4.")
                print()
        except ValueError:
            print()
            print("Invalid input. Please enter a valid number between 2 and 4.")
            print()

played_cards = []

def player_1_hand():
    global player1_hand
    player1_hand = [card for card in player_hands[0][:] if card not in played_cards]

def player_2_hand():
    global player2_hand
    player2_hand = [card for card in player_hands[1][:] if card not in played_cards]

def player_3_hand():
    global player3_hand
    player3_hand = [card for card in player_hands[2][:] if card not in played_cards]

def player_4_hand():
    global player4_hand
    player4_hand = [card for card in player_hands[3][:] if card not in played_cards]

def is_valid_play(card, current_card):
    # Convert input to uppercase for consistency
    card = card.upper()
    
    # Check if colors match (first character)
    if card[0] == current_card[0]:
        return True
        
    # Check if numbers match (characters after the first)
    if card[1:] == current_card[1:]:
        return True
        
    return False

def game_loop():
    global player1_hand, player2_hand, player3_hand, player4_hand, played_cards, current_card
    
    game_over = False
    current_player = 1
    
    while not game_over:
        if current_player == 1:
            print("It is Player 1's turn.")
            print("Current card on top:", current_card)
            print("Your hand is currently:", player1_hand)
            print()
            
            valid_move = False
            while not valid_move:
                card_input = input("Which card would you like to play? Or 'draw' to pick a card from the deck: ").lower()
                card_input = card_input.upper()

                if card_input == "DRAW":
                    drawn_card = draw_card()
                    if drawn_card:
                        player1_hand.append(drawn_card)
                        print("You drew:", drawn_card)
                        print("Your new hand is:", player1_hand)
                        print("Remember, the card on top is still:", current_card)
                        print()
                    continue

                elif card_input in player1_hand and is_valid_play(card_input, current_card):
                    player1_hand.remove(card_input)
                    current_card = card_input
                    played_cards.append(card_input)
                    print("Player 1 played:", card_input)
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
                    print("Invalid move! Try again.")
                    
            current_player = 2
                
        elif current_player == 2:
            print("\nIt is Player 2's turn.")
            print("Current card on top:", current_card)
            print("Your hand is currently:", player2_hand)
            print()
            
            valid_move = False
            while not valid_move:
                card_input = input("Which card would you like to play? Or 'draw' to pick a card from the deck: ").lower()
                card_input = card_input.upper()
                
                if card_input == "DRAW":
                    drawn_card = draw_card()
                    if drawn_card:
                        player2_hand.append(drawn_card)
                        print("You drew:", drawn_card)
                        print("Your new hand is:", player2_hand)
                        print("Remember, the card on top is still:", current_card)
                        print()
                    continue

                elif card_input in player2_hand and is_valid_play(card_input, current_card):
                    player2_hand.remove(card_input)
                    current_card = card_input
                    played_cards.append(card_input)
                    print("Player 2 played:", card_input)
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
                    print("Invalid move! Try again.")
            
            if real_player_count >= 3:
                current_player = 3
            else:
                current_player = 1
                
        elif current_player == 3:
            print("\nIt is Player 3's turn.")
            print("Current card on top:", current_card)
            print("Your hand is currently:", player3_hand)
            print()
            
            valid_move = False
            while not valid_move:
                card_input = input("Which card would you like to play? Or 'draw' to pick a card from the deck: ").lower()
                card_input = card_input.upper()
                
                if card_input == "DRAW":
                    drawn_card = draw_card()
                    if drawn_card:
                        player3_hand.append(drawn_card)
                        print("You drew:", drawn_card)
                        print("Your new hand is:", player3_hand)
                        print("Remember, the card on top is still:", current_card)
                        print()
                    continue

                elif card_input in player3_hand and is_valid_play(card_input, current_card):
                    player3_hand.remove(card_input)
                    current_card = card_input
                    played_cards.append(card_input)
                    print("Player 3 played:", card_input)
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
                    print("Invalid move! Try again.")
            
            if real_player_count == 4:
                current_player = 4
            else:
                current_player = 1
                
        elif current_player == 4:
            print("\nIt is Player 4's turn.")
            print("Current card on top:", current_card)
            print("Your hand is currently:", player4_hand)
            print()
            
            valid_move = False
            while not valid_move:
                card_input = input("Which card would you like to play? Or 'draw' to pick a card from the deck: ").lower()
                card_input = card_input.upper()
                
                if card_input == "DRAW":
                    drawn_card = draw_card()
                    if drawn_card:
                        player4_hand.append(drawn_card)
                        print("You drew:", drawn_card)
                        print("Your new hand is:", player4_hand)
                        print("Remember, the card on top is still:", current_card)
                        print()
                    continue

                elif card_input in player4_hand and is_valid_play(card_input, current_card):
                    player4_hand.remove(card_input)
                    current_card = card_input
                    played_cards.append(card_input)
                    print("Player 4 played:", card_input)
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
                    print("Invalid move! Try again.")
            
            current_player = 1

if __name__ == "__main__":
    tres_main()
    
    
#### add a timing function to the beggining of game before 1st players turn to give players a warning that the game is about to start and to look away if they are not the first player.
#### Add a spacing to drawing scenario
