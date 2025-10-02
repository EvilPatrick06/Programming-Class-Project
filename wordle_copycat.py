import random
import time


WORDS = ["apple", "brave", "crisp", "daisy", "eagle", "flame", "grape", "honey", "ivory", "jolly",
"knack", "lemon", "mango", "noble", "ocean", "piano", "quilt", "raven", "sugar", "tiger",
"umbra", "vivid", "waltz", "xenon", "yacht", "zesty", "acorn", "blaze", "charm", "drift",
"elbow", "frost", "glide", "haste", "inbox", "jumps", "karma", "latch", "mirth", "nudge",
"orbit", "plume", "quack", "risky", "swoop", "truce", "unite", "vapor", "whirl", "xylem",
"yield", "zebra", "aloof", "bloom", "climb", "dwell", "evoke", "fable", "gloom", "haste",
"ideal", "jewel", "kneel", "lunar", "moist", "nifty", "oxide", "punch", "quell", "rider",
"spice", "tweak", "ultra", "vixen", "wiser", "xerox", "young", "zonal", "angel", "blunt",
"cabin", "dealt", "eager", "flick", "grind", "haunt", "inlet", "jumpy", "kiosk", "latch",
"motel", "noble", "ounce", "prism", "quiet", "ranch", "siren", "tulip", "udder", "vocal",
"witty", "xenon", "yummy", "zippy", "amber", "bison", "candy", "dizzy", "eject", "fuzzy",
"giddy", "hippo", "input", "jelly", "koala", "liver", "mimic", "ninja", "otter", "panda",
"quark", "reign", "sassy", "tango", "urban", "vigor", "wacky", "xenon", "yodel", "zebra",
"argue", "bliss", "crane", "drape", "elite", "finer", "grace", "hover", "index", "joust",
"knock", "lodge", "mover", "noble", "optic", "pouch", "quake", "risky", "slope", "treat",
"unzip", "voter", "wound", "xenon", "youth", "zebra", "adore", "brisk", "crown", "dough",
"eerie", "frown", "gauge", "hatch", "inbox", "jumps", "kneel", "latch", "mirth", "nudge",
"orbit", "plume", "quack", "risky", "swoop", "truce", "unite", "vapor", "whirl", "xylem",
"yield", "zesty", "amuse", "blame", "crush", "dizzy", "eject", "fuzzy", "giddy", "hippo",
"input", "jelly", "koala", "liver", "mimic", "ninja", "otter", "panda", "quark", "reign",
"sassy", "tango", "urban", "vigor", "wacky", "xenon", "yodel", "zebra", "argue", "bliss",
"crane", "drape", "elite", "finer", "grace", "hover", "index", "joust", "knock", "lodge"]

tries = 6
attempt = 0
score = 0


# Get the guess
def guessing():
    global guess
    global guess_check
    guess = input("Whats your guess?").lower()
    guess_check = list(guess)
    print(guess_check)
    


# pick the word
def gen_word():
    global cor_word
    global cor_word_check
    global guess_check
    cor_word = random.choice(WORDS)
    cor_word_check = list(cor_word)

    print (cor_word_check)

# Check if letters match anywhere     (needs work)
def check():
    global cor_word_check
    global guess_check
    global score
    global guess
    while score != 5:
        score = 0
        cor_lett = 0
        # shared = guess_check and cor_word_check
        guess = input("Whats your guess?").lower()
        guess_check = list(guess)
        print(guess_check)
        if cor_word_check[0] == guess_check[0]:
            score += 1
            cor_lett += 1
        if cor_word_check[1] == guess_check[1]:
            score += 1
            cor_lett +=1
        if cor_word_check[2] == guess_check[2]:
            score += 1
            cor_lett += 1
        if cor_word_check[3] == guess_check[3]:
            score += 1
            cor_lett += 1
        if cor_word_check[4] == guess_check[4]:
            score += 1 
            cor_lett += 1
        if score == 5:
            print("Congrats you won")
            exit()
        print(f"you have {cor_lett} in the right spot")
       








gen_word()
check()