# CtrlUno Arcade - Multi-Game Collection
# A comprehensive arcade game application featuring four distinct games and navigation menus
# 
# Games Included:
# - Wordy: A word-guessing game with multiple difficulty levels (4, 5, or 8 letter words)
# - Tres: A card matching game inspired by Uno with unique punishment mechanics
# - Hangman: Classic word-guessing game with visual hangman display
# - Gambling Gauntlet: Progressive casino simulation with 7 tables and escalating stakes
#
# Menus:
# - Main Menu: Central hub for game and menu selection
# - Help Menu: Comprehensive rules and instructions for all games
# - Quit Menu: Confirmation system for exiting the application
#
# Authors: Team CtrlUno (Gavin Knotts, Jabriel Neal, Joshua Casey)
# Version Control: GitHub for collaboration and project management

import random

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
WILD_CARDS = ["W"]  # Wild cards that can change color (4 total in deck)
CARDS = COLOR_CARDS + ZERO_CARDS + WILD_CARDS  # Complete card type definitions

#------------------------------------------------------
# GLOBAL VARIABLES - TRES GAME
# Card game state tracking and deck management
#------------------------------------------------------

# Game state and availability tracking
color_card_limits = {}   # Tracks remaining copies of each color card (2 per card type)
zero_card_limits = {}    # Tracks remaining copies of each zero card (1 per color)
wild_card_limit = {}     # Tracks remaining wild cards (4 total)

#------------------------------------------------------
# GLOBAL VARIABLES - HANGMAN GAME
# Classic word-guessing game with visual feedback
#------------------------------------------------------

# Comprehensive word list spanning various categories and difficulties
HANGMAN_WORDS = ["avatar","matrix","sherlock","pikachu","gollum","beetlejuice","inception","jumanji","justice","ethics","truth","absurd","reason","skeptic","existence","nirvana","jaguar","volcano","tsunami","orchid","glacier","falcon","cactus","panther","quiz","lynx","fjord","zeal","knit","echo","vex","jazz","labyrinth","philosopher","conundrum","paradoxical","metamorphosis","transcendence","hallucination","revolutionary","entropy","illusion","clarity","chaos","serenity","whimsy","grit","valor","myth","legend","oracle","cipher","riddle","enigma","symbol","ritual","dream","vision","fable","tale","story","narrative","dialogue","monologue","soliloquy","tragedy","comedy","satire","irony","parody","meme","advertisement","slogan","tagline","brand","identity","persona","mask","guise","shadow","light","darkness","twilight","dawn","sunset","moonlight","starlight","galaxy","nebula","cosmos","universe","dimension","portal","threshold","liminal","abyss","void","infinity","eternity","time","space","gravity","quantum","atom","particle","wave","frequency","vibration","energy","force","motion","momentum","balance","equilibrium","duality","unity","harmony","discord","conflict","peace","war","battle","struggle","resistance","rebellion","revolution","uprising","awakening","enlightenment","wisdom","knowledge","learning","education","school","teacher","student","mentor","guide","hero","villain","antihero","champion","guardian","protector","warrior","fighter","survivor","wanderer","seeker","pilgrim","traveler","explorer","adventurer","nomad","outsider","stranger","friend","enemy","rival","partner","companion","ally","foe","monster","beast","creature","animal","bird","fish","insect","reptile","mammal","plant","tree","flower","leaf","root","seed","fruit","vegetable","grain","earth","soil","rock","stone","crystal","gem","metal","gold","silver","iron","copper","bronze","steel","glass","mirror","window","door","gate","wall","tower","castle","fortress","temple","shrine","church","mosque","synagogue","altar","sacrifice","offering","prayer","chant","song","melody","rhythm","beat","sound","noise","voice","speech","language","word","letter","text","script","code","signal","message","note","email","call","phone","radio","tv","screen","monitor","keyboard","mouse","tablet","laptop","computer","robot","android","cyborg","machine","engine","motor","gear","wheel","lever","switch","button","sensor","camera","lens","flash","lightbulb","lamp","torch","fire","flame","spark","ember","smoke","ash","dust","cloud","rain","snow","hail","storm","wind","breeze","gust","tornado","hurricane","earthquake","eruption","flood","drought","climate","weather","season","spring","summer","autumn","winter","day","night","hour","minute","second","clock","calendar","schedule","plan","goal","dream","hope","fear","joy","sadness","anger","love","hate","envy","greed","pride","lust","gluttony","sloth","virtue","vice","morality","law","rule","order","freedom","equality","power","control","authority","government","state","nation","country","city","town","village","street","road","path","trail","bridge","river","lake","ocean","sea","bay","coast","beach","island","mountain","hill","valley","canyon","desert","forest","jungle","swamp","marsh","plain","field","meadow","garden","park","zoo","farm","ranch","camp","tent","cabin","house","home","apartment","building","skyscraper","office","store","shop","market","mall","restaurant","cafe","bar","club","theater","cinema","museum","library","hospital","clinic","lab","factory","warehouse","garage","station","airport","port","dock","harbor","ship","boat","car","truck","bus","train","bike","motorcycle","scooter","subway","elevator","escalator","stairs","ladder","rope","chain","lock","key","map","compass","manual","book","novel","poem","essay","article","paper","report","journal","diary","log","record","data","info","fact","lie","rumor","gossip","secret","mystery","clue","evidence","proof","argument","debate","discussion","conversation","question","answer","solution","problem","challenge","task","mission","quest","journey","game","play","win","lose","score","level","stage","round","match","treaty","agreement","contract","deal","trade","exchange","buy","sell","give","take","share","borrow","lend","steal","rob","cheat","trick","deceive","manipulate","dominate","lead","follow","obey","resist","protest","march","strike","vote","elect","judge","sentence","punish","reward","praise","blame","forgive","apologize","regret","remember","forget","think","believe","understand","create","build","destroy","change","grow","shrink","move","stay","run","walk","jump","fly","swim","climb","crawl","dance","sing","talk","listen","watch","look","see","hear","smell","taste","touch","feel"]

#------------------------------------------------------
# GLOBAL VARIABLES - GAMBLING GAUNTLET GAME
# Progressive casino simulation with escalating stakes
#------------------------------------------------------

gauntlet_bankroll = 0    # Player's current money available for betting

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
            quit_menu()
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
# Card matching game with unique punishment mechanics and multi-player support
#------------------------------------------------------

def deck_limits():
    """
    Initializes card availability tracking for deck management.
    Sets up proper card distribution matching physical card game rules.
    
    Card Distribution:
    - Color cards (R1-R9, G1-G9, etc.): 2 copies each
    - Zero cards (R0, G0, B0, Y0): 1 copy each
    - Wild cards: 4 total copies
    
    Global Variables Modified:
        color_card_limits, zero_card_limits, wild_card_limit: Initialize availability counters
    """
    global color_card_limits, zero_card_limits, wild_card_limit
    color_card_limits = {card: 2 for card in COLOR_CARDS}
    zero_card_limits = {card: 1 for card in ZERO_CARDS}
    wild_card_limit = {card: 4 for card in WILD_CARDS}

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
    
    # Add wild cards (4 copies)
    deck.extend(WILD_CARDS * 4)
    
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
    print("\n Welcome to Tres! \n Compete with other players to be the first to play all of your cards. \n Match either colors or numbers. \n But beware - when someone reaches exactly three cards, the punishment mechanic could activate! \n Good luck and may the odds be in your favor! \n")

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
    - Wild cards (W) are always playable and change color
    - Wild cards prompt for new color selection
    
    Args:
        card (str): Card player wants to play (e.g., "R5", "W")
        current_card (str): Current card on top of play pile
        
    Returns:
        tuple: (is_valid_boolean, updated_current_card)
               For wild cards, updated_card includes chosen color
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

            wild_card = False
            while not wild_card:
                if current_card == "W":
                    card_input = input("Wild card played! What color do you want to choose? (R, G, B, Y): ").lower()
                    wild_card_input = card_input.upper()
                    if wild_card_input in ["R", "G", "B", "Y"]:
                        print(f"You chose {card_input} as the new color.")
                        updated_card = wild_card_input + "W"  # Create updated card with new color
                        print("The card on top is now:", updated_card)
                        current_card = updated_card
                        print("Reminder your hand is currently:", player1_hand)
                    elif wild_card_input not in ["R", "G", "B", "Y"]:
                        print("Invalid color choice. Please choose R, G, B, or Y.")
                        continue


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
            print("\n" * 500)
            current_player = 2
                
        elif current_player == 2:
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
    while True:        
        tres_play_again = input("Would you like to play again? (yes/no): ").lower()

        if tres_play_again in ["yes", "y"]:
            what_game = input("\n1: Keep playing Tres?, Enter: \"Continue\"\n2: Main Menu, Enter: \"Main Menu\"\n\n").lower()

            if what_game in ["continue", "1"]:
                tres_main()
                break
           
            elif what_game in ["main menu", "2"]:
                main_menu()
                break

        elif tres_play_again in ["no", "n"]:
            quit_menu()
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

#------------------------------------------------------
# HANGMAN GAME FUNCTIONS
# Classic word-guessing game with visual hangman progression
#------------------------------------------------------

def hangman_gen_word():
    """
    Selects random word from comprehensive Hangman word list.
    Converts selected word to character list for letter-by-letter processing.
    
    Word Selection:
    - Chooses from 500+ words spanning multiple categories
    - Includes various difficulties and word lengths
    - Words range from simple to complex vocabulary
    
    Global Variables Modified:
        hangman_right_word: Target word as list of characters
    """
    global hangman_right_word
    words = HANGMAN_WORDS.copy()
    random.shuffle(words)
    hangman_right_word = random.choice(words)
    hangman_right_word = list(hangman_right_word)

def hangman_hint():
    """
    Initializes visual hint display with underscores for each letter position.
    Creates the classic Hangman blank word representation.
    
    Display Format: " _ " for each letter with spaces for readability
    
    Global Variables Modified:
        hangman_hint_display: List of blanks matching word length
    """
    global hangman_right_word, hangman_hint_display
    hangman_hint_display = [" _ "] * len(hangman_right_word)

def hangman_check():
    """
    Core Hangman gameplay loop with guess processing and visual feedback.
    Manages letter guessing, hangman drawing, and win/lose detection.
    
    Game Mechanics:
    - Tracks used letters to prevent duplicates
    - Updates hint display when letters are found
    - Draws progressive hangman figure for wrong guesses
    - Enforces 6-guess limit before loss
    
    Input Validation:
    - Single alphabetic characters only
    - Prevents duplicate guesses
    - Clear error messages for invalid input
    
    Visual Progression:
    - ASCII art hangman drawn step by step
    - 6 progressive stages from head to full figure
    
    Global Variables Modified:
        hangman_hint_display: Updated with correct letter guesses
        hangman_tries: Incremented for each wrong guess
    """
    global hangman_hint_display, hangman_right_word, hangman_tries
    hangman_right_word = list(hangman_right_word)
    hangman_tries = 0
    man = ("\n\n\n   ")
    used_letters = []

    while True:
        print(" ".join(hangman_hint_display))
        print(man)
        print("You have used :", ", ".join(used_letters))
        guess = input("Please enter a letter: ").lower()
        
        if len(guess) != 1:
            print("\nPlease enter just one letter... ")
            continue
        if not guess.isalpha():
            print("\nPlease enter a letter... ")
            continue

        if guess in used_letters:
            print("You already guessed that letter...")
            continue
        
        used_letters.append(guess)
        
        if guess in hangman_right_word:
            for i in range(len(hangman_right_word)):
                if guess == hangman_right_word[i]:
                    hangman_hint_display[i] = guess
        else:
            print("\n____________________________________")
            print("Uh-Oh... Try again.")
            print("____________________________________")
            hangman_tries += 1
            
            if hangman_tries == 1:
                man = ("\n\n O \n\n")
            elif hangman_tries == 2:
                man = ("\n\n O \n"
                       " | \n"
                       " \n ")
            elif hangman_tries == 3:
                man = ("\n\n O \n"
                       "/| \n"
                       " \n ")
            elif hangman_tries == 4:
                man = ("\n\n O \n"
                       "/|\\\n"
                       "  \n ")
            elif hangman_tries == 5:
                man = ("\n\n O \n"
                       "/|\\\n"
                       "/  ")
            elif hangman_tries == 6:
                man = ("\n\n O \n"
                       "/|\\\n"
                       "/ \\\n\n")
                print(man, "\n       ...You lost... The word was ", "".join(hangman_right_word))
                print()
                hangman_playagain()
                return
        
        if " _ " not in hangman_hint_display and hangman_tries <= 6:
            print()
            print("********")
            print("You win!!!!")
            print("********")
            print()
            hangman_playagain()
            return

def hangman_playagain():
    """
    Post-game navigation for Hangman sessions.
    Offers options to replay Hangman, return to main menu, or quit application.
    
    Navigation Options:
    - Continue: Start new Hangman game
    - Main Menu: Return to game selection
    - Quit: Exit application entirely
    
    Input validation with clear error messages for invalid choices.
    """
    while True:        
        hangman_play_again = input("Would you like to play again? (yes/no): ").lower()

        if hangman_play_again in ["yes", "y"]:
            what_game = input("\n1: Keep playing Hangman?, Enter: \"Continue\"\n2: Main Menu, Enter: \"Main Menu\"\n\n").lower()
            
            if what_game in ["continue", "1"]:
                hangman_menu()
                break
           
            elif what_game in ["main menu", "2"]:
                main_menu()
                break
        
        elif hangman_play_again in ["no", "n"]:
            quit_menu()
            break
        
        else:
            print()
            print("Invalid choice. Please try again. Enter y/yes or n/no.")

def hangman_menu():
    """
    Hangman game introduction and initialization.
    Displays game rules, starts word generation, and launches gameplay.
    
    Setup Sequence:
    1. Display welcome message and rules
    2. Generate random target word
    3. Initialize hint display
    4. Start main game loop
    
    Provides clear expectations about hangman consequences and gameplay.
    """
    print("\n\n***************************************************************************")
    print("Welcome to Hangman! Guess the secret word.")
    print("Too many attempts and.... Well it doesn't end well.")
    print("Good luck!!")
    print("***************************************************************************")
    hangman_gen_word()
    hangman_hint()
    hangman_check()

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
                main_menu()
                break
        
        elif gauntlet_play_again in ["no", "n"]:
            quit_menu()
            break
        
        else:
            print()
            print("Invalid choice. Please try again. Enter y/yes or n/no.")

#------------------------------------------------------
# HELP MENU FUNCTIONS
# Comprehensive game documentation and rule explanations
#------------------------------------------------------

def help_menu():
    """
    Interactive help system providing detailed rules for all arcade games.
    Offers comprehensive documentation with strategies and gameplay mechanics.
    
    Available Help Topics:
    1. Wordy: Word guessing rules, difficulty levels, feedback system
    2. Tres: Card matching rules, punishment mechanics, multi-player strategy
    3. Hangman: Classic rules, strategy tips, visual progression
    4. Gambling Gauntlet: All 7 tables, odds, progression requirements
    
    Navigation Features:
    - Return to help for additional topics
    - Access main menu or quit from help system
    - Input validation with clear error handling
    
    Each help section includes:
    - Basic rules and objectives
    - Detailed gameplay mechanics
    - Strategic tips and advice
    - Special features and unique mechanics
    """
    help_choice = input(" \n What game do you want help with:\n\n1: Wordy?\n2: Tres?\n3: Hangman?\n4: Gambling Gauntlet?\n5: Quit? \n \n").lower()

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

    elif help_choice in ["hangman", "3"]:
        print("""\n# Welcome to Hangman!

        Hangman is a classic word-guessing game where you try to guess a secret word letter by letter.

        # Hangman Basic Rules

            - A random word is selected from a large word list.
            - You see blank spaces representing each letter of the word.
            - Guess one letter at a time.
            - Correct guesses reveal the letter(s) in their position(s).
            - Incorrect guesses add a body part to the hangman figure.
            - You have 6 incorrect guesses before losing.
            - No special characters or numbers.

        # Strategy Tips

            - Start with common vowels (A, E, I, O, U).
            - Try frequently used consonants (R, S, T, L, N).
            - Use the word length as a clue.
            - Pay attention to letter patterns.

        Good luck saving the hangman!""")

    elif help_choice in ["gambling gauntlet", "gambler's gauntlet", "gauntlet", "4"]:
        print("""\n# Welcome to the Gambling Gauntlet!

        The Gambling Gauntlet is a progressive casino game where you start with $1,000 and try to reach millionaire status.

        # Gambling Gauntlet Basic Rules

            - Start with $1,000 bankroll.
            - Progress through 6 tables plus a final all-in round.
            - Each table has different odds and a bankroll target to unlock the next table.
            - Go broke at any time and you're out.

        # The Tables

            1. **Heads or Tails** (1:1) - Reach $3,000
            2. **Color Wheel** (3:1) - Reach $15,000
            3. **Five Cups** (8.5:1) - Reach $50,000
            4. **Clock Game** (12:1) - Reach $125,000
            5. **Rat Race** (20:1) - Reach $250,000
            6. **Secret Number** (50:1) - Reach $500,000
            7. **Make or Break** (All-in) - Win big or lose everything
    
        # Strategy Tips

            - Manage your bankroll carefully.
            - Don't bet more than you can afford to lose.
            - Higher risk tables have higher payouts.
            - The final table is all or nothing.

        May the odds be ever in your favor!""")

    elif help_choice in ["quit", "5"]:
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
# Application exit confirmation and navigation safety
#------------------------------------------------------

def quit_menu():
    """
    Exit confirmation system preventing accidental application closure.
    Provides last-chance navigation to help or main menu.
    
    Safety Features:
    - Confirmation required before exiting
    - Access to help if player needs information
    - Return to main menu option
    - Clear exit message when confirmed
    
    Options:
    1. Help: Access game documentation
    2. Main Menu: Return to game selection
    3. Quit: Confirmed application exit with goodbye message
    
    Input validation ensures proper choice handling before exit.
    """
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
# Central navigation hub and application entry point
#------------------------------------------------------

def main_menu():
    """
    Primary navigation interface and application entry point.
    Provides access to all games, help system, and exit functionality.
    
    Available Options:
    1. Wordy: Word-guessing game with multiple difficulties
    2. Tres: Multi-player card matching game
    3. Hangman: Classic word-guessing with visual feedback
    4. Gambling Gauntlet: Progressive casino simulation
    5. Help: Comprehensive game documentation
    6. Quit: Confirmed application exit
    
    Features:
    - Clear option presentation with multiple input formats
    - Robust input validation and error handling
    - Seamless navigation between all application components
    - Fallback error handling for invalid selections
    
    Input Flexibility:
    - Accepts both numeric (1-6) and text-based inputs
    - Case-insensitive text matching
    - Alternative names supported (e.g., "gauntlet" for Gambling Gauntlet)
    """
    game = input(" \n What would do you like to play / do?:\n\n1: Wordy?\n2: Tres?\n3: Hangman?\n4: Gambling Gauntlet?\n5: Help?\n6: Quit? \n \n").lower()

    if game in ["wordy", "1"]:
        wordy_menu()
    elif game in ["tres", "2"]:
        tres_main()
    elif game in ["hangman", "3"]:
        hangman_menu()
    elif game in ["gambling gauntlet", "gambler's gauntlet", "gauntlet", "4"]:
        gauntlet_menu()
    elif game in ["help", "5"]:
        help_menu()
    elif game in ["quit", "6"]:
        quit_menu()
    else:
        print("Invalid option. Please try again.")
        main_menu()
        
if __name__ == "__main__":
    main_menu()
