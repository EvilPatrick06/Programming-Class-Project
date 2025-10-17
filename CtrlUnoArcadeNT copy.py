# Arcade Game Application
# Currently contains two games and 3 menus: Wordy (a word guessing game) and Tres (a card matching game), Main Menu (Where a user selects the game they wish to play or a menu), Help Menu (Here a user can find the rules and how to play a game), and Quit Menu (Here a user gets prompted to confirm that they want to quit entirely, or if they want to go to a differen  menu).
# Authors/Team: CtrlUno (Gavin Knotts, Jabriel Neal, and Joshua Casey)
# We use GitHub for version control and collaboration.

import random

#------------------------------------------------------
# WORD LISTS FOR WORDY GAME
#------------------------------------------------------

# Easy words are 4 letters long
WORDY_EASY = ["able", "acid", "aged", "also", "area", "army", "away", "baby", "back", "ball", "band", "bank", "base", "bath", "bear", "beat", "been", "beer", "bell", "belt", "best", "bike", "bill", "bird", "blow", "blue", "boat", "body", "bone", "book", "born", "both", "boys", "busy", "call", "calm", "came", "camp", "card", "care", "cars", "case", "cash", "cast", "cats", "cell", "chat", "chip", "city", "club", "coal", "coat", "code", "cold", "come", "cook", "cool", "copy", "corn", "cost", "crew", "crop", "dark", "data", "date", "days", "dead", "deal", "dear", "deep", "desk", "diet", "dirt", "dish", "does", "done", "door", "down", "draw", "drew", "drop", "drug", "dual", "duck", "dust", "duty", "each", "earn", "east", "easy", "edge", "eggs", "else", "even", "ever", "evil", "exit", "eyes", "face", "fact", "fail", "fair", "fall", "fans", "farm", "fast", "fate", "fear", "feed", "feel", "feet", "fell", "felt", "file", "fill", "film", "find", "fine", "fire", "firm", "fish", "fist", "fits", "five", "flag", "flat", "flew", "flow", "folk", "food", "foot", "ford", "fork", "form", "fort", "four", "free", "from", "fuel", "full", "fund", "gain", "game", "gate", "gave", "gear", "gets", "gift", "girl", "give", "glad", "goal", "goes", "gold", "golf", "gone", "good", "grab", "grew", "grey", "grow", "guys", "hair", "half", "hall", "hand", "hang", "hard", "hate", "have", "head", "hear", "heat", "held", "help", "here", "hide", "high", "hill", "hint", "hire", "hits", "hold", "hole", "home", "hope", "host", "hour", "huge", "hung", "hunt", "hurt", "idea", "inch", "into", "iron", "item", "jail", "jane", "jazz", "join", "joke", "jump", "june", "jury", "just", "keep", "kept", "keys", "kick", "kids", "kill", "kind", "king", "knee", "knew", "know", "lack", "lady", "laid", "lake", "land", "lane", "last", "late", "lead", "left", "legs", "less", "lets", "life", "lift", "like", "line", "link", "list", "live", "load", "loan", "lock", "long", "look", "lord", "lose", "loss", "lost", "lots", "loud", "love", "luck", "made", "mail", "main", "make", "male", "mall", "many", "mark", "mass", "math", "meal", "mean", "meat", "meet", "melt", "menu", "mess", "mice", "mile", "milk", "mind", "mine", "miss", "mode", "mood", "moon", "more", "most", "move", "much", "must", "name", "navy", "near", "neck", "need", "news", "next", "nice", "nine", "none", "noon", "nose", "note", "nuts", "okay", "once", "only", "open", "oral", "over", "pace", "pack", "page", "paid", "pain", "pair", "palm", "park", "part", "pass", "past", "path", "peak", "pick", "pics", "pile", "pink", "pipe", "plan", "play", "plot", "plus", "poem", "pole", "poll", "pool", "poor", "pope", "port", "post", "pull", "pure", "push", "puts", "race", "rain", "rank", "rate", "read", "real", "rear", "rely", "rent", "rest", "rice", "rich", "ride", "ring", "rise", "risk", "road", "rock", "role", "roll", "roof", "room", "root", "rope", "rose", "rule", "runs", "safe", "said", "sail", "sale", "salt", "same", "sand", "save", "says", "seal", "seat", "seed", "seek", "seem", "seen", "self", "sell", "send", "sent", "ship", "shoe", "shop", "shot", "show", "shut", "sick", "side", "sign", "silk", "sing", "sink", "site", "size", "skin", "skip", "slip", "slow", "snap", "snow", "soap", "soft", "soil", "sold", "sole", "some", "song", "soon", "sort", "soul", "soup", "spot", "star", "stay", "step", "stir", "stop", "such", "suit", "sure", "swim", "take", "tale", "talk", "tall", "tank", "tape", "task", "team", "tell", "tend", "tent", "term", "test", "text", "than", "that", "them", "then", "they", "thin", "this", "thus", "tide", "tied", "ties", "time", "tiny", "tips", "tire", "told", "tone", "took", "tool", "tops", "torn", "tour", "town", "toys", "tree", "trim", "trip", "true", "tune", "turn", "twin", "type", "unit", "used", "user", "uses", "vary", "vast", "very", "view", "vote", "wait", "wake", "walk", "wall", "want", "warm", "warn", "wash", "wave", "ways", "weak", "wear", "week", "well", "went", "were", "west", "what", "when", "wide", "wife", "wild", "will", "wind", "wine", "wing", "wire", "wise", "wish", "with", "wood", "wool", "word", "wore", "work", "worn", "yard", "year", "your", "zero", "zone"]

# Medium words are 5 letters long
WORDY_MEDIUM = ["about", "above", "abuse", "actor", "acute", "admit", "adopt", "adult", "after", "again", "agent", "agree", "ahead", "alarm", "album", "alert", "alien", "align", "alike", "alive", "allow", "alone", "along", "alter", "among", "anger", "angle", "angry", "apart", "apple", "apply", "arena", "argue", "arise", "array", "arrow", "aside", "asset", "avoid", "awake", "award", "aware", "badly", "baker", "bases", "basic", "beach", "began", "begin", "being", "below", "bench", "billy", "birth", "black", "blame", "blind", "block", "blood", "bloom", "blown", "blues", "blunt", "blush", "board", "boast", "bonds", "boost", "booth", "bound", "brain", "brand", "brass", "brave", "bread", "break", "breed", "brief", "bring", "broad", "broke", "brown", "brush", "build", "built", "burst", "buyer", "cable", "calif", "carry", "catch", "cause", "chain", "chair", "chaos", "charm", "chart", "chase", "cheap", "check", "chest", "chief", "child", "china", "chose", "civil", "claim", "class", "clean", "clear", "click", "climb", "clock", "close", "cloud", "clown", "clubs", "coach", "coast", "could", "count", "court", "cover", "craft", "crash", "crazy", "cream", "crime", "cross", "crowd", "crown", "crude", "curve", "cycle", "daily", "dance", "dated", "dealt", "death", "debut", "delay", "depth", "doing", "doubt", "dozen", "draft", "drama", "drank", "dream", "dress", "drill", "drink", "drive", "drove", "dying", "eager", "early", "earth", "eight", "elite", "empty", "enemy", "enjoy", "enter", "entry", "equal", "error", "event", "every", "exact", "exist", "extra", "faith", "false", "fault", "fiber", "field", "fifth", "fifty", "fight", "final", "first", "fixed", "flash", "fleet", "floor", "fluid", "focus", "force", "forth", "forty", "forum", "found", "frame", "frank", "fraud", "fresh", "front", "fruit", "fully", "funny", "giant", "given", "glass", "globe", "going", "grace", "grade", "grand", "grant", "grass", "grave", "great", "green", "gross", "group", "grown", "guard", "guess", "guest", "guide", "happy", "harry", "heart", "heavy", "hence", "henry", "horse", "hotel", "house", "human", "hurry", "image", "index", "inner", "input", "issue", "japan", "jimmy", "joint", "jones", "judge", "known", "label", "large", "laser", "later", "laugh", "layer", "learn", "lease", "least", "leave", "legal", "level", "lewis", "light", "limit", "links", "lives", "local", "loose", "lower", "lucky", "lunch", "lying", "magic", "major", "maker", "march", "maria", "match", "maybe", "mayor", "meant", "media", "metal", "might", "minor", "minus", "mixed", "model", "money", "month", "moral", "motor", "mount", "mouse", "mouth", "moved", "movie", "music", "needs", "never", "newly", "night", "noise", "north", "noted", "novel", "nurse", "occur", "ocean", "offer", "often", "order", "other", "ought", "paint", "panel", "paper", "party", "peace", "peter", "phase", "phone", "photo", "piano", "picked", "piece", "pilot", "pitch", "place", "plain", "plane", "plant", "plate", "plays", "plaza", "point", "pound", "power", "press", "price", "pride", "prime", "print", "prior", "prize", "proof", "proud", "prove", "queen", "quick", "quiet", "quite", "radio", "raise", "range", "rapid", "ratio", "reach", "ready", "realm", "rebel", "refer", "relax", "repay", "reply", "right", "rigid", "risky", "river", "robin", "roger", "roman", "rough", "round", "route", "royal", "rural", "salad", "sales", "sat", "sauce", "scale", "scare", "scene", "scope", "score", "sense", "serve", "seven", "shall", "shape", "share", "sharp", "sheet", "shelf", "shell", "shift", "shine", "shirt", "shock", "shoot", "short", "shown", "sides", "sight", "simon", "since", "sixth", "sixty", "sized", "skill", "sleep", "slide", "small", "smart", "smile", "smith", "smoke", "snake", "snow", "soapy", "social", "solar", "solid", "solve", "sorry", "sound", "south", "space", "spare", "speak", "speed", "spend", "spent", "split", "spoke", "sport", "staff", "stage", "stake", "stand", "start", "state", "stays", "steal", "steam", "steel", "steep", "steer", "stern", "stick", "still", "stock", "stone", "stood", "store", "storm", "story", "strip", "stuck", "study", "stuff", "style", "sugar", "suite", "super", "sweet", "swift", "swing", "swiss", "table", "taken", "taste", "taxes", "teach", "terms", "texas", "thank", "theft", "their", "theme", "there", "these", "thick", "thing", "think", "third", "those", "three", "threw", "throw", "thumb", "tiger", "tight", "timer", "title", "today", "topic", "total", "touch", "tough", "tower", "track", "trade", "train", "trait", "treat", "trend", "trial", "tribe", "trick", "tried", "tries", "truck", "truly", "trust", "truth", "twice", "twist", "tyler", "uncle", "under", "undue", "union", "unity", "until", "upper", "upset", "urban", "usage", "usual", "valid", "value", "video", "virus", "visit", "vital", "vocal", "voice", "waste", "watch", "water", "wave", "ways", "wealth", "weary", "weigh", "weird", "wheel", "where", "which", "while", "white", "whole", "whose", "wiped", "wired", "woman", "world", "worry", "worse", "worst", "worth", "would", "write", "wrong", "wrote", "young", "yours", "youth", "zones"]

# Hard words are 8 letters long
WORDY_HARD = ["absolute", "abstract", "academic", "accepted", "accident", "accuracy", "accurate", "achieved", "acquired", "activity", "actually", "addition", "adequate", "adjacent", "adjusted", "advanced", "advisory", "advocate", "affected", "aircraft", "although", "analysis", "annually", "answered", "anywhere", "apparent", "appeared", "approach", "approval", "approved", "argument", "arranged", "ArticleS", "assemble", "assembly", "assessed", "assigned", "assisted", "assuming", "attached", "attacked", "attempts", "attended", "attorney", "audience", "authored", "automate", "autonomy", "bathroom", "becoming", "behavior", "believed", "benefits", "birthday", "boundary", "breakfast", "bringing", "brothers", "building", "business", "calendar", "campaign", "capacity", "category", "chairman", "champion", "chapters", "chemical", "children", "choosing", "churches", "circular", "citation", "citizens", "civilian", "claiming", "cleaning", "clearing", "climbing", "clinical", "clothing", "coaching", "cocktail", "collapse", "collected", "colonial", "colorful", "combines", "commands", "commerce", "commonly", "communicate", "compared", "compiler", "complete", "composed", "compound", "computed", "computer", "concepts", "concrete", "confused", "congress", "connects", "consider", "consists", "constant", "contains", "contests", "contexts", "continue", "contract", "contrast", "controls", "convince", "creating", "creative", "criminal", "crossing", "crushing", "cultural", "customer", "database", "deadline", "deciding", "decision", "declared", "decrease", "delivery", "demands", "democrat", "depends", "describe", "designed", "designer", "detailed", "detected", "develop", "dialogue", "diamond", "differed", "digital", "directly", "director", "disabled", "disaster", "discount", "discover", "disguise", "disorder", "disposed", "distance", "distinct", "district", "dividend", "division", "document", "domestic", "dominant", "downtown", "dramatic", "drawings", "dropdown", "duration", "dynamics", "economic", "educated", "election", "electric", "eligible", "employee", "employer", "enabling", "encoding", "endorsed", "engaging", "engineer", "enhanced", "enormous", "entering", "entirely", "entitled", "envelope", "equality", "equation", "equipped", "estimate", "evaluate", "eventual", "everyone", "evidence", "exampled", "exchange", "exciting", "executed", "exercise", "existing", "expected", "expertise", "explains", "explored", "extended", "external", "facebook", "facility", "familiar", "families", "featured", "features", "feedback", "feelings", "festival", "filename", "filtered", "finished", "floating", "followed", "football", "forecast", "foreign", "formally", "formerly", "formulae", "fraction", "frequent", "friendly", "function", "funding", "gathered", "generate", "genetics", "geometry", "goldfish", "graduate", "graphics", "greatest", "handbook", "handling", "hardware", "headline", "heritage", "highway", "historic", "holidays", "hometown", "hospital", "hundreds", "husband", "identify", "identity", "illusion", "imagined", "immature", "imperial", "implicit", "imported", "improved", "incident", "includes", "increase", "indicate", "indirect", "industry", "infected", "infinite", "informed", "initiate", "injured", "innocent", "inserted", "inspired", "instance", "instinct", "intended", "interact", "interest", "internal", "internet", "interval", "intimate", "involved", "isolated", "keyboard", "knowledge", "language", "launched", "learning", "lectures", "leverage", "lifetime", "likewise", "limiting", "listened", "literacy", "literary", "location", "machines", "magnetic", "maintain", "majority", "managing", "marriage", "material", "meanings", "measured", "mechanic", "medicine", "meetings", "membrane", "memorial", "mentions", "merchant", "midnight", "military", "minimize", "ministry", "minority", "missiles", "missions", "mistakes", "modeling", "moderate", "modified", "molecule", "momentum", "monitors", "mortgage", "motivated", "mountain", "movement", "multiple", "national", "negative", "networks", "normally", "notebook", "noticein", "november", "numbered", "numerous", "observed", "obtained", "occasion", "occupied", "occurred", "offering", "official", "offshore", "operates", "operator", "opinions", "opponent", "optional", "ordinary", "organize", "oriental", "original", "outdated", "outlined", "outright", "overcome", "overhead", "overseas", "overview", "packages", "painting", "paradise", "parallel", "parental", "partners", "passport", "password", "patience", "patterns", "payments", "peaceful", "performs", "personal", "persuade", "petition", "physical", "pictures", "planning", "platform", "pleasure", "policies", "politics", "popular", "portrait", "position", "positive", "possible", "possibly", "practice", "precious", "prepared", "presence", "preserve", "pressure", "previous", "princess", "priority", "prisoner", "probably", "problems", "proceed", "products", "progress", "projects", "promises", "property", "proposal", "proposed", "prospect", "protocol", "provided", "provider", "province", "publicly", "purchase", "purposes", "pursuant", "quantity", "question", "quotient", "reaction", "readings", "realized", "reasoned", "received", "recently", "recorded", "recovery", "redirect", "reducing", "referred", "reflects", "regarded", "regional", "register", "regulate", "rejected", "relation", "relative", "released", "relevant", "reliable", "remained", "removing", "repeated", "replaced", "reported", "republic", "required", "research", "reserved", "resident", "resolved", "resource", "response", "resulted", "returned", "revealed", "reversed", "reviewed", "revision", "rewards", "sandwich", "schedule", "sciences", "security", "selected", "semester", "sequence", "services", "sessions", "settings", "shoulder", "siblings", "silently", "simulate", "situated", "slightly", "software", "solution", "somebody", "somewhat", "southern", "speaking", "specific", "specimen", "spelling", "spending", "sponsors", "standard", "standing", "stations", "sterling", "straight", "strategy", "strength", "striking", "strongly", "struggle", "students", "subjects", "subtitle", "suitable", "summoned", "supplies", "supposed", "supports", "surprise", "survived", "swimming", "symbolic", "symphony", "symptoms", "syndrome", "teachers", "teaching", "teamwork", "technics", "terminal", "textbook", "theories", "thinking", "thoughts", "thousand", "threatens", "thursday", "together", "tomorrow", "tracking", "training", "transfer", "traveled", "treasure", "triangle", "tropical", "troubled", "tumbling", "tutorial", "umbrella", "unbiased", "uncommon", "undefied", "underway", "unfunny", "universe", "unlikely", "unnotice", "unsigned", "username", "vacation", "validate", "variable", "vehicles", "verified", "versions", "vertical", "vicinity", "violence", "virginia", "visiting", "warranty", "watching", "weakness", "whatever", "wildlife", "withdraw", "wondered", "workflow", "workload", "workshop", "wrapping", "yourself"]

#------------------------------------------------------
# GLOBAL VARIABLES - WORDY GAME
#------------------------------------------------------

hint = []                # List to store hint display for player
cor_word = []            # List containing the letters of the correct word
score = 0                # Player's score for current guess
t = True                 # Control flag for loops
cor_let_wrong_spot = []  # List of correctly guessed letters in wrong positions
attempts = 0             # Number of attempts player has made
guess = []               # Player's current guess
words = []               # Selected word list based on difficulty
word_length = 5          # Length of words in the current difficulty level

#------------------------------------------------------
# GLOBAL VARIABLES - TRES GAME
#------------------------------------------------------

# Card definitions by color and number
RED_CARDS = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]
GREEN_CARDS = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]
BLUE_CARDS = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
YELLOW_CARDS = ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9"]
COLOR_CARDS = RED_CARDS + GREEN_CARDS + BLUE_CARDS + YELLOW_CARDS  # All color cards combined
ZERO_CARDS = ["R0", "G0", "B0", "Y0"]  # Zero cards for each color
WILD_CARDS = ["W"]  # Wild card 
CARDS = COLOR_CARDS + ZERO_CARDS + WILD_CARDS        # Complete deck

# Game state tracking variables
color_card_limits = {}   # Tracks availability of color cards
zero_card_limits = {}    # Tracks availability of zero cards
wild_card_limit = {}      # Tracks availability of wild card
#------------------------------------------------------
# WORDY GAME FUNCTIONS
#------------------------------------------------------

def gen_word():
    """
    Randomly selects a word from the current difficulty word list.
    Sets the correct word (cor_word) as a list of letters.
    """
    global cor_word
    cor_word = random.choice(words)
    cor_word = list(cor_word)
    
def check():
    """
    Checks the player's guess against the correct word.
    Updates score, hint display, and tracks letters in wrong positions.
    
    Returns:
        str: Game status - "win", "lose", or "continue"
    """
    global cor_word, hint, score, attempts, word_length
    cor_let_wrong_spot = []
    
    # Count letters in the correct word
    word_letter_count = {}
    for letter in cor_word:
        word_letter_count[letter] = word_letter_count.get(letter, 0) + 1
    
    # Create a copy to track remaining available letters
    available_letters = word_letter_count.copy()
    
    # First pass: Mark correct positions and reduce available count
    for i in range(word_length):
        if guess[i] == cor_word[i]:
            score += 1
            hint[i] = guess[i].upper()
            available_letters[guess[i]] -= 1
    
    # Second pass: Check for wrong positions using remaining available letters
    for i in range(word_length):
        if guess[i] != cor_word[i]:  # Not in correct position
            letter = guess[i]
            # Check if this letter exists in the word and we have remaining instances
            if letter in available_letters and available_letters[letter] > 0:
                cor_let_wrong_spot.append(letter)
                available_letters[letter] -= 1
    
    attempts += 1     

    # Check for win condition
    if score == word_length:
        print()
        print("***************")
        print("YOU WIN!!!")
        print("***************")
        return "win"
    
    # Provide feedback about correct letters in wrong positions
    elif len(cor_let_wrong_spot) > 0:
        print(f"\nYou have ", " | ".join(cor_let_wrong_spot).upper(), " in the wrong spot!")
    
    # No correct letters
    elif score == 0:
        print()
        print("No letters match.")

    # Check for lose condition (max attempts reached)
    if attempts >= 6:
        print()
        print("***************")
        print("YOU LOSE!!!")
        print("***************")
        print()
        print("The word was:", "".join(cor_word))
        return "lose"
    
    return "continue"

def get_guess():    
    """
    Prompts the player for a guess and validates the input.
    
    Returns:
        list: The player's validated guess as a list of characters
    """
    while True:
        guess = input(f"Enter a {word_length} letter word:\n\n").lower()
        if len(guess) > word_length:
            print("\n Invalid input try again \n (Too many letters)")
            print()
            continue
        elif len(guess) < word_length:
            print("\n Invalid input try again \n (Too few letters)")
            print()
            continue
        elif not guess.isalpha():
            print("\n Invalid input try again \n (Non-alphabetic characters detected)")
            print()
            continue
        break

    return list(guess)

def give_hint():
    """
    Placeholder for future hint functionality.
    """
    pass

def wordy_main():
    """
    Main game loop for the Wordy game.
    Initializes game state, processes player guesses, and handles end-game logic.
    """
    global hint, cor_word, score, t, cor_let_wrong_spot, attempts, words, word_length, guess
    
    attempts = 0
    gen_word()
    word_length = len(cor_word)
    hint = ["_"] * len(cor_word)
    
    while attempts <= 6:
        cor_let_wrong_spot = []
        score = 0
        print()
        print(" | ".join(hint).upper())
        print()
        guess = get_guess()
        result = check()
        
        if result == "win" or result == "lose":
            break
    
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again in ['y', 'yes']:
        wordy_menu()
    else:
        main_menu()

def wordy_menu():
    """
    Displays the Wordy game menu and handles difficulty selection.
    Sets up the appropriate word list based on user's choice.
    """
    global words, word_length
    
    print(" \n Welcome to Wordy! You have 6 tries to guess the correct word.\n After each guess, you'll receive feedback on how many letters are in the right position, as well as which letters are correct but in the wrong position. Good luck!")
    
    while True:
        difficulty = input("\n Choose your difficulty: \n\n1: Easy (4 letters)\n2: Medium (5 letters)\n3: Hard (8 letters)\n4: Want to play a different game?, Enter: \"Main Menu\"\n5: Need help?: type \"Help\"\n6: Want to quit?, Enter: \"Quit\"\n\n").lower()

        if difficulty in ["easy", "1"]:
            words = WORDY_EASY
            word_length = 4
            wordy_main()
            return
        elif difficulty in ["medium", "2"]:
            words = WORDY_MEDIUM
            word_length = 5
            wordy_main()
            return
        elif difficulty in ["hard", "3"]:
            words = WORDY_HARD
            word_length = 8
            wordy_main()
            return
        elif difficulty in ["main menu", "4"]:
            main_menu()
            return
        elif difficulty in ["help", "5"]:
            help_menu()
            return
        elif difficulty in ["quit", "6"]:
            quit_menu()
            return
        else:
            print("\n Invalid choice. Please try again.")

#------------------------------------------------------
# TRES GAME FUNCTIONS
#------------------------------------------------------

def deck_limits():
    """
    Initialize the limits for each card type in the Tres deck.
    Color cards have 2 copies each, zero cards have 1 copy each.
    """
    global color_card_limits, zero_card_limits, wild_card_limit
    color_card_limits = {card: 2 for card in COLOR_CARDS}
    zero_card_limits = {card: 1 for card in ZERO_CARDS}
    wild_card_limit = {card: 4 for card in WILD_CARDS}

def gen_deck():
    """
    Generates and shuffles a complete Tres deck.
    
    Returns:
        list: A shuffled deck of Tres cards
    """
    deck = COLOR_CARDS*2 + WILD_CARDS*4 + ZERO_CARDS
    random.shuffle(deck)
    return deck

# Initialize the deck
deck = gen_deck()
    
def gen_card():
    """
    Randomly selects a card from the available cards.
    Updates the card_limits to track used cards.
    """
    global card_limits, cor_card
    available = [card for card, count in card_limits.items() if count > 0]
    
    if available:
        cor_card = random.choice(available)
        card_limits[cor_card] -= 1
    else:
        print("Warning: No more cards available!")
        cor_card = None

def starting_hands():
    """
    Distributes starting hands to players based on the number of real players.
    Each player receives 7 cards from the shuffled deck.
    """
    global player_hands
    get_real_player_count()
    player_hands = [
        [card for card in deck[1:8]],
        [card for card in deck[8:15]],
        [card for card in deck[15:22]],
        [card for card in deck[22:29]],
    ]

def setup_first_card():
    """
    Sets up the first card in play from the top of the deck.
    Displays this card to all players.
    """
    global current_card
    current_card = deck[0]
    print()
    
    if real_player_count == 2:
        player_hands[0]
        player_hands[1]
        print()
        get_player1()
        get_player2()
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
               |                                                                                                                                       |
               |                                                                                                                                       |
                                                                The first card in play is: {current_card}           
                                                                The first card in play is: {current_card}           
                                                                The first card in play is: {current_card}           
                                                                The first card in play is: {current_card}           
                                                                The first card in play is: {current_card}           
                                                                The first card in play is: {current_card}           
                                                                The first card in play is: {current_card}           
               |                                                                                                                                       |
               |                                                                                                                                       |
               """)

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
    """
    Draws a card from the top of the deck.
    If deck is empty, reshuffles played cards to create a new deck.
    
    Returns:
        str: The drawn card, or None if deck is empty
    """
    global deck, played_cards, current_card
    
    if deck:
        return deck.pop(0)
    
    # The deck is empty, check if we can reshuffle played cards
    elif played_cards:
        print("The deck is empty! Reshuffling the discard pile...")
        
        # Save the current card (it's in play)
        current_in_play = current_card
        
        # Remove current card from played cards if it's there
        if current_in_play in played_cards:
            played_cards.remove(current_in_play)
            
        # Shuffle the played cards to create a new deck
        random.shuffle(played_cards)
        deck = played_cards.copy()
        played_cards = []  # Clear played cards
        
        # Add current card back to played cards
        played_cards.append(current_in_play)
        
        if deck:
            return deck.pop(0)
    
    # No cards left at all
    else: print("Error no cards left to draw. There is no way this should happen. Please play a card if you can.")
    print("Reminder your hand is ", player_hands[0])
    print("The current card in play is ", current_card)
    print()
    return None

def get_player1():
    """
    Prompts player 1 to confirm readiness.
    Loops until player confirms they are ready.
    """
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
    """
    Prompts player 2 to confirm readiness.
    Loops until player confirms they are ready.
    """
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
    """
    Prompts player 3 to confirm readiness.
    Loops until player confirms they are ready.
    """
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
    """
    Prompts player 4 to confirm readiness.
    Loops until player confirms they are ready.
    """
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
    """
    Displays the welcome message and rules for the Tres game.
    """
    print("\n Welcome to Tres! \n Compete with other players to be the first to play all your cards. \n Match either colors or numbers. \n But beware - when someone reaches exactly three cards, the punishment mechanic could activate! \n Good luck and may the odds be in your favor! \n")

def get_real_player_count():
    """
    Gets the number of real players for the Tres game.
    Validates input to ensure it's between 2 and 4 players.
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

# Initialize the list of played cards
played_cards = []

def player_1_hand():
    """
    Updates player 1's hand by filtering out played cards.
    """
    global player1_hand
    player1_hand = [card for card in player_hands[0][:] if card not in played_cards]

def player_2_hand():
    """
    Updates player 2's hand by filtering out played cards.
    """
    global player2_hand
    player2_hand = [card for card in player_hands[1][:] if card not in played_cards]

def player_3_hand():
    """
    Updates player 3's hand by filtering out played cards.
    """
    global player3_hand
    player3_hand = [card for card in player_hands[2][:] if card not in played_cards]

def player_4_hand():
    """
    Updates player 4's hand by filtering out played cards.
    """
    global player4_hand
    player4_hand = [card for card in player_hands[3][:] if card not in played_cards]

def is_valid_play(card, current_card):
    """
    Checks if a card can be played on the current card.
    Valid plays match either color (first character) or number (second character).
    
    Args:
        card (str): The card attempting to be played
        current_card (str): The current card on top of the play pile
        
    Returns:
        tuple: (is_valid, updated_card) - Boolean indicating if play is valid and the updated current card
    """
    # Convert input to uppercase for consistency
    card = card.upper()
    
    # Check if colors match (first character)
    if card[0] == current_card[0] or card == "W":
        if card == "W":
            card_input = input("Wild card played! What color do you want to choose? (R, G, B, Y): ").lower()
            wild_card_input = card_input.upper()
            if wild_card_input in ["R", "G", "B", "Y"]:
                print(f"You chose {card_input} as the new color.")
                updated_card = wild_card_input + "W"  # Create updated card with new color
                print("The card on top is now:", updated_card)
                return True, updated_card
            else:
                print("Invalid color choice. Please choose R, G, B, or Y.")
                return False, current_card
        return True, current_card
    
    # Check if numbers match (characters after the first)
    if card[1:] == current_card[1:] or current_card[1:] == "R" or current_card[1:] == "G" or current_card[1:] == "B" or current_card[1:] == "Y":
        return True, current_card
        
    return False, current_card

def game_loop():
    """
    Main game loop for Tres. Handles player turns, card plays, and win conditions.
    Continues until a player has played all their cards.
    """
    global player1_hand, player2_hand, player3_hand, player4_hand, played_cards, current_card
    
    game_over = False
    current_player = 1
    
    while not game_over:
        if current_player == 1:
            print("""
               |                                            If you are not player 1 please look away.                                                  |
               |                                            If you are not player 1 please look away.                                                  |
               |                                            If you are not player 1 please look away.                                                  |
               |                                            If you are not player 1 please look away.                                                  |
               |                                            If you are not player 1 please look away.                                                  |
               |                                            If you are not player 1 please look away.                                                  |
               |                                            If you are not player 1 please look away.                                                  |
               |                                            If you are not player 1 please look away.                                                  |
               |                                            If you are not player 1 please look away.                                                  |
               |                                            If you are not player 1 please look away.                                                  |
               """)
            print("It is Player 1's turn.")
            print("Current card on top:", current_card)
            print("Your hand is currently:", player1_hand)
            print()
            
            valid_move = False
            while not valid_move:
                card_input = input("Which card would you like to play? Or 'draw/d' to pick a card from the deck: ").lower()
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

                elif card_input in player1_hand:
                    is_valid, updated_card = is_valid_play(card_input, current_card)
                    if is_valid:
                        player1_hand.remove(card_input)
                        # If it's a wild card, use the updated card with color
                        if card_input == "W":
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

            current_player = 2
                
        elif current_player == 2:
            print("""
               |                                            If you are not player 2 please look away.                                                  |
               |                                            If you are not player 2 please look away.                                                  |
               |                                            If you are not player 2 please look away.                                                  |
               |                                            If you are not player 2 please look away.                                                  |
               |                                            If you are not player 2 please look away.                                                  |
               |                                            If you are not player 2 please look away.                                                  |
               |                                            If you are not player 2 please look away.                                                  |
               |                                            If you are not player 2 please look away.                                                  |
               |                                            If you are not player 2 please look away.                                                  |
               |                                            If you are not player 2 please look away.                                                  |
               """)
            print("It is Player 2's turn.")
            print("Current card on top:", current_card)
            print("Your hand is currently:", player2_hand)
            print()
            
            valid_move = False
            while not valid_move:
                card_input = input("Which card would you like to play? Or 'draw/d' to pick a card from the deck: ").lower()
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
                        # If it's a wild card, use the updated card with color
                        if card_input == "W":
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
                card_input = input("Which card would you like to play? Or 'draw/d' to pick a card from the deck: ").lower()
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
                        # If it's a wild card, use the updated card with color
                        if card_input == "W":
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
                card_input = input("Which card would you like to play? Or 'draw/d' to pick a card from the deck: ").lower()
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
                        # If it's a wild card, use the updated card with color
                        if card_input == "W":
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
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again in ['y', 'yes']:
        global deck
        deck = gen_deck()  # Generate a new deck
        tres_main()
    else:
        main_menu()

def tres_main():
    """
    Main entry point for the Tres game.
    Initializes the game, sets up players and hands, and starts the game loop.
    """
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

#------------------------------------------------------
# HELP MENU FUNCTIONS
#------------------------------------------------------

def help_menu():
    help_choice = input(" \n What game do you want help with:\n\n1: Wordy?\n2: Tres?\n3: Quit? \n \n").lower()

    if help_choice in ["wordy", "1"]:
        print("""\n# Welcome to Wordy!
        Wordy is a word-guessing game inspired by Wordle, but with a difficulty twists:

        # Wordy Basic Rules

            - Words are randomly selected from a predefined list and can be of any length.
            - Choose your difficulty level: Easy has 4 letters, Medium has 6 letters, and Hard has 8 letters.
            - You have a limited number of attempts to guess the word (You only get 6 of them!).
            - Be strategic with your guesses to find the secret word in as few attempts as possible.
            - Any English word is allowed, including proper nouns. 
            - No special characters.

        # Feedback System

            After each guess, you'll receive feedback:
            
                - The number of letters in the correct position.
                - The number of correct letters but in the wrong position.

        # Strategy Tips

            - Start with common letters and vowels.
            - Use the feedback to eliminate impossible letters.
            - Pay attention to letter positions to narrow down possibilities.

        Good luck guessing the secret word!""")

    elif help_choice in ["tres", "2"]:
            print("""\n# Welcome to Tres!

        Tres is a card game where players compete to be the first to play all of their cards. 
        Do this by matching either colors or numbers. 
        The game draws inspiration from Uno, but introduces a unique mechnic: 
        when a player reaches exactly three cards, a punishment round is triggered.

        # Tres Basic Rules

            - Match cards by either color or number.
            - Be the first to play all your cards to win.
            - Skip Card: Play a skip card to skip the next player's turn.
            - Wild Card: Play a wild card to change the current color to any color of your choice.
            - +2 Card: Play a +2 card to force the next player to draw two cards.
            - +4 Card: Play a +4 card to force the next player to draw four cards. 
            Also change the current color to a color of your choice.
            - Reverse Card: Play a reverse card to change the order of play.
            - You may stack +2 and +4 cards, has to be with the same type of card.
            - When you have exactly 3 cards, the punishment mechanic activates.

        # Punishment Mechanic

            When you have exactly 3 cards, you can initiate a punishment round:

                1. **Choose a Number**: Select a number between 1 and 100.
                2. **Secret Number**: The game randomly generates a secret number between 1 and 100.
                - If your number is **higher
                - If you match the **exact** secret number, the punishment effect is doubled (2x multiplier).
                3. Punishment Amount: The game randomly generates a number between 1 and 5 cards to draw as punishment.
                - If you guessed the exact secret number, this amount is doubled.
                - The punishment is applied either to you (if higher) or to all other players (if lower or exact).

           This mechanic adds suspense and strategic depth whenever a player reaches three cards. Good luck!""")

    elif help_choice in ["quit", "3"]:
        quit_menu()

    
    help_choice2 = input(" \n What do you want to do now?:\n\n1: More help?, Enter: \"Help\"\n2: Go Back to Main Menu?, Enter: \"Main Menu\"\n3: Quit? \n \n").lower()

    if help_choice2 in ["help", "1"]:
        help_menu() 
        
    elif help_choice2 in ["main menu", "2"]:
        main_menu() 

    elif help_choice2 in ["quit", "3"]:
        quit_menu()

#------------------------------------------------------
# QUIT MENU FUNCTIONS
#------------------------------------------------------

def quit_menu():
    
    quit_choice = input(" \n Are you sure you want to quit?:\n\n1: Need help?, Enter: \"Help\"\n2: Go Back to Main Menu?, Enter: \"Main Menu\"\n3: Quit? \n \n").lower()

    if quit_choice in ["help", "1"]:
        help_menu()

    elif quit_choice in ["main menu", "2"]:
        main_menu()

    elif quit_choice in ["quit", "3"]:
        print("\n Exiting the game. Goodbye! \n")
        exit()

#------------------------------------------------------
# MAIN MENU FUNCTIONS
#------------------------------------------------------

def main_menu():
    """
    Displays the main menu and handles game selection.
    Entry point for the entire application.
    """
    game = input(" \n What would do you like to play / do?:\n\n1: Wordy?\n2: Tres?\n3: Help?\n4: Quit? \n \n").lower()

    if game in ["wordy", "1"]:
        wordy_menu()
    elif game in ["tres", "2"]:
        tres_main()
    elif game in ["help", "3"]:
        help_menu()
    elif game in ["quit", "4"]:
        quit_menu()
    else:
        print("Invalid option. Please try again.")
        main_menu()
        
if __name__ == "__main__":
    main_menu()
