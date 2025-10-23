# CtrlUno Arcade - Hangman Game
# Classic word-guessing game with visual hangman progression

# Import Random module for word selection
import random

# Import quit menu for navigation
import quit_menu

#------------------------------------------------------
# GLOBAL VARIABLES - HANGMAN GAME
# Classic word-guessing game with visual feedback
#------------------------------------------------------

# Comprehensive word list spanning various categories and difficulties
HANGMAN_WORDS = ["avatar","matrix","sherlock","pikachu","gollum","beetlejuice","inception","jumanji","justice","ethics","truth","absurd","reason","skeptic","existence","nirvana","jaguar","volcano","tsunami","orchid","glacier","falcon","cactus","panther","quiz","lynx","fjord","zeal","knit","echo","vex","jazz","labyrinth","philosopher","conundrum","paradoxical","metamorphosis","transcendence","hallucination","revolutionary","entropy","illusion","clarity","chaos","serenity","whimsy","grit","valor","myth","legend","oracle","cipher","riddle","enigma","symbol","ritual","dream","vision","fable","tale","story","narrative","dialogue","monologue","soliloquy","tragedy","comedy","satire","irony","parody","meme","advertisement","slogan","tagline","brand","identity","persona","mask","guise","shadow","light","darkness","twilight","dawn","sunset","moonlight","starlight","galaxy","nebula","cosmos","universe","dimension","portal","threshold","liminal","abyss","void","infinity","eternity","time","space","gravity","quantum","atom","particle","wave","frequency","vibration","energy","force","motion","momentum","balance","equilibrium","duality","unity","harmony","discord","conflict","peace","war","battle","struggle","resistance","rebellion","revolution","uprising","awakening","enlightenment","wisdom","knowledge","learning","education","school","teacher","student","mentor","guide","hero","villain","antihero","champion","guardian","protector","warrior","fighter","survivor","wanderer","seeker","pilgrim","traveler","explorer","adventurer","nomad","outsider","stranger","friend","enemy","rival","partner","companion","ally","foe","monster","beast","creature","animal","bird","fish","insect","reptile","mammal","plant","tree","flower","leaf","root","seed","fruit","vegetable","grain","earth","soil","rock","stone","crystal","gem","metal","gold","silver","iron","copper","bronze","steel","glass","mirror","window","door","gate","wall","tower","castle","fortress","temple","shrine","church","mosque","synagogue","altar","sacrifice","offering","prayer","chant","song","melody","rhythm","beat","sound","noise","voice","speech","language","word","letter","text","script","code","signal","message","note","email","call","phone","radio","tv","screen","monitor","keyboard","mouse","tablet","laptop","computer","robot","android","cyborg","machine","engine","motor","gear","wheel","lever","switch","button","sensor","camera","lens","flash","lightbulb","lamp","torch","fire","flame","spark","ember","smoke","ash","dust","cloud","rain","snow","hail","storm","wind","breeze","gust","tornado","hurricane","earthquake","eruption","flood","drought","climate","weather","season","spring","summer","autumn","winter","day","night","hour","minute","second","clock","calendar","schedule","plan","goal","dream","hope","fear","joy","sadness","anger","love","hate","envy","greed","pride","lust","gluttony","sloth","virtue","vice","morality","law","rule","order","freedom","equality","power","control","authority","government","state","nation","country","city","town","village","street","road","path","trail","bridge","river","lake","ocean","sea","bay","coast","beach","island","mountain","hill","valley","canyon","desert","forest","jungle","swamp","marsh","plain","field","meadow","garden","park","zoo","farm","ranch","camp","tent","cabin","house","home","apartment","building","skyscraper","office","store","shop","market","mall","restaurant","cafe","bar","club","theater","cinema","museum","library","hospital","clinic","lab","factory","warehouse","garage","station","airport","port","dock","harbor","ship","boat","car","truck","bus","train","bike","motorcycle","scooter","subway","elevator","escalator","stairs","ladder","rope","chain","lock","key","map","compass","manual","book","novel","poem","essay","article","paper","report","journal","diary","log","record","data","info","fact","lie","rumor","gossip","secret","mystery","clue","evidence","proof","argument","debate","discussion","conversation","question","answer","solution","problem","challenge","task","mission","quest","journey","game","play","win","lose","score","level","stage","round","match","treaty","agreement","contract","deal","trade","exchange","buy","sell","give","take","share","borrow","lend","steal","rob","cheat","trick","deceive","manipulate","dominate","lead","follow","obey","resist","protest","march","strike","vote","elect","judge","sentence","punish","reward","praise","blame","forgive","apologize","regret","remember","forget","think","believe","understand","create","build","destroy","change","grow","shrink","move","stay","run","walk","jump","fly","swim","climb","crawl","dance","sing","talk","listen","watch","look","see","hear","smell","taste","touch","feel"]

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
               return

        elif hangman_play_again in ["no", "n"]:
            quit_menu.quit_menu()
            
        
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