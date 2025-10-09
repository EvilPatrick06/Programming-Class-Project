import random



words = ["apple", "brave", "crisp", "daisy", "eagle", "flame", "grape", "honey", "ivory", "jelly", "karma", "lemon", "mango", "noble", "ocean", "piano", "queen", "raven", "sunny", "tiger", "ultra", "vivid", "witty", "xenon", "yacht", "zesty", "amber", "blush", "charm", "dream", "elbow", "frost", "glide", "haste", "inbox", "jolly", "kneel", "latch", "mirth", "nudge", "orbit", "plume", "quilt", "risky", "swoop", "truce", "unite", "vapor", "whirl", "yield", "zebra", "acorn", "bloom", "cabin", "dwell", "ember", "fable", "gloom", "haste", "ideal", "jumpy", "knack", "lunar", "moist", "nifty", "oxide", "prism", "quirk", "rally", "spice", "tweak", "udder", "vixen", "waltz", "xenon", "young", "zonal", "aloof", "blitz", "candy", "drape", "eerie", "flick", "grind", "hover", "inlet", "joust", "karma", "latch", "mimic", "noble", "ounce", "punch", "quack", "reign", "siren", "tango", "unzip", "vouch", "wacky", "xenon", "yummy", "zebra", "angel", "bland", "climb", "drift", "evoke", "frown", "glare", "haunt", "index", "jumpy", "kneel", "lodge", "motel", "niche", "optic", "pouch", "quake", "risky", "scoop", "tulip", "urban", "vigor", "wrist", "xenon", "youth", "zesty", "amuse", "brisk", "clerk", "dizzy", "elite", "flood", "grasp", "hatch", "input", "jelly", "knock", "latch", "mirth", "nudge", "oxide", "pinto", "quilt", "rider", "swoop", "truce", "unite", "vapor", "whirl", "xylem", "yield", "zebra", "abide", "blaze", "crave", "douse", "eject", "fable", "gauge", "hover", "inbox", "jolly", "kneel", "latch", "mirth", "nudge", "orbit", "plume", "quilt", "risky", "swoop", "truce", "unite", "vapor", "whirl", "xylem"]

def main():
    global hint, cor_word, score, t, cor_let_wrong_spot, attempts
    
    
    t = True

    while t:
        attempts = 0
        gen_word()
        hint = ["_"] * len(cor_word)
        while t:
            cor_let_wrong_spot = 0
            score = 0
            print(" | ".join(hint).upper())
            get_guess()
            check()
            continue
            

def gen_word():
    global cor_word
    cor_word = random.choice(words)
    cor_word = list(cor_word)
    
    
def check():
    global cor_word, hint, score, attempts
    cor_let_wrong_spot = []
    if guess[0] == cor_word[0]:
        score += 1
        
        hint[0] = guess[0].upper()
    elif guess[0] in cor_word:
        cor_let_wrong_spot.append(guess[0])
        
        
                 
    if guess[1] == cor_word[1]:
        score += 1
        
        hint[1] = guess[1].upper()
    elif guess[1] in cor_word:
        cor_let_wrong_spot.append(guess[1])
        
        
        
    if guess[2] == cor_word[2]:
        score += 1
        
        hint[2] = guess[2].upper()
    elif guess[2] in cor_word:
        cor_let_wrong_spot.append(guess[2])
        
        
        
    if guess[3] == cor_word[3]:
        score += 1
        
        hint[3] = guess[3].upper()
    elif guess[3] in cor_word:
        cor_let_wrong_spot.append(guess[3])
    attempts += 1     
        
    if guess[4] == cor_word[4]:
        score += 1
        
        hint[4] = guess[4].upper()
    elif guess[4] in cor_word:
        cor_let_wrong_spot.append(guess[4])
        


    if score == 5:
        print("***************")
        print("YOU WIN!!!")
        print("***************")
        exit()
    elif score != 5:
        print(f"\nyou have ", " | ".join(cor_let_wrong_spot).upper(), " in the wrong spot")
    elif score == 0:
        print("no letters match")
    if attempts >= 6:
        print("you lose\n\n the word was", cor_word)
        exit()








def get_guess():
    global guess, t
    
    while t:
        guess = input("Enter a 5 letter word:\n\n").lower()
        if len(guess) > 5:
            print("invalid input try again")
            continue
        elif len(guess) < 5:
            print("invalid input try again")
            continue
        elif not guess.isalpha():
            print("invalid input try again")
            continue
        break

    
    guess = list(guess)



def give_hint():
    pass




if __name__ == '__main__':
    main()