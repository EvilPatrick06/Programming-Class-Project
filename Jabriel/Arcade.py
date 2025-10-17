import random

WORDY_EASY = ["able", "acid", "aged", "also", "area", "army", "away", "baby", "back", "ball", "band", "bank", "base", "bath", "bear", "beat", "been", "beer", "bell", "belt", "best", "bike", "bill", "bird", "blow", "blue", "boat", "body", "bone", "book", "born", "both", "boys", "busy", "call", "calm", "came", "camp", "card", "care", "cars", "case", "cash", "cast", "cats", "cell", "chat", "chip", "city", "club", "coal", "coat", "code", "cold", "come", "cook", "cool", "copy", "corn", "cost", "crew", "crop", "dark", "data", "date", "days", "dead", "deal", "dear", "deep", "desk", "diet", "dirt", "dish", "does", "done", "door", "down", "draw", "drew", "drop", "drug", "dual", "duck", "dust", "duty", "each", "earn", "east", "easy", "edge", "eggs", "else", "even", "ever", "evil", "exit", "eyes", "face", "fact", "fail", "fair", "fall", "fans", "farm", "fast", "fate", "fear", "feed", "feel", "feet", "fell", "felt", "file", "fill", "film", "find", "fine", "fire", "firm", "fish", "fist", "fits", "five", "flag", "flat", "flew", "flow", "folk", "food", "foot", "ford", "fork", "form", "fort", "four", "free", "from", "fuel", "full", "fund", "gain", "game", "gate", "gave", "gear", "gets", "gift", "girl", "give", "glad", "goal", "goes", "gold", "golf", "gone", "good", "grab", "grew", "grey", "grow", "guys", "hair", "half", "hall", "hand", "hang", "hard", "hate", "have", "head", "hear", "heat", "held", "help", "here", "hide", "high", "hill", "hint", "hire", "hits", "hold", "hole", "home", "hope", "host", "hour", "huge", "hung", "hunt", "hurt", "idea", "inch", "into", "iron", "item", "jail", "jane", "jazz", "join", "joke", "jump", "june", "jury", "just", "keep", "kept", "keys", "kick", "kids", "kill", "kind", "king", "knee", "knew", "know", "lack", "lady", "laid", "lake", "land", "lane", "last", "late", "lead", "left", "legs", "less", "lets", "life", "lift", "like", "line", "link", "list", "live", "load", "loan", "lock", "long", "look", "lord", "lose", "loss", "lost", "lots", "loud", "love", "luck", "made", "mail", "main", "make", "male", "mall", "many", "mark", "mass", "math", "meal", "mean", "meat", "meet", "melt", "menu", "mess", "mice", "mile", "milk", "mind", "mine", "miss", "mode", "mood", "moon", "more", "most", "move", "much", "must", "name", "navy", "near", "neck", "need", "news", "next", "nice", "nine", "none", "noon", "nose", "note", "nuts", "okay", "once", "only", "open", "oral", "over", "pace", "pack", "page", "paid", "pain", "pair", "palm", "park", "part", "pass", "past", "path", "peak", "pick", "pics", "pile", "pink", "pipe", "plan", "play", "plot", "plus", "poem", "pole", "poll", "pool", "poor", "pope", "port", "post", "pull", "pure", "push", "puts", "race", "rain", "rank", "rate", "read", "real", "rear", "rely", "rent", "rest", "rice", "rich", "ride", "ring", "rise", "risk", "road", "rock", "role", "roll", "roof", "room", "root", "rope", "rose", "rule", "runs", "safe", "said", "sail", "sale", "salt", "same", "sand", "save", "says", "seal", "seat", "seed", "seek", "seem", "seen", "self", "sell", "send", "sent", "ship", "shoe", "shop", "shot", "show", "shut", "sick", "side", "sign", "silk", "sing", "sink", "site", "size", "skin", "skip", "slip", "slow", "snap", "snow", "soap", "soft", "soil", "sold", "sole", "some", "song", "soon", "sort", "soul", "soup", "spot", "star", "stay", "step", "stir", "stop", "such", "suit", "sure", "swim", "take", "tale", "talk", "tall", "tank", "tape", "task", "team", "tell", "tend", "tent", "term", "test", "text", "than", "that", "them", "then", "they", "thin", "this", "thus", "tide", "tied", "ties", "time", "tiny", "tips", "tire", "told", "tone", "took", "tool", "tops", "torn", "tour", "town", "toys", "tree", "trim", "trip", "true", "tune", "turn", "twin", "type", "unit", "used", "user", "uses", "vary", "vast", "very", "view", "vote", "wait", "wake", "walk", "wall", "want", "warm", "warn", "wash", "wave", "ways", "weak", "wear", "week", "well", "went", "were", "west", "what", "when", "wide", "wife", "wild", "will", "wind", "wine", "wing", "wire", "wise", "wish", "with", "wood", "wool", "word", "wore", "work", "worn", "yard", "year", "your", "zero", "zone"]
WORDY_MEDIUM = ["about", "above", "abuse", "actor", "acute", "admit", "adopt", "adult", "after", "again", "agent", "agree", "ahead", "alarm", "album", "alert", "alien", "align", "alike", "alive", "allow", "alone", "along", "alter", "among", "anger", "angle", "angry", "apart", "apple", "apply", "arena", "argue", "arise", "array", "arrow", "aside", "asset", "avoid", "awake", "award", "aware", "badly", "baker", "bases", "basic", "beach", "began", "begin", "being", "below", "bench", "billy", "birth", "black", "blame", "blind", "block", "blood", "bloom", "blown", "blues", "blunt", "blush", "board", "boast", "bonds", "boost", "booth", "bound", "brain", "brand", "brass", "brave", "bread", "break", "breed", "brief", "bring", "broad", "broke", "brown", "brush", "build", "built", "burst", "buyer", "cable", "calif", "carry", "catch", "cause", "chain", "chair", "chaos", "charm", "chart", "chase", "cheap", "check", "chest", "chief", "child", "china", "chose", "civil", "claim", "class", "clean", "clear", "click", "climb", "clock", "close", "cloud", "clown", "clubs", "coach", "coast", "could", "count", "court", "cover", "craft", "crash", "crazy", "cream", "crime", "cross", "crowd", "crown", "crude", "curve", "cycle", "daily", "dance", "dated", "dealt", "death", "debut", "delay", "depth", "doing", "doubt", "dozen", "draft", "drama", "drank", "dream", "dress", "drill", "drink", "drive", "drove", "dying", "eager", "early", "earth", "eight", "elite", "empty", "enemy", "enjoy", "enter", "entry", "equal", "error", "event", "every", "exact", "exist", "extra", "faith", "false", "fault", "fiber", "field", "fifth", "fifty", "fight", "final", "first", "fixed", "flash", "fleet", "floor", "fluid", "focus", "force", "forth", "forty", "forum", "found", "frame", "frank", "fraud", "fresh", "front", "fruit", "fully", "funny", "giant", "given", "glass", "globe", "going", "grace", "grade", "grand", "grant", "grass", "grave", "great", "green", "gross", "group", "grown", "guard", "guess", "guest", "guide", "happy", "harry", "heart", "heavy", "hence", "henry", "horse", "hotel", "house", "human", "hurry", "image", "index", "inner", "input", "issue", "japan", "jimmy", "joint", "jones", "judge", "known", "label", "large", "laser", "later", "laugh", "layer", "learn", "lease", "least", "leave", "legal", "level", "lewis", "light", "limit", "links", "lives", "local", "loose", "lower", "lucky", "lunch", "lying", "magic", "major", "maker", "march", "maria", "match", "maybe", "mayor", "meant", "media", "metal", "might", "minor", "minus", "mixed", "model", "money", "month", "moral", "motor", "mount", "mouse", "mouth", "moved", "movie", "music", "needs", "never", "newly", "night", "noise", "north", "noted", "novel", "nurse", "occur", "ocean", "offer", "often", "order", "other", "ought", "paint", "panel", "paper", "party", "peace", "peter", "phase", "phone", "photo", "piano", "picked", "piece", "pilot", "pitch", "place", "plain", "plane", "plant", "plate", "plays", "plaza", "point", "pound", "power", "press", "price", "pride", "prime", "print", "prior", "prize", "proof", "proud", "prove", "queen", "quick", "quiet", "quite", "radio", "raise", "range", "rapid", "ratio", "reach", "ready", "realm", "rebel", "refer", "relax", "repay", "reply", "right", "rigid", "risky", "river", "robin", "roger", "roman", "rough", "round", "route", "royal", "rural", "salad", "sales", "sat", "sauce", "scale", "scare", "scene", "scope", "score", "sense", "serve", "seven", "shall", "shape", "share", "sharp", "sheet", "shelf", "shell", "shift", "shine", "shirt", "shock", "shoot", "short", "shown", "sides", "sight", "simon", "since", "sixth", "sixty", "sized", "skill", "sleep", "slide", "small", "smart", "smile", "smith", "smoke", "snake", "snow", "soapy", "social", "solar", "solid", "solve", "sorry", "sound", "south", "space", "spare", "speak", "speed", "spend", "spent", "split", "spoke", "sport", "staff", "stage", "stake", "stand", "start", "state", "stays", "steal", "steam", "steel", "steep", "steer", "stern", "stick", "still", "stock", "stone", "stood", "store", "storm", "story", "strip", "stuck", "study", "stuff", "style", "sugar", "suite", "super", "sweet", "swift", "swing", "swiss", "table", "taken", "taste", "taxes", "teach", "terms", "texas", "thank", "theft", "their", "theme", "there", "these", "thick", "thing", "think", "third", "those", "three", "threw", "throw", "thumb", "tiger", "tight", "timer", "title", "today", "topic", "total", "touch", "tough", "tower", "track", "trade", "train", "trait", "treat", "trend", "trial", "tribe", "trick", "tried", "tries", "truck", "truly", "trust", "truth", "twice", "twist", "tyler", "uncle", "under", "undue", "union", "unity", "until", "upper", "upset", "urban", "usage", "usual", "valid", "value", "video", "virus", "visit", "vital", "vocal", "voice", "waste", "watch", "water", "wave", "ways", "wealth", "weary", "weigh", "weird", "wheel", "where", "which", "while", "white", "whole", "whose", "wiped", "wired", "woman", "world", "worry", "worse", "worst", "worth", "would", "write", "wrong", "wrote", "young", "yours", "youth", "zones"]
WORDY_HARD = ["absolute", "abstract", "academic", "accepted", "accident", "accuracy", "accurate", "achieved", "acquired", "activity", "actually", "addition", "adequate", "adjacent", "adjusted", "advanced", "advisory", "advocate", "affected", "aircraft", "although", "analysis", "annually", "answered", "anywhere", "apparent", "appeared", "approach", "approval", "approved", "argument", "arranged", "ArticleS", "assemble", "assembly", "assessed", "assigned", "assisted", "assuming", "attached", "attacked", "attempts", "attended", "attorney", "audience", "authored", "automate", "autonomy", "bathroom", "becoming", "behavior", "believed", "benefits", "birthday", "boundary", "breakfast", "bringing", "brothers", "building", "business", "calendar", "campaign", "capacity", "category", "chairman", "champion", "chapters", "chemical", "children", "choosing", "churches", "circular", "citation", "citizens", "civilian", "claiming", "cleaning", "clearing", "climbing", "clinical", "clothing", "coaching", "cocktail", "collapse", "collected", "colonial", "colorful", "combines", "commands", "commerce", "commonly", "communicate", "compared", "compiler", "complete", "composed", "compound", "computed", "computer", "concepts", "concrete", "confused", "congress", "connects", "consider", "consists", "constant", "contains", "contests", "contexts", "continue", "contract", "contrast", "controls", "convince", "creating", "creative", "criminal", "crossing", "crushing", "cultural", "customer", "database", "deadline", "deciding", "decision", "declared", "decrease", "delivery", "demands", "democrat", "depends", "describe", "designed", "designer", "detailed", "detected", "develop", "dialogue", "diamond", "differed", "digital", "directly", "director", "disabled", "disaster", "discount", "discover", "disguise", "disorder", "disposed", "distance", "distinct", "district", "dividend", "division", "document", "domestic", "dominant", "downtown", "dramatic", "drawings", "dropdown", "duration", "dynamics", "economic", "educated", "election", "electric", "eligible", "employee", "employer", "enabling", "encoding", "endorsed", "engaging", "engineer", "enhanced", "enormous", "entering", "entirely", "entitled", "envelope", "equality", "equation", "equipped", "estimate", "evaluate", "eventual", "everyone", "evidence", "exampled", "exchange", "exciting", "executed", "exercise", "existing", "expected", "expertise", "explains", "explored", "extended", "external", "facebook", "facility", "familiar", "families", "featured", "features", "feedback", "feelings", "festival", "filename", "filtered", "finished", "floating", "followed", "football", "forecast", "foreign", "formally", "formerly", "formulae", "fraction", "frequent", "friendly", "function", "funding", "gathered", "generate", "genetics", "geometry", "goldfish", "graduate", "graphics", "greatest", "handbook", "handling", "hardware", "headline", "heritage", "highway", "historic", "holidays", "hometown", "hospital", "hundreds", "husband", "identify", "identity", "illusion", "imagined", "immature", "imperial", "implicit", "imported", "improved", "incident", "includes", "increase", "indicate", "indirect", "industry", "infected", "infinite", "informed", "initiate", "injured", "innocent", "inserted", "inspired", "instance", "instinct", "intended", "interact", "interest", "internal", "internet", "interval", "intimate", "involved", "isolated", "keyboard", "knowledge", "language", "launched", "learning", "lectures", "leverage", "lifetime", "likewise", "limiting", "listened", "literacy", "literary", "location", "machines", "magnetic", "maintain", "majority", "managing", "marriage", "material", "meanings", "measured", "mechanic", "medicine", "meetings", "membrane", "memorial", "mentions", "merchant", "midnight", "military", "minimize", "ministry", "minority", "missiles", "missions", "mistakes", "modeling", "moderate", "modified", "molecule", "momentum", "monitors", "mortgage", "motivated", "mountain", "movement", "multiple", "national", "negative", "networks", "normally", "notebook", "noticein", "november", "numbered", "numerous", "observed", "obtained", "occasion", "occupied", "occurred", "offering", "official", "offshore", "operates", "operator", "opinions", "opponent", "optional", "ordinary", "organize", "oriental", "original", "outdated", "outlined", "outright", "overcome", "overhead", "overseas", "overview", "packages", "painting", "paradise", "parallel", "parental", "partners", "passport", "password", "patience", "patterns", "payments", "peaceful", "performs", "personal", "persuade", "petition", "physical", "pictures", "planning", "platform", "pleasure", "policies", "politics", "popular", "portrait", "position", "positive", "possible", "possibly", "practice", "precious", "prepared", "presence", "preserve", "pressure", "previous", "princess", "priority", "prisoner", "probably", "problems", "proceed", "products", "progress", "projects", "promises", "property", "proposal", "proposed", "prospect", "protocol", "provided", "provider", "province", "publicly", "purchase", "purposes", "pursuant", "quantity", "question", "quotient", "reaction", "readings", "realized", "reasoned", "received", "recently", "recorded", "recovery", "redirect", "reducing", "referred", "reflects", "regarded", "regional", "register", "regulate", "rejected", "relation", "relative", "released", "relevant", "reliable", "remained", "removing", "repeated", "replaced", "reported", "republic", "required", "research", "reserved", "resident", "resolved", "resource", "response", "resulted", "returned", "revealed", "reversed", "reviewed", "revision", "rewards", "sandwich", "schedule", "sciences", "security", "selected", "semester", "sequence", "services", "sessions", "settings", "shoulder", "siblings", "silently", "simulate", "situated", "slightly", "software", "solution", "somebody", "somewhat", "southern", "speaking", "specific", "specimen", "spelling", "spending", "sponsors", "standard", "standing", "stations", "sterling", "straight", "strategy", "strength", "striking", "strongly", "struggle", "students", "subjects", "subtitle", "suitable", "summoned", "supplies", "supposed", "supports", "surprise", "survived", "swimming", "symbolic", "symphony", "symptoms", "syndrome", "teachers", "teaching", "teamwork", "technics", "terminal", "textbook", "theories", "thinking", "thoughts", "thousand", "threatens", "thursday", "together", "tomorrow", "tracking", "training", "transfer", "traveled", "treasure", "triangle", "tropical", "troubled", "tumbling", "tutorial", "umbrella", "unbiased", "uncommon", "undefied", "underway", "unfunny", "universe", "unlikely", "unnotice", "unsigned", "username", "vacation", "validate", "variable", "vehicles", "verified", "versions", "vertical", "vicinity", "violence", "virginia", "visiting", "warranty", "watching", "weakness", "whatever", "wildlife", "withdraw", "wondered", "workflow", "workload", "workshop", "wrapping", "yourself"]

# Global variables
hint = []
cor_word = []
score = 0
t = True
cor_let_wrong_spot = []
attempts = 0
guess = []
words = []
word_length = 5

def gen_word():
    global cor_word
    cor_word = random.choice(words)
    cor_word = list(cor_word)
    
    
def check():
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

    if score == word_length:
        print()
        print("***************")
        print("YOU WIN!!!")
        print("***************")
        return "win"
    
    elif len(cor_let_wrong_spot) > 0:
        print(f"\nYou have ", " | ".join(cor_let_wrong_spot).upper(), " in the wrong spot!")
    
    elif score == 0:
        print()
        print("No letters match.")

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
    while t:
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
    pass

def wordy_main():
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
    
    

def main_menu():
    game = input(" \n What would do you like to play / do?:\n\n1: Wordy?\n2: Tres?\n3: Hangman?\n4: Gambler Gauntlet?\n5: Help? \n6: Quit\n \n").lower()

    if game in ["wordy", "1"]:
        wordy_menu()

    elif game in ["tres", "2"]:
        print(" \n Welcome to Tres! \n This game is currently under development. \n Please check back later for updates and the full gaming experience. \n Thank you for your patience! \n")
        main_menu()

    elif game in ["hangman", "3"]:
        hangman_menu()

    elif game in ["gambler gauntlet", "4"]:
        gauntlet_menu()

    elif game in ["help", "5"]:
        help_menu()
    
    elif game in ["quit", "6"]:
        quit_menu()


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
                - If your number is **higher** than the secret number, you must punish yourself.
                - If your number is **lower** than the secret number, you can punish all other players.
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

def quit_menu():
    
    quit_choice = input(" \n Are you sure you want to quit?:\n\n1: Need help?, Enter: \"Help\"\n2: Go Back to Main Menu?, Enter: \"Main Menu\"\n3: Quit? \n \n").lower()

    if quit_choice in ["help", "1"]:
        help_menu()

    elif quit_choice in ["main menu", "2"]:
        main_menu()

    elif quit_choice in ["quit", "3"]:
        print("\n Exiting the game. Goodbye! \n")
        exit()

def wordy_menu():
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
        elif difficulty in ["help", "5"]:
            help_menu()
        elif difficulty in ["quit", "6"]:
            quit_menu()
        else:
            print("\n Invalid choice. Please try again.")

def tres():

    print(" \n Welcome to Tres! \n Compete with other players to be the first to play all your cards. \n Match either colors or numbers, but beware - when someone reaches exactly three cards, the punishment mechanic could activate! \n Good luck and may the odds be in your favor! \n")

    while True:
        player_count = input("\n Choose your difficulty: \n\n1: Easy (4 letters)\n2: Medium (5 letters)\n3: Hard (8 letters)\n4: Want to play a different game?, Enter: \"Main Menu\"\n5: Need help?: type \"Help\"\n6: Want to quit?, Enter: \"Quit\"\n\n").lower()

        if player_count in ["easy", "1"]:
            words = WORDY_EASY
            word_length = 4
            wordy_main()
            return
        elif player_count in ["medium", "2"]:
            words = WORDY_MEDIUM
            word_length = 5
            wordy_main()
            return
        elif player_count in ["hard", "3"]:
            words = WORDY_HARD
            word_length = 8
            wordy_main()
            return
        
def hangman_gen_word():
    global right_word
    words = ["avatar","matrix","sherlock","pikachu","gollum","beetlejuice","inception","jumanji","justice","ethics","truth","absurd","reason","skeptic","existence","nirvana","jaguar","volcano","tsunami","orchid","glacier","falcon","cactus","panther","quiz","lynx","fjord","zeal","knit","echo","vex","jazz","labyrinth","philosopher","conundrum","paradoxical","metamorphosis","transcendence","hallucination","revolutionary","entropy","illusion","clarity","chaos","serenity","whimsy","grit","valor","myth","legend","oracle","cipher","riddle","enigma","symbol","ritual","dream","vision","fable","tale","story","narrative","dialogue","monologue","soliloquy","tragedy","comedy","satire","irony","parody","meme","advertisement","slogan","tagline","brand","identity","persona","mask","guise","shadow","light","darkness","twilight","dawn","sunset","moonlight","starlight","galaxy","nebula","cosmos","universe","dimension","portal","threshold","liminal","abyss","void","infinity","eternity","time","space","gravity","quantum","atom","particle","wave","frequency","vibration","energy","force","motion","momentum","balance","equilibrium","duality","unity","harmony","discord","conflict","peace","war","battle","struggle","resistance","rebellion","revolution","uprising","awakening","enlightenment","wisdom","knowledge","learning","education","school","teacher","student","mentor","guide","hero","villain","antihero","champion","guardian","protector","warrior","fighter","survivor","wanderer","seeker","pilgrim","traveler","explorer","adventurer","nomad","outsider","stranger","friend","enemy","rival","partner","companion","ally","foe","monster","beast","creature","animal","bird","fish","insect","reptile","mammal","plant","tree","flower","leaf","root","seed","fruit","vegetable","grain","earth","soil","rock","stone","crystal","gem","metal","gold","silver","iron","copper","bronze","steel","glass","mirror","window","door","gate","wall","tower","castle","fortress","temple","shrine","church","mosque","synagogue","altar","sacrifice","offering","prayer","chant","song","melody","rhythm","beat","sound","noise","voice","speech","language","word","letter","text","script","code","signal","message","note","email","call","phone","radio","tv","screen","monitor","keyboard","mouse","tablet","laptop","computer","robot","android","cyborg","machine","engine","motor","gear","wheel","lever","switch","button","sensor","camera","lens","flash","lightbulb","lamp","torch","fire","flame","spark","ember","smoke","ash","dust","cloud","rain","snow","hail","storm","wind","breeze","gust","tornado","hurricane","earthquake","eruption","flood","drought","climate","weather","season","spring","summer","autumn","winter","day","night","hour","minute","second","clock","calendar","schedule","plan","goal","dream","hope","fear","joy","sadness","anger","love","hate","envy","greed","pride","lust","gluttony","sloth","virtue","vice","morality","law","rule","order","freedom","equality","power","control","authority","government","state","nation","country","city","town","village","street","road","path","trail","bridge","river","lake","ocean","sea","bay","coast","beach","island","mountain","hill","valley","canyon","desert","forest","jungle","swamp","marsh","plain","field","meadow","garden","park","zoo","farm","ranch","camp","tent","cabin","house","home","apartment","building","skyscraper","office","store","shop","market","mall","restaurant","cafe","bar","club","theater","cinema","museum","library","hospital","clinic","lab","factory","warehouse","garage","station","airport","port","dock","harbor","ship","boat","car","truck","bus","train","bike","motorcycle","scooter","subway","elevator","escalator","stairs","ladder","rope","chain","lock","key","map","compass","manual","book","novel","poem","essay","article","paper","report","journal","diary","log","record","data","info","fact","lie","rumor","gossip","secret","mystery","clue","evidence","proof","argument","debate","discussion","conversation","question","answer","solution","problem","challenge","task","mission","quest","journey","game","play","win","lose","score","level","stage","round","match","treaty","agreement","contract","deal","trade","exchange","buy","sell","give","take","share","borrow","lend","steal","rob","cheat","trick","deceive","manipulate","dominate","lead","follow","obey","resist","protest","march","strike","vote","elect","judge","sentence","punish","reward","praise","blame","forgive","apologize","regret","remember","forget","think","believe","understand","create","build","destroy","change","grow","shrink","move","stay","run","walk","jump","fly","swim","climb","crawl","dance","sing","talk","listen","watch","look","see","hear","smell","taste","touch","feel"]
    random.shuffle(words)
    right_word = random.choice(words)
    right_word = list(right_word)
    




def hangman_hint():
    global right_word, hint, guess
    hint = [" _ "] * len(right_word)
    

def hangman_check():
    global guess, hint, right_word, tries
    right_word = list(right_word)
    tries = 0
    man = ("\n\n\n   ")
    used_letters = []

    while True:
        print(" ".join(hint))
        print(man)
        print("You have used :",", ".join(used_letters))
        guess = input("please enter a letter. : ")
        if len(guess) != 1 or not guess.isalpha():
            print("\nplease enter just one letter... ")
            continue
        if guess in hint:
            print("You already guessed that letter...")
        if guess in right_word:
            for i in range(len(right_word)):
                if guess == right_word[i]:
                    hint[i] = guess
                    
        else:
                   
            print("\n____________________________________")
            print("Uh-Oh... Try again.")
            print("____________________________________")
            tries += 1
            if tries == 1:
                man = ("\n\n O \n\n")
                
            elif tries == 2:
                man = ("\n\n O \n"
                        " | \n"
                        " \n ")
            elif tries == 3:
                man = ("\n\n O \n"
                        "/| \n"
                        " \n ")

            elif tries == 4:
                man = ("\n\n O \n"
                        "/|\\\n"
                        "  \n ")
            elif tries == 5:
                man = ("\n\n O \n"
                        "/|\\\n"
                        "/  ")
            elif tries == 6:
                man = ("\n\n O \n"
                        "/|\\\n"
                        "/ \\\n\n")
                print(man, "\n       ...You lost... The word was ", "".join(right_word))
                hangman_playagain()
        if not " _ " in hint and tries <= 6:
                print("********")
                print("You win!!!!")
                print("********")
                hangman_playagain()
                



def hangman_playagain():
  while True:          
    hangman_play_again = input("would you like to play again?  (Yes/No)")
    if hangman_play_again == "yes"or "y" or "1":
        what_game = input("\n1: Keep playing hangman?, Enter: \"Continue\" \n2: Main Menu, Enter: \"Main Menu\"\n \n").lower()
        if what_game in ["Continue", "1"]:
            hangman_menu()
            break
        elif what_game in ["main menu", "2"]:
            main_menu()
            break
    elif hangman_play_again == "no" or "n" or "2":
        main_menu()
        break
    


def hangman_menu():
    print("\n\n***************************************************************************")
    print("Welcome to Hangman. Letter by letter you will need to guess the secret word. \nToo many attempts and.... Well it doesnt end well.\nGood luck!!")
    print("***************************************************************************")
    hangman_gen_word()
    hangman_hint()
    hangman_check()




play = True


def gauntlet_intro():
    print("\n\nWelcome to the Gambling Gauntlet Casino.\n")
    print("You have $1,000 and a chance to leave a millionaire.\n")
    print("Each table has its own rules and odds. Achieve the bankroll target, and you unlock the next game.\n")
    print("The farther you progress in the gauntlet, the higher the bet minimums are.")
    print("Be warned: the house doesn’t like losers. Go broke, and you're out.\n")
    input("Press 'ENTER' to begin the first table...")


def gauntlet_heads_or_tails():#1:1
    play = True
    while play == True:
        global bankroll
        toss = [1, 2]
        result = random.choice(toss)
        wager = int(input("How much would you like to bet?"))
        if wager > bankroll or wager < 0:
            print(f"Stop playing around. You only have {bankroll:,.2f}. Place your bet.")
            continue
        bet = input(" \n1: Heads\n2: Tails\n\n ")
        if bet == "1" or "heads":
            bet = 1
        if bet == "2" or "tails":
            bet = 2
        else:
            print("Thats a bad bet friend. Try again.")
            continue
        
        
        if result == bet:
            bankroll += wager
            print("You win! \n\nBankroll:", bankroll)
        else:
            bankroll = bankroll - wager
            print("You lose..\n\n\tBankroll is ", bankroll)     
        if bankroll <= 0:
            print("\n\nYa gone broke kid... take out a loan")
            gauntlet_replay()
            break
        if bankroll >= 3000:
            play = False
            



def gauntlet_color_wheel():      #2:1
    play = True
    while play == True:
        global bankroll
        colors = [1, 2, 3]
        random.shuffle(colors)
        result = random.choice(colors)
        wager = int(input("\n\nHow much do you want to bet buddy?\n\n\t$"))
        if wager > bankroll or wager < 0:
            print(f"Keep dreaming buddy... You only got ${bankroll:,.2f}")
            continue
        bet = int(input("Pick the color it will land on:\n1: Red\n2: Black\n3: Green\n\t\t_"))
        if bet > 3 or bet < 1 or not bet.is_integer():
            print("\n\nThats a losing bet friend. Give it another shot.")
        if bet == result:
            bankroll += (wager*3)
            print("***********")
            print(f"\n\nYou win! \n\nBankroll: ${bankroll:,.2f}")
            print("***********")
            if bankroll >= 15000:
                print("You have unlocked the next table my friend... Best of luck.")
                break 
            continue
        elif bet != result:
            bankroll -= wager
            print("---------------------") 
            print(f"\n\nYou lose... \n\n\t\tThe winning number was {result}\n\tBankroll:${bankroll:,.2f}\n\n") 
            print("---------------------")
            if bankroll <= 0:
                print("\n\n Ya gone broke kid... take out a loan")
                gauntlet_replay()
                break
            
            continue
                          
        
        




def gauntlet_cups():                 # 8.5:1
    play = True
    while play == True:
        global bankroll
        
        wager = float(input("How much would you like to bet? \t: "))
        if wager > bankroll or wager < 0:
            print(f"Don't go getting funny now. you have ${bankroll:,.2f} to bet. ")
            continue
        
        bet = int(input(" \n Pick a cup. (1-5)\n\n PAYS: 8.5:1\n "))
        if bet < 1 or bet > 5 or bet.is_integer() == False or bet == "":
            print("Can't let you do that friendo, try again...")
            continue
        toss = [1, 2, 3, 4, 5]
        result = random.choice(toss)
        if result == bet:
            bankroll += (wager*8.5)
            print(f"You win! \n\nBankroll: ${bankroll:,.2f}")
        else:
            bankroll -= wager
            print("_______________________")
            print(f"You lose...\n The winning cup was {result}\n\t Bankroll: {bankroll:,.2f}\n")       
        if bankroll <= 0:
            print("\n\n Ya gone broke kid... take out a loan")
            gauntlet_replay()
            break
        if bankroll >= 50000:
            play = False
           
            

def gauntlet_clock():            # 12:1
    global bankroll
    hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    while True:
        actual_time = random.choice(hours)
        wager = int(input("How much are you betting?\n\n\t$"))
        if wager > bankroll or wager < 0 or wager.is_integer() == False:
            print(f"Don't go getting funny now. you have ${bankroll:,.2f} to bet. ")
            continue
        bet = int(input("Guess which hour the clock will land on. (1-12)"))
        if bet < 1 or bet > 12 or bet.is_integer() == False:
            print("Can't let you do that friendo, try again...")
            continue
        if bet == actual_time:
            bankroll = bankroll+(wager*12)
            print(f"You win!!! {bankroll:,.2f}")
            if bankroll > 125000:
                print(f"You have unlocked the next table with ${bankroll:,.2f} to play with.\n\tGood luck!")
        else:
            bankroll = bankroll - wager
            print("\n\n__________________________________________________________________________________________________")
            print(f"You lost buddy.\nThe right hour was {actual_time}.\n\tYour remaining bankroll is ${bankroll:,.2f}.\n\n")
            if bankroll <= 0:
                print("ya gone broke kid... Take out a loan.")
                gauntlet_replay()
                break



def gauntlet_rat_race():             # 20:1  $50000
    global bankroll
    while True:
        winner = random.randint(1, 16)
        wager = int(input("How much would you like to bet? "))
        bet = int(input("Choose the number of the winning rat. (1-16)"))
        if bet > 16 or bet < 1:
            print("That is a losing bet my friend. There's only 16 rats to bet on...")
            continue
        if wager > bankroll:
            print("You ain't that rich yet...")
            continue
        if bet == winner:
            bankroll += wager*20
            print(f"You win! \n\nBankroll: ${bankroll:,.2f}\n")
        else:
            bankroll -= wager
            print(f"You lose... Bankroll: {bankroll:,.2f}\n\nThe winning rat was #",winner)
        if bankroll <= 0:
            print("\n\n Ya gone broke kid... take out a loan")
            gauntlet_replay()
            break
        if bankroll >= 250000:
            break




def gauntlet_num_guess():#50:1
    global bankroll
    

    while True:
        attempts = 0
        correct_number = random.randint(1, 50)    
        wager = int(input("How much would you llike to bet?\n\n\t$"))
        if wager < 0 or wager > bankroll or wager.is_integer == False or wager == "":
                print(f"These are very high stakes, stop messing around... You have ${bankroll:,.2f} to play with")
                continue        
        while True:
            bet = int(input("\n\nPick the secret number between 1 and 50\n\n\t"))
            if bet < 1 or bet > 50 or bet.is_integer() == False or bet == "":
                print("Too close to the end to make a mistake like that...")
                continue
            if bet > correct_number:
                print("Your guess is too high👆🏽.")
                attempts += 1
                if attempts >=3:
                    bankroll = bankroll - wager
                    print(f"Unfortunately not this time. The correct number was {correct_number}\n\n\tYour bankroll is ${bankroll:,.2f}")
                    if bankroll <= 0:
                        print("\n\n Ya gone broke kid... take out a loan")
                        gauntlet_replay()
                        break
                    break
                continue
            elif bet < correct_number:
                print("Your guess is too low👇🏽")
                attempts += 1
                if bankroll <= 0:
                    print("\n\n Ya gone broke kid... take out a loan")
                    gauntlet_replay()
                    break
                if attempts >=3:
                    bankroll = bankroll - wager
                    print(f"\n\nUnfortunately not this time🗿⚱️🚬. The correct number was {correct_number}\n\n\tYour bankroll is ${bankroll:,.2f}")
                    if bankroll <= 0:
                        print("\n\n Ya gone broke kid... take out a loan")
                        gauntlet_replay()
                        break
                    break
                continue
            
                
            elif bet == correct_number:
                bankroll += (wager*50)
                print("***********************************")
                print(f"Congratulations, you are victorious.💰\n\n\tYour bankroll is ${bankroll:,.2f}")
                print("***********************************")
                
                break

            if bankroll >= 500000:
                print("Fantasic, quite incredible what you've done. Allow my to shhow you to you final table... Best of luck")
                gauntlet_replay()
                break
                
            


def gauntlet_make_or_break():
    play = True
    while play == True:
        global bankroll
        toss = [1, 2]
        result = random.choice(toss)
        wager = bankroll
        print("You are all in on this hand. Finishing how you started... May the Gauntlet be in your favor")
        bet = input(" \n1: Heads\n2: Tails\n\n ")
        if bet == "1" or "heads":
            bet = 1
        if bet == "2" or "tails":
            bet = 2
        else:
            print("Thats a bad bet friend. Try again.")
            continue
        
        
        if result == bet:
            bankroll += wager
            print("You have completed the gauntlet!! You get to cash out all your winnings. \n\nBankroll:", bankroll)
            print(f"After taxes of course that only leaves you with ${bankroll/2}.")
            bankroll = bankroll/2
            bankroll = bankroll - 20000 - 10000, 5000, 100000
            print(f"Ohh and of course the gratuity, drink fee, parking, and a well...\n\n\nDont worry about the rest. \nThis is your profits from today. Bye.\n\nProfits: {bankroll:,.2f}")
            gauntlet_replay()
        else:
            bankroll = bankroll - wager
            print("You lose..\n\n\tBankroll is ", bankroll)     
        if bankroll <= 0:
            print("\n\nYa gone broke kid... take out a loan")
            gauntlet_replay()
            break
        if bankroll >= 3000:
            play = False







def gauntlet_menu():
    global bankroll
    while True:
        bankroll = 1000
        gauntlet_intro()
        print("_____________________________________")
        print("\n\nTABLE 1: HEADS OR TAILS\n")#Heads or tails intro
        print("The warm-up. A coin toss. 50/50.\n")
        print("Double or nothing until you hit $3,000. No frills, just guts.")
        input("No minimum bet.\n\nPress 'Enter' to begin.")
        gauntlet_heads_or_tails()
        print("\n\nTABLE 2: COLOR WHEEL\n")#color wheel iintro
        print("Three colors. One spin. Red, Black, or Green.\n")
        print("Pick right, triple your bet. Reach $5,000 and the next table opens.")
        gauntlet_color_wheel()
        print("\n\nTABLE 3: FIVE CUPS\n")#Cups intro
        print("Five cups. One hides the jackpot.\n")
        print("The odds are steep, but the payout’s sweet. Hit $15,000 to move on.")
        gauntlet_cups()
        print("\n\nTABLE 4: CLOCK GAME\n")#clock intro
        print("Twelve hours. One guess.\n")
        print("Time is money. Guess the hour, win big. Reach $25,000 to unlock the next challenge.")
        gauntlet_clock()
        print("\n\nTABLE 5: RAT RACE\n")#rat race into
        print("Sixteen rats. One winner.\n")
        print("Place your bet. If your rat wins, you’re one step closer to the big leagues. $50,000 gets you through.")
        gauntlet_rat_race()
        print("\n\nTABLE 6: SECRET NUMBER\n")#Secret number intro
        print("One number between 1 and 50. Three guesses.\n")
        print("This is where legends are made. Hit the jackpot and reach $250,000 to face the final table.")
        gauntlet_num_guess()
        print("*****************************")
        print("\n\nFINAL TABLE: MAKE OR BREAK\n")#the last bet
        print(f"One coin toss. Heads or Tails. Win, and you walk out with $500,000.\nLose, and the house takes everything.\n")
        input("Ready to flip the coin? Press ENTER to go all in...")
        gauntlet_make_or_break()
        gauntlet_replay()
        break


def gauntlet_replay():
  while True:          
    hangman_play_again = input("would you like to play again?  (Yes/No)")
    if hangman_play_again == "yes"or "y" or "1":
        what_game = input("\n1: Keep playing Gambler's Gauntlet?, Enter 1: \"Continue\" \n2: Main Menu, Enter: \"Main Menu\"\n \n").lower()
        if what_game in ["Continue", "1"]:
            gauntlet_menu()
            break
        elif what_game in ["main menu", "2"]:
            main_menu()
            break
    elif hangman_play_again == "no" or "n" or "2":
        main_menu()
        break

if __name__ == "__main__":
    main_menu()

