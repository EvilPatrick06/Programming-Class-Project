import random

RED_CARDS = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "RSkip", "RReverse", "RDrawTwo"]

GREEN_CARDS = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "GSkip", "GReverse", "GDrawTwo"]

BLUE_CARDS = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "BSkip", "BReverse", "BDrawTwo"]

YELLOW_CARDS = ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "YSkip", "YReverse", "YDrawTwo"]

COLOR_CARDS = RED_CARDS + GREEN_CARDS + BLUE_CARDS + YELLOW_CARDS

WILD_CARDS = ["Wild", "WildDrawFour"]

ZERO_CARDS = ["R0", "G0", "B0", "Y0"]

CARDS = COLOR_CARDS + WILD_CARDS + ZERO_CARDS

t = True
color_card_limits = {}
wild_card_limits = {}
zero_card_limits = {}


def deck_limits():
    global color_card_limits, wild_card_limits, zero_card_limits
    color_card_limits = {card: 2 for card in COLOR_CARDS}
    wild_card_limits = {card: 4 for card in WILD_CARDS}
    zero_card_limits = {card: 1 for card in ZERO_CARDS}

def gen_deck():
    deck = COLOR_CARDS*2 + WILD_CARDS*4 + ZERO_CARDS
    random.shuffle(deck)
    return deck

deck = gen_deck()
    
    
def tres_main():
    tres_menu()
    deck_limits()
    starting_hands()



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
    global player_hands, bot_hands
    get_real_player_count()
    get_bot_player_count()
    
    player_hands = [
        [card for card in deck[0:7]],
        [card for card in deck[7:14]],
        [card for card in deck[14:21]],
        [card for card in deck[21:28]],
    ]
    
    bot_hands = [
        [card for card in deck[28:35]],
        [card for card in deck[35:42]],
        [card for card in deck[42:49]],
    ]
    
    if real_player_count == 1:
        print("Player 1 hand:", player_hands[0])
    elif real_player_count == 2:
        print("Player 1 hand:", player_hands[0])
        print("Player 2 hand:", player_hands[1])
    elif real_player_count == 3:
        print("Player 1 hand:", player_hands[0])
        print("Player 2 hand:", player_hands[1])
        print("Player 3 hand:", player_hands[2])
    elif real_player_count == 4:
        print("Player 1 hand:", player_hands[0])
        print("Player 2 hand:", player_hands[1])
        print("Player 3 hand:", player_hands[2])
        print("Player 4 hand:", player_hands[3])
    else:
        print("Invalid number of real players.")

    if bot_player_count == 0:
        pass
    elif bot_player_count == 1:
        bot_hands[0]
    elif bot_player_count == 2:
        bot_hands[0]
        bot_hands[1]
    elif bot_player_count == 3:
        bot_hands[0]
        bot_hands[1]
        bot_hands[2]
    else:
        print("Invalid number of bot players.")
    
def tres_menu():
    print("\n Welcome to Tres! \n Compete with other players to be the first to play all your cards. \n Match either colors or numbers. \n But beware - when someone reaches exactly three cards, the punishment mechanic could activate! \n Good luck and may the odds be in your favor! \n")

    
def get_real_player_count():
    global real_player_count, t
    while t:
            real_player_count = int(input("Enter the number of real players (1-4): "))
            if 1 <= real_player_count <= 4:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 4.")

def get_bot_player_count():
    global bot_player_count, t
    while t:
            bot_player_count = int(input("Enter the number of bot players (0-3): "))
            if 0 <= bot_player_count <= 3:
                break
            else:
                print("Invalid input. Please enter a number between 0 and 3.")
                
def get_total_players():
    global total_players
    total_players = real_player_count + bot_player_count
    print("The total number of players is: " + str(total_players))

if __name__ == "__main__":
    tres_main()
