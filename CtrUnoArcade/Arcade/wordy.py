# CtrlUno Arcade - Wordy Game
# Word-guessing game with multiple difficulty levels and strategic feedback

# Import random library for word selection
import random

# Import quit and help menus for navigation
import quit_menu 
import help_menu

#------------------------------------------------------
# WORD LISTS - WORDY GAME
# Three difficulty levels with carefully curated word lists
#------------------------------------------------------

# Easy difficulty: 4-letter words for beginners
WORDY_EASY = ["able", "acid", "aged", "also", "area", "army", "away", "baby", "back", "ball", "band", "bank", "base", "bath", "bear", "beat", "been", "beer", "bell", "belt", "best", "bike", "bill", "bird", "blow", "blue", "boat", "body", "bone", "book", "born", "both", "boys", "busy", "call", "calm", "came", "camp", "card", "care", "cars", "case", "cash", "cast", "cats", "cell", "chat", "chip", "city", "club", "coal", "coat", "code", "cold", "come", "cook", "cool", "copy", "corn", "cost", "crew", "crop", "dark", "data", "date", "days", "dead", "deal", "dear", "deep", "desk", "diet", "dirt", "dish", "does", "done", "door", "down", "draw", "drew", "drop", "drug", "dual", "duck", "dust", "duty", "each", "earn", "east", "easy", "edge", "eggs", "else", "even", "ever", "evil", "exit", "eyes", "face", "fact", "fail", "fair", "fall", "fans", "farm", "fast", "fate", "fear", "feed", "feel", "feet", "fell", "felt", "file", "fill", "film", "find", "fine", "fire", "firm", "fish", "fist", "fits", "five", "flag", "flat", "flew", "flow", "folk", "food", "foot", "ford", "fork", "form", "fort", "four", "free", "from", "fuel", "full", "fund", "gain", "game", "gate", "gave", "gear", "gets", "gift", "girl", "give", "glad", "goal", "goes", "gold", "golf", "gone", "good", "grab", "grew", "grey", "grow", "guys", "hair", "half", "hall", "hand", "hang", "hard", "hate", "have", "head", "hear", "heat", "held", "help", "here", "hide", "high", "hill", "hint", "hire", "hits", "hold", "hole", "home", "hope", "host", "hour", "huge", "hung", "hunt", "hurt", "idea", "inch", "into", "iron", "item", "jail", "jane", "jazz", "join", "joke", "jump", "june", "jury", "just", "keep", "kept", "keys", "kick", "kids", "kill", "kind", "king", "knee", "knew", "know", "lack", "lady", "laid", "lake", "land", "lane", "last", "late", "lead", "left", "legs", "less", "lets", "life", "lift", "like", "line", "link", "list", "live", "load", "loan", "lock", "long", "look", "lord", "lose", "loss", "lost", "lots", "loud", "love", "luck", "made", "mail", "main", "make", "male", "mall", "many", "mark", "mass", "math", "meal", "mean", "meat", "meet", "melt", "menu", "mess", "mice", "mile", "milk", "mind", "mine", "miss", "mode", "mood", "moon", "more", "most", "move", "much", "must", "name", "navy", "near", "neck", "need", "news", "next", "nice", "nine", "none", "noon", "nose", "note", "nuts", "okay", "once", "only", "open", "oral", "over", "pace", "pack", "page", "paid", "pain", "pair", "palm", "park", "part", "pass", "past", "path", "peak", "pick", "pics", "pile", "pink", "pipe", "plan", "play", "plot", "plus", "poem", "pole", "poll", "pool", "poor", "pope", "port", "post", "pull", "pure", "push", "puts", "race", "rain", "rank", "rate", "read", "real", "rear", "rely", "rent", "rest", "rice", "rich", "ride", "ring", "rise", "risk", "road", "rock", "role", "roll", "roof", "room", "root", "rope", "rose", "rule", "runs", "safe", "said", "sail", "sale", "salt", "same", "sand", "save", "says", "seal", "seat", "seed", "seek", "seem", "seen", "self", "sell", "send", "sent", "ship", "shoe", "shop", "shot", "show", "shut", "sick", "side", "sign", "silk", "sing", "sink", "site", "size", "skin", "skip", "slip", "slow", "snap", "snow", "soap", "soft", "soil", "sold", "sole", "some", "song", "soon", "sort", "soul", "soup", "spot", "star", "stay", "step", "stir", "stop", "such", "suit", "sure", "swim", "take", "tale", "talk", "tall", "tank", "tape", "task", "team", "tell", "tend", "tent", "term", "test", "text", "than", "that", "them", "then", "they", "thin", "this", "thus", "tide", "tied", "ties", "time", "tiny", "tips", "tire", "told", "tone", "took", "tool", "tops", "torn", "tour", "town", "toys", "tree", "trim", "trip", "true", "tune", "turn", "twin", "type", "unit", "used", "user", "uses", "vary", "vast", "very", "view", "vote", "wait", "wake", "walk", "wall", "want", "warm", "warn", "wash", "wave", "ways", "weak", "wear", "week", "well", "went", "were", "west", "what", "when", "wide", "wife", "wild", "will", "wind", "wine", "wing", "wire", "wise", "wish", "with", "wood", "wool", "word", "wore", "work", "worn", "yard", "year", "your", "zero", "zone"]

# Medium difficulty: 5-letter words for intermediate players
WORDY_MEDIUM = ["about", "above", "abuse", "actor", "acute", "admit", "adopt", "adult", "after", "again", "agent", "agree", "ahead", "alarm", "album", "alert", "alien", "align", "alike", "alive", "allow", "alone", "along", "alter", "among", "anger", "angle", "angry", "apart", "apple", "apply", "arena", "argue", "arise", "array", "arrow", "aside", "asset", "avoid", "awake", "award", "aware", "badly", "baker", "bases", "basic", "beach", "began", "begin", "being", "below", "bench", "billy", "birth", "black", "blame", "blind", "block", "blood", "bloom", "blown", "blues", "blunt", "blush", "board", "boast", "bonds", "boost", "booth", "bound", "brain", "brand", "brass", "brave", "bread", "break", "breed", "brief", "bring", "broad", "broke", "brown", "brush", "build", "built", "burst", "buyer", "cable", "calif", "carry", "catch", "cause", "chain", "chair", "chaos", "charm", "chart", "chase", "cheap", "check", "chest", "chief", "child", "china", "chose", "civil", "claim", "class", "clean", "clear", "click", "climb", "clock", "close", "cloud", "clown", "clubs", "coach", "coast", "could", "count", "court", "cover", "craft", "crash", "crazy", "cream", "crime", "cross", "crowd", "crown", "crude", "curve", "cycle", "daily", "dance", "dated", "dealt", "death", "debut", "delay", "depth", "doing", "doubt", "dozen", "draft", "drama", "drank", "dream", "dress", "drill", "drink", "drive", "drove", "dying", "eager", "early", "earth", "eight", "elite", "empty", "enemy", "enjoy", "enter", "entry", "equal", "error", "event", "every", "exact", "exist", "extra", "faith", "false", "fault", "fiber", "field", "fifth", "fifty", "fight", "final", "first", "fixed", "flash", "fleet", "floor", "fluid", "focus", "force", "forth", "forty", "forum", "found", "frame", "frank", "fraud", "fresh", "front", "fruit", "fully", "funny", "giant", "given", "glass", "globe", "going", "grace", "grade", "grand", "grant", "grass", "grave", "great", "green", "gross", "group", "grown", "guard", "guess", "guest", "guide", "happy", "harry", "heart", "heavy", "hence", "henry", "horse", "hotel", "house", "human", "hurry", "image", "index", "inner", "input", "issue", "japan", "jimmy", "joint", "jones", "judge", "known", "label", "large", "laser", "later", "laugh", "layer", "learn", "lease", "least", "leave", "legal", "level", "lewis", "light", "limit", "links", "lives", "local", "loose", "lower", "lucky", "lunch", "lying", "magic", "major", "maker", "march", "maria", "match", "maybe", "mayor", "meant", "media", "metal", "might", "minor", "minus", "mixed", "model", "money", "month", "moral", "motor", "mount", "mouse", "mouth", "moved", "movie", "music", "needs", "never", "newly", "night", "noise", "north", "noted", "novel", "nurse", "occur", "ocean", "offer", "often", "order", "other", "ought", "paint", "panel", "paper", "party", "peace", "peter", "phase", "phone", "photo", "piano", "picked", "piece", "pilot", "pitch", "place", "plain", "plane", "plant", "plate", "plays", "plaza", "point", "pound", "power", "press", "price", "pride", "prime", "print", "prior", "prize", "proof", "proud", "prove", "queen", "quick", "quiet", "quite", "radio", "raise", "range", "rapid", "ratio", "reach", "ready", "realm", "rebel", "refer", "relax", "repay", "reply", "right", "rigid", "risky", "river", "robin", "roger", "roman", "rough", "round", "route", "royal", "rural", "salad", "sales", "sat", "sauce", "scale", "scare", "scene", "scope", "score", "sense", "serve", "seven", "shall", "shape", "share", "sharp", "sheet", "shelf", "shell", "shift", "shine", "shirt", "shock", "shoot", "short", "shown", "sides", "sight", "simon", "since", "sixth", "sixty", "sized", "skill", "sleep", "slide", "small", "smart", "smile", "smith", "smoke", "snake", "snow", "soapy", "social", "solar", "solid", "solve", "sorry", "sound", "south", "space", "spare", "speak", "speed", "spend", "spent", "split", "spoke", "sport", "staff", "stage", "stake", "stand", "start", "state", "stays", "steal", "steam", "steel", "steep", "steer", "stern", "stick", "still", "stock", "stone", "stood", "store", "storm", "story", "strip", "stuck", "study", "stuff", "style", "sugar", "suite", "super", "sweet", "swift", "swing", "swiss", "table", "taken", "taste", "taxes", "teach", "terms", "texas", "thank", "theft", "their", "theme", "there", "these", "thick", "thing", "think", "third", "those", "three", "threw", "throw", "thumb", "tiger", "tight", "timer", "title", "today", "topic", "total", "touch", "tough", "tower", "track", "trade", "train", "trait", "treat", "trend", "trial", "tribe", "trick", "tried", "tries", "truck", "truly", "trust", "truth", "twice", "twist", "tyler", "uncle", "under", "undue", "union", "unity", "until", "upper", "upset", "urban", "usage", "usual", "valid", "value", "video", "virus", "visit", "vital", "vocal", "voice", "waste", "watch", "water", "wave", "ways", "wealth", "weary", "weigh", "weird", "wheel", "where", "which", "while", "white", "whole", "whose", "wiped", "wired", "woman", "world", "worry", "worse", "worst", "worth", "would", "write", "wrong", "wrote", "young", "yours", "youth", "zones"]

# Hard difficulty: 8-letter words for advanced players
WORDY_HARD = ["absolute", "abstract", "academic", "accepted", "accident", "accuracy", "accurate", "achieved", "acquired", "activity", "actually", "addition", "adequate", "adjacent", "adjusted", "advanced", "advisory", "advocate", "affected", "aircraft", "although", "analysis", "annually", "answered", "anywhere", "apparent", "appeared", "approach", "approval", "approved", "argument", "arranged", "ArticleS", "assemble", "assembly", "assessed", "assigned", "assisted", "assuming", "attached", "attacked", "attempts", "attended", "attorney", "audience", "authored", "automate", "autonomy", "bathroom", "becoming", "behavior", "believed", "benefits", "birthday", "boundary", "breakfast", "bringing", "brothers", "building", "business", "calendar", "campaign", "capacity", "category", "chairman", "champion", "chapters", "chemical", "children", "choosing", "churches", "circular", "citation", "citizens", "civilian", "claiming", "cleaning", "clearing", "climbing", "clinical", "clothing", "coaching", "cocktail", "collapse", "collected", "colonial", "colorful", "combines", "commands", "commerce", "commonly", "communicate", "compared", "compiler", "complete", "composed", "compound", "computed", "computer", "concepts", "concrete", "confused", "congress", "connects", "consider", "consists", "constant", "contains", "contests", "contexts", "continue", "contract", "contrast", "controls", "convince", "creating", "creative", "criminal", "crossing", "crushing", "cultural", "customer", "database", "deadline", "deciding", "decision", "declared", "decrease", "delivery", "demands", "democrat", "depends", "describe", "designed", "designer", "detailed", "detected", "develop", "dialogue", "diamond", "differed", "digital", "directly", "director", "disabled", "disaster", "discount", "discover", "disguise", "disorder", "disposed", "distance", "distinct", "district", "dividend", "division", "document", "domestic", "dominant", "downtown", "dramatic", "drawings", "dropdown", "duration", "dynamics", "economic", "educated", "election", "electric", "eligible", "employee", "employer", "enabling", "encoding", "endorsed", "engaging", "engineer", "enhanced", "enormous", "entering", "entirely", "entitled", "envelope", "equality", "equation", "equipped", "estimate", "evaluate", "eventual", "everyone", "evidence", "exampled", "exchange", "exciting", "executed", "exercise", "existing", "expected", "expertise", "explains", "explored", "extended", "external", "facebook", "facility", "familiar", "families", "featured", "features", "feedback", "feelings", "festival", "filename", "filtered", "finished", "floating", "followed", "football", "forecast", "foreign", "formally", "formerly", "formulae", "fraction", "frequent", "friendly", "function", "funding", "gathered", "generate", "genetics", "geometry", "goldfish", "graduate", "graphics", "greatest", "handbook", "handling", "hardware", "headline", "heritage", "highway", "historic", "holidays", "hometown", "hospital", "hundreds", "husband", "identify", "identity", "illusion", "imagined", "immature", "imperial", "implicit", "imported", "improved", "incident", "includes", "increase", "indicate", "indirect", "industry", "infected", "infinite", "informed", "initiate", "injured", "innocent", "inserted", "inspired", "instance", "instinct", "intended", "interact", "interest", "internal", "internet", "interval", "intimate", "involved", "isolated", "keyboard", "knowledge", "language", "launched", "learning", "lectures", "leverage", "lifetime", "likewise", "limiting", "listened", "literacy", "literary", "location", "machines", "magnetic", "maintain", "majority", "managing", "marriage", "material", "meanings", "measured", "mechanic", "medicine", "meetings", "membrane", "memorial", "mentions", "merchant", "midnight", "military", "minimize", "ministry", "minority", "missiles", "missions", "mistakes", "modeling", "moderate", "modified", "molecule", "momentum", "monitors", "mortgage", "motivated", "mountain", "movement", "multiple", "national", "negative", "networks", "normally", "notebook", "noticein", "november", "numbered", "numerous", "observed", "obtained", "occasion", "occupied", "occurred", "offering", "official", "offshore", "operates", "operator", "opinions", "opponent", "optional", "ordinary", "organize", "oriental", "original", "outdated", "outlined", "outright", "overcome", "overhead", "overseas", "overview", "packages", "painting", "paradise", "parallel", "parental", "partners", "passport", "password", "patience", "patterns", "payments", "peaceful", "performs", "personal", "persuade", "petition", "physical", "pictures", "planning", "platform", "pleasure", "policies", "politics", "popular", "portrait", "position", "positive", "possible", "possibly", "practice", "precious", "prepared", "presence", "preserve", "pressure", "previous", "princess", "priority", "prisoner", "probably", "problems", "proceed", "products", "progress", "projects", "promises", "property", "proposal", "proposed", "prospect", "protocol", "provided", "provider", "province", "publicly", "purchase", "purposes", "pursuant", "quantity", "question", "quotient", "reaction", "readings", "realized", "reasoned", "received", "recently", "recorded", "recovery", "redirect", "reducing", "referred", "reflects", "regarded", "regional", "register", "regulate", "rejected", "relation", "relative", "released", "relevant", "reliable", "remained", "removing", "repeated", "replaced", "reported", "republic", "required", "research", "reserved", "resident", "resolved", "resource", "response", "resulted", "returned", "revealed", "reversed", "reviewed", "revision", "rewards", "sandwich", "schedule", "sciences", "security", "selected", "semester", "sequence", "services", "sessions", "settings", "shoulder", "siblings", "silently", "simulate", "situated", "slightly", "software", "solution", "somebody", "somewhat", "southern", "speaking", "specific", "specimen", "spelling", "spending", "sponsors", "standard", "standing", "stations", "sterling", "straight", "strategy", "strength", "striking", "strongly", "struggle", "students", "subjects", "subtitle", "suitable", "summoned", "supplies", "supposed", "supports", "surprise", "survived", "swimming", "symbolic", "symphony", "symptoms", "syndrome", "teachers", "teaching", "teamwork", "technics", "terminal", "textbook", "theories", "thinking", "thoughts", "thousand", "threatens", "thursday", "together", "tomorrow", "tracking", "training", "transfer", "traveled", "treasure", "triangle", "tropical", "troubled", "tumbling", "tutorial", "umbrella", "unbiased", "uncommon", "undefied", "underway", "unfunny", "universe", "unlikely", "unnotice", "unsigned", "username", "vacation", "validate", "variable", "vehicles", "verified", "versions", "vertical", "vicinity", "violence", "virginia", "visiting", "warranty", "watching", "weakness", "whatever", "wildlife", "withdraw", "wondered", "workflow", "workload", "workshop", "wrapping", "yourself"]

#------------------------------------------------------
# GLOBAL VARIABLES - WORDY GAME
# State management for word guessing gameplay
#------------------------------------------------------

hint = []                # Visual display of correctly guessed letters and positions
cor_word = []            # Target word split into individual characters
score = 0                # Current guess accuracy score (correct positions)
t = True                 # General-purpose boolean flag for loop control
cor_let_wrong_spot = []  # Letters that exist in word but are in wrong positions
attempts = 0             # Current number of guess attempts made by player
guess = []               # Player's current guess split into characters
words = []               # Active word list based on selected difficulty level
word_length = 5          # Length of words for current difficulty (4, 5, or 8)

#------------------------------------------------------
# WORDY GAME FUNCTIONS
# Word-guessing game with multiple difficulty levels and strategic feedback
#------------------------------------------------------

def gen_word():
    """
    Randomly selects a target word from the current difficulty's word list.
    Converts the selected word into a list of individual characters for processing.
    
    Global Variables Modified:
        cor_word: Set to list of characters from randomly selected word
    """
    global cor_word
    cor_word = random.choice(words)
    cor_word = list(cor_word)
    
def check():
    """
    Analyzes player's guess against the target word using advanced matching logic.
    Implements sophisticated letter counting to handle duplicate letters correctly.
    Provides detailed feedback about letter positions and existence.
    
    Algorithm:
    1. Count all letters in target word
    2. First pass: Mark exact position matches and decrement available counts
    3. Second pass: Check remaining letters for wrong-position matches
    4. Evaluate win/lose conditions based on attempts and accuracy
    
    Returns:
        str: Game state - "win" (complete match), "lose" (max attempts), or "continue"
    
    Global Variables Modified:
        score: Number of correctly positioned letters
        attempts: Incremented after each guess
        hint: Updated with correctly guessed letters
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
    Prompts player for word guess with comprehensive input validation.
    Ensures guess meets length requirements and contains only alphabetic characters.
    Provides specific error messages for different validation failures.
    
    Validation Checks:
    - Exact length matching current difficulty
    - Alphabetic characters only
    - Non-empty input
    
    Returns:
        list: Validated player guess as list of lowercase characters
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
    Placeholder function for future hint system implementation.
    Could provide clues like word category, synonym, or letter frequency.
    """
    pass

def wordy_main():
    """
    Core game loop managing complete Wordy gameplay session.
    Handles initialization, guess processing, and end-game flow.
    
    Game Flow:
    1. Initialize game state and generate target word
    2. Display current hint state and get player guess
    3. Process guess and provide feedback
    4. Check for win/lose conditions and handle appropriately
    5. Offer replay options with menu navigation
    
    Global Variables Modified:
        Multiple Wordy game state variables reset for new game
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
    
    while True:
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        
        if play_again in ['y', 'yes']:
            wordy_menu()
            break
        
        elif play_again in ['n', 'no']:
            quit_menu.quit_menu()
            break

        else:
            print()
            print("Invalid choice. Please try again. Enter y/yes or n/no.")

def wordy_menu():
    """
    Difficulty selection interface for Wordy game.
    Provides game instructions and sets up word lists based on player choice.
    
    Difficulty Levels:
    - Easy: 4-letter words for beginners
    - Medium: 5-letter words for intermediate challenge  
    - Hard: 8-letter words for advanced players
    
    Navigation Options:
    - Return to main menu, access help, or quit application
    
    Global Variables Modified:
        words: Set to appropriate difficulty word list
        word_length: Set to match selected difficulty
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
            return
        elif difficulty in ["help", "5"]:
            help_menu.help_menu()
            return
        elif difficulty in ["quit", "6"]:
            quit_menu.quit_menu()
            return
        else:
            print("\n Invalid choice. Please try again.")
            wordy_menu()
