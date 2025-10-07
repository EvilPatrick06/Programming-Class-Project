import turtle
import random

WORDY_EASY = ["able", "acid", "aged", "also", "area", "army", "away", "baby", "back", "ball", "band", "bank", "base", "bath", "bear", "beat", "been", "beer", "bell", "belt", "best", "bike", "bill", "bird", "blow", "blue", "boat", "body", "bone", "book", "born", "both", "boys", "busy", "call", "calm", "came", "camp", "card", "care", "cars", "case", "cash", "cast", "cats", "cell", "chat", "chip", "city", "club", "coal", "coat", "code", "cold", "come", "cook", "cool", "copy", "corn", "cost", "crew", "crop", "dark", "data", "date", "days", "dead", "deal", "dear", "deep", "desk", "diet", "dirt", "dish", "does", "done", "door", "down", "draw", "drew", "drop", "drug", "dual", "duck", "dust", "duty", "each", "earn", "east", "easy", "edge", "eggs", "else", "even", "ever", "evil", "exit", "eyes", "face", "fact", "fail", "fair", "fall", "fans", "farm", "fast", "fate", "fear", "feed", "feel", "feet", "fell", "felt", "file", "fill", "film", "find", "fine", "fire", "firm", "fish", "fist", "fits", "five", "flag", "flat", "flew", "flow", "folk", "food", "foot", "ford", "fork", "form", "fort", "four", "free", "from", "fuel", "full", "fund", "gain", "game", "gate", "gave", "gear", "gets", "gift", "girl", "give", "glad", "goal", "goes", "gold", "golf", "gone", "good", "grab", "grew", "grey", "grow", "guys", "hair", "half", "hall", "hand", "hang", "hard", "hate", "have", "head", "hear", "heat", "held", "help", "here", "hide", "high", "hill", "hint", "hire", "hits", "hold", "hole", "home", "hope", "host", "hour", "huge", "hung", "hunt", "hurt", "idea", "inch", "into", "iron", "item", "jail", "jane", "jazz", "join", "joke", "jump", "june", "jury", "just", "keep", "kept", "keys", "kick", "kids", "kill", "kind", "king", "knee", "knew", "know", "lack", "lady", "laid", "lake", "land", "lane", "last", "late", "lead", "left", "legs", "less", "lets", "life", "lift", "like", "line", "link", "list", "live", "load", "loan", "lock", "long", "look", "lord", "lose", "loss", "lost", "lots", "loud", "love", "luck", "made", "mail", "main", "make", "male", "mall", "many", "mark", "mass", "math", "meal", "mean", "meat", "meet", "melt", "menu", "mess", "mice", "mile", "milk", "mind", "mine", "miss", "mode", "mood", "moon", "more", "most", "move", "much", "must", "name", "navy", "near", "neck", "need", "news", "next", "nice", "nine", "none", "noon", "nose", "note", "nuts", "okay", "once", "only", "open", "oral", "over", "pace", "pack", "page", "paid", "pain", "pair", "palm", "park", "part", "pass", "past", "path", "peak", "pick", "pics", "pile", "pink", "pipe", "plan", "play", "plot", "plus", "poem", "pole", "poll", "pool", "poor", "pope", "port", "post", "pull", "pure", "push", "puts", "race", "rain", "rank", "rate", "read", "real", "rear", "rely", "rent", "rest", "rice", "rich", "ride", "ring", "rise", "risk", "road", "rock", "role", "roll", "roof", "room", "root", "rope", "rose", "rule", "runs", "safe", "said", "sail", "sale", "salt", "same", "sand", "save", "says", "seal", "seat", "seed", "seek", "seem", "seen", "self", "sell", "send", "sent", "ship", "shoe", "shop", "shot", "show", "shut", "sick", "side", "sign", "silk", "sing", "sink", "site", "size", "skin", "skip", "slip", "slow", "snap", "snow", "soap", "soft", "soil", "sold", "sole", "some", "song", "soon", "sort", "soul", "soup", "spot", "star", "stay", "step", "stir", "stop", "such", "suit", "sure", "swim", "take", "tale", "talk", "tall", "tank", "tape", "task", "team", "tell", "tend", "tent", "term", "test", "text", "than", "that", "them", "then", "they", "thin", "this", "thus", "tide", "tied", "ties", "time", "tiny", "tips", "tire", "told", "tone", "took", "tool", "tops", "torn", "tour", "town", "toys", "tree", "trim", "trip", "true", "tune", "turn", "twin", "type", "unit", "used", "user", "uses", "vary", "vast", "very", "view", "vote", "wait", "wake", "walk", "wall", "want", "warm", "warn", "wash", "wave", "ways", "weak", "wear", "week", "well", "went", "were", "west", "what", "when", "wide", "wife", "wild", "will", "wind", "wine", "wing", "wire", "wise", "wish", "with", "wood", "wool", "word", "wore", "work", "worn", "yard", "year", "your", "zero", "zone"]
WORDY_MEDIUM = ["about", "above", "abuse", "actor", "acute", "admit", "adopt", "adult", "after", "again", "agent", "agree", "ahead", "alarm", "album", "alert", "alien", "align", "alike", "alive", "allow", "alone", "along", "alter", "among", "anger", "angle", "angry", "apart", "apple", "apply", "arena", "argue", "arise", "array", "arrow", "aside", "asset", "avoid", "awake", "award", "aware", "badly", "baker", "bases", "basic", "beach", "began", "begin", "being", "below", "bench", "billy", "birth", "black", "blame", "blind", "block", "blood", "bloom", "blown", "blues", "blunt", "blush", "board", "boast", "bonds", "boost", "booth", "bound", "brain", "brand", "brass", "brave", "bread", "break", "breed", "brief", "bring", "broad", "broke", "brown", "brush", "build", "built", "burst", "buyer", "cable", "calif", "carry", "catch", "cause", "chain", "chair", "chaos", "charm", "chart", "chase", "cheap", "check", "chest", "chief", "child", "china", "chose", "civil", "claim", "class", "clean", "clear", "click", "climb", "clock", "close", "cloud", "clown", "clubs", "coach", "coast", "could", "count", "court", "cover", "craft", "crash", "crazy", "cream", "crime", "cross", "crowd", "crown", "crude", "curve", "cycle", "daily", "dance", "dated", "dealt", "death", "debut", "delay", "depth", "doing", "doubt", "dozen", "draft", "drama", "drank", "dream", "dress", "drill", "drink", "drive", "drove", "dying", "eager", "early", "earth", "eight", "elite", "empty", "enemy", "enjoy", "enter", "entry", "equal", "error", "event", "every", "exact", "exist", "extra", "faith", "false", "fault", "fiber", "field", "fifth", "fifty", "fight", "final", "first", "fixed", "flash", "fleet", "floor", "fluid", "focus", "force", "forth", "forty", "forum", "found", "frame", "frank", "fraud", "fresh", "front", "fruit", "fully", "funny", "giant", "given", "glass", "globe", "going", "grace", "grade", "grand", "grant", "grass", "grave", "great", "green", "gross", "group", "grown", "guard", "guess", "guest", "guide", "happy", "harry", "heart", "heavy", "hence", "henry", "horse", "hotel", "house", "human", "hurry", "image", "index", "inner", "input", "issue", "japan", "jimmy", "joint", "jones", "judge", "known", "label", "large", "laser", "later", "laugh", "layer", "learn", "lease", "least", "leave", "legal", "level", "lewis", "light", "limit", "links", "lives", "local", "loose", "lower", "lucky", "lunch", "lying", "magic", "major", "maker", "march", "maria", "match", "maybe", "mayor", "meant", "media", "metal", "might", "minor", "minus", "mixed", "model", "money", "month", "moral", "motor", "mount", "mouse", "mouth", "moved", "movie", "music", "needs", "never", "newly", "night", "noise", "north", "noted", "novel", "nurse", "occur", "ocean", "offer", "often", "order", "other", "ought", "paint", "panel", "paper", "party", "peace", "peter", "phase", "phone", "photo", "piano", "picked", "piece", "pilot", "pitch", "place", "plain", "plane", "plant", "plate", "plays", "plaza", "point", "pound", "power", "press", "price", "pride", "prime", "print", "prior", "prize", "proof", "proud", "prove", "queen", "quick", "quiet", "quite", "radio", "raise", "range", "rapid", "ratio", "reach", "ready", "realm", "rebel", "refer", "relax", "repay", "reply", "right", "rigid", "risky", "river", "robin", "roger", "roman", "rough", "round", "route", "royal", "rural", "salad", "sales", "sat", "sauce", "scale", "scare", "scene", "scope", "score", "sense", "serve", "seven", "shall", "shape", "share", "sharp", "sheet", "shelf", "shell", "shift", "shine", "shirt", "shock", "shoot", "short", "shown", "sides", "sight", "simon", "since", "sixth", "sixty", "sized", "skill", "sleep", "slide", "small", "smart", "smile", "smith", "smoke", "snake", "snow", "soapy", "social", "solar", "solid", "solve", "sorry", "sound", "south", "space", "spare", "speak", "speed", "spend", "spent", "split", "spoke", "sport", "staff", "stage", "stake", "stand", "start", "state", "stays", "steal", "steam", "steel", "steep", "steer", "stern", "stick", "still", "stock", "stone", "stood", "store", "storm", "story", "strip", "stuck", "study", "stuff", "style", "sugar", "suite", "super", "sweet", "swift", "swing", "swiss", "table", "taken", "taste", "taxes", "teach", "terms", "texas", "thank", "theft", "their", "theme", "there", "these", "thick", "thing", "think", "third", "those", "three", "threw", "throw", "thumb", "tiger", "tight", "timer", "title", "today", "topic", "total", "touch", "tough", "tower", "track", "trade", "train", "trait", "treat", "trend", "trial", "tribe", "trick", "tried", "tries", "truck", "truly", "trust", "truth", "twice", "twist", "tyler", "uncle", "under", "undue", "union", "unity", "until", "upper", "upset", "urban", "usage", "usual", "valid", "value", "video", "virus", "visit", "vital", "vocal", "voice", "waste", "watch", "water", "wave", "ways", "wealth", "weary", "weigh", "weird", "wheel", "where", "which", "while", "white", "whole", "whose", "wiped", "wired", "woman", "world", "worry", "worse", "worst", "worth", "would", "write", "wrong", "wrote", "young", "yours", "youth", "zones"]
WORDY_HARD = ["absolute", "abstract", "academic", "accepted", "accident", "accuracy", "accurate", "achieved", "acquired", "activity", "actually", "addition", "adequate", "adjacent", "adjusted", "advanced", "advisory", "advocate", "affected", "aircraft", "although", "analysis", "annually", "answered", "anywhere", "apparent", "appeared", "approach", "approval", "approved", "argument", "arranged", "ArticleS", "assemble", "assembly", "assessed", "assigned", "assisted", "assuming", "attached", "attacked", "attempts", "attended", "attorney", "audience", "authored", "automate", "autonomy", "bathroom", "becoming", "behavior", "believed", "benefits", "birthday", "boundary", "breakfast", "bringing", "brothers", "building", "business", "calendar", "campaign", "capacity", "category", "chairman", "champion", "chapters", "chemical", "children", "choosing", "churches", "circular", "citation", "citizens", "civilian", "claiming", "cleaning", "clearing", "climbing", "clinical", "clothing", "coaching", "cocktail", "collapse", "collected", "colonial", "colorful", "combines", "commands", "commerce", "commonly", "communicate", "compared", "compiler", "complete", "composed", "compound", "computed", "computer", "concepts", "concrete", "confused", "congress", "connects", "consider", "consists", "constant", "contains", "contests", "contexts", "continue", "contract", "contrast", "controls", "convince", "creating", "creative", "criminal", "crossing", "crushing", "cultural", "customer", "database", "deadline", "deciding", "decision", "declared", "decrease", "delivery", "demands", "democrat", "depends", "describe", "designed", "designer", "detailed", "detected", "develop", "dialogue", "diamond", "differed", "digital", "directly", "director", "disabled", "disaster", "discount", "discover", "disguise", "disorder", "disposed", "distance", "distinct", "district", "dividend", "division", "document", "domestic", "dominant", "downtown", "dramatic", "drawings", "dropdown", "duration", "dynamics", "economic", "educated", "election", "electric", "eligible", "employee", "employer", "enabling", "encoding", "endorsed", "engaging", "engineer", "enhanced", "enormous", "entering", "entirely", "entitled", "envelope", "equality", "equation", "equipped", "estimate", "evaluate", "eventual", "everyone", "evidence", "exampled", "exchange", "exciting", "executed", "exercise", "existing", "expected", "expertise", "explains", "explored", "extended", "external", "facebook", "facility", "familiar", "families", "featured", "features", "feedback", "feelings", "festival", "filename", "filtered", "finished", "floating", "followed", "football", "forecast", "foreign", "formally", "formerly", "formulae", "fraction", "frequent", "friendly", "function", "funding", "gathered", "generate", "genetics", "geometry", "goldfish", "graduate", "graphics", "greatest", "handbook", "handling", "hardware", "headline", "heritage", "highway", "historic", "holidays", "hometown", "hospital", "hundreds", "husband", "identify", "identity", "illusion", "imagined", "immature", "imperial", "implicit", "imported", "improved", "incident", "includes", "increase", "indicate", "indirect", "industry", "infected", "infinite", "informed", "initiate", "injured", "innocent", "inserted", "inspired", "instance", "instinct", "intended", "interact", "interest", "internal", "internet", "interval", "intimate", "involved", "isolated", "keyboard", "knowledge", "language", "launched", "learning", "lectures", "leverage", "lifetime", "likewise", "limiting", "listened", "literacy", "literary", "location", "machines", "magnetic", "maintain", "majority", "managing", "marriage", "material", "meanings", "measured", "mechanic", "medicine", "meetings", "membrane", "memorial", "mentions", "merchant", "midnight", "military", "minimize", "ministry", "minority", "missiles", "missions", "mistakes", "modeling", "moderate", "modified", "molecule", "momentum", "monitors", "mortgage", "motivated", "mountain", "movement", "multiple", "national", "negative", "networks", "normally", "notebook", "noticein", "november", "numbered", "numerous", "observed", "obtained", "occasion", "occupied", "occurred", "offering", "official", "offshore", "operates", "operator", "opinions", "opponent", "optional", "ordinary", "organize", "oriental", "original", "outdated", "outlined", "outright", "overcome", "overhead", "overseas", "overview", "packages", "painting", "paradise", "parallel", "parental", "partners", "passport", "password", "patience", "patterns", "payments", "peaceful", "performs", "personal", "persuade", "petition", "physical", "pictures", "planning", "platform", "pleasure", "policies", "politics", "popular", "portrait", "position", "positive", "possible", "possibly", "practice", "precious", "prepared", "presence", "preserve", "pressure", "previous", "princess", "priority", "prisoner", "probably", "problems", "proceed", "products", "progress", "projects", "promises", "property", "proposal", "proposed", "prospect", "protocol", "provided", "provider", "province", "publicly", "purchase", "purposes", "pursuant", "quantity", "question", "quotient", "reaction", "readings", "realized", "reasoned", "received", "recently", "recorded", "recovery", "redirect", "reducing", "referred", "reflects", "regarded", "regional", "register", "regulate", "rejected", "relation", "relative", "released", "relevant", "reliable", "remained", "removing", "repeated", "replaced", "reported", "republic", "required", "research", "reserved", "resident", "resolved", "resource", "response", "resulted", "returned", "revealed", "reversed", "reviewed", "revision", "rewards", "sandwich", "schedule", "sciences", "security", "selected", "semester", "sequence", "services", "sessions", "settings", "shoulder", "siblings", "silently", "simulate", "situated", "slightly", "software", "solution", "somebody", "somewhat", "southern", "speaking", "specific", "specimen", "spelling", "spending", "sponsors", "standard", "standing", "stations", "sterling", "straight", "strategy", "strength", "striking", "strongly", "struggle", "students", "subjects", "subtitle", "suitable", "summoned", "supplies", "supposed", "supports", "surprise", "survived", "swimming", "symbolic", "symphony", "symptoms", "syndrome", "teachers", "teaching", "teamwork", "technics", "terminal", "textbook", "theories", "thinking", "thoughts", "thousand", "threatens", "thursday", "together", "tomorrow", "tracking", "training", "transfer", "traveled", "treasure", "triangle", "tropical", "troubled", "tumbling", "tutorial", "umbrella", "unbiased", "uncommon", "undefied", "underway", "unfunny", "universe", "unlikely", "unnotice", "unsigned", "username", "vacation", "validate", "variable", "vehicles", "verified", "versions", "vertical", "vicinity", "violence", "virginia", "visiting", "warranty", "watching", "weakness", "whatever", "wildlife", "withdraw", "wondered", "workflow", "workload", "workshop", "wrapping", "yourself"]

tries = 6

# Get the guess
def guessing():
    global guess
    global guess_check
    guess = input("Whats your guess?").lower()
    guess_check = list(guess)
    print(guess_check)
    


# pick the word
def pick_word(difficulty):
    if difficulty == "easy":
        return random.choice(WORDY_EASY)
    elif difficulty == "medium":
        return random.choice(WORDY_MEDIUM)
    else:
        return random.choice(WORDY_HARD)
    
# --- Main game logic ---
def play_wordy(rows, cols, word_length, difficulty):
    jc = turtle.Turtle()
    jc.hideturtle()
    jc.speed(0)
    jc.pensize(3)

    draw_grid(rows, cols, jc)
    word = pick_word(difficulty)
    word_letters = list(word)

   for attempt in range(rows):
    while True:
        guess = input(f"Attempt {attempt + 1}: Enter a {word_length}-letter word: ").lower()
        if len(guess) != word_length:
            print("Invalid length, try again.")
            continue
        break
    guess_letters = list(guess)

    if guess == word:
        print("Congratulations! You guessed the word!")
        break
else:
    print(f"Sorry, you ran out of attempts. The word was: {word}")

    # First color correct letters green, then yellow for wrong spot
    def color_square(turtle_obj, row, col, color, rows, cols):
        start_x = -cols * SQUARE_SIZE / 2
        start_y = rows * SQUARE_SIZE / 2
        x = start_x + col * SQUARE_SIZE
        y = start_y - row * SQUARE_SIZE
        turtle_obj.penup()
        turtle_obj.goto(x, y)
        turtle_obj.pendown()
        turtle_obj.fillcolor(color)
        turtle_obj.begin_fill()
        for _ in range(4):
            turtle_obj.forward(SQUARE_SIZE)
            turtle_obj.right(90)
        turtle_obj.end_fill()


        

#Constants
SQUARE_SIZE = 70
GRID_COLOR = "black"
BACKGROUND_COLOR = "white"

def draw_grid(rows, cols, square_size=70):
    jc = turtle.Turtle()
    jc.hideturtle()
    jc.speed(0)
    jc.pensize(3)
    
    # Draw title above the grid
    jc.penup()
    jc.goto(0, rows * square_size / 2 + 20)
    jc.write("Wordy", align="center", font=("Verdana", 40, "bold"))
    
    # Draw each square
    start_x = -cols * square_size / 2
    start_y = rows * square_size / 2

    for row in range(rows):
        for col in range(cols):
            x = start_x + col * square_size
            y = start_y - row * square_size
            jc.penup()
            jc.goto(x, y)
            jc.pendown()
            for _ in range(4):
                jc.forward(square_size)
                jc.right(90)
#Fill a square with color                
def write_letter(turtle_obj, letter, row, col, rows, cols):
    start_x = -cols * SQUARE_SIZE / 2
    start_y = rows * SQUARE_SIZE / 2
    x = start_x + col * SQUARE_SIZE + SQUARE_SIZE / 2
    y = start_y - row * SQUARE_SIZE - SQUARE_SIZE * 0.75
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.color("black")
    turtle_obj.write(letter.upper(), align="center", font=("Arial", 32, "bold"))



def main_menu():
    game = input(" \n What game do you want to play:\n\n1: Wordy?\n2: Tres?\n3: Quit? \n \n").lower()
    if game == "wordy" or game == "1":
        print(" \n Welcome to Wordy! You have 6 tries to guess the correct 5 letter word.\n After each guess, you'll receive feedback on how many letters are in the right position, as well as which letters are correct but in the wrong position. Good luck!")
        difficulty = input("\n Choose your difficulty: \n\n1: Easy\n2: Medium\n3: Hard\n \n").lower()
        difficulty_levels = {
            "easy": (6, 4),
            "medium": (6, 5),
            "hard": (6, 8)
        }
        if difficulty in ["easy", "1"]:
            ROWS, COLS = difficulty_levels["easy"]
            play_wordy(ROWS, COLS, COLS, "easy")
        elif difficulty in ["medium", "2"]:
            ROWS, COLS = difficulty_levels["medium"]
            play_wordy(ROWS, COLS, COLS, "medium")
        elif difficulty in ["hard", "3"]:
            ROWS, COLS = difficulty_levels["hard"]
            play_wordy(ROWS, COLS, COLS, "hard")
        else:
            print("Invalid choice, defaulting to medium.")
            ROWS, COLS = difficulty_levels["medium"]
            play_wordy(ROWS, COLS, COLS, "medium")
    elif game == "tres" or game == "2":
        print("sorry, under construction rn :'(")
    elif game == "quit" or game == "3":
        print("\n Exiting the game. Goodbye! \n")
        exit()

main_menu()
turtle.done()

