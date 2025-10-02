import random


WORDS = ["abide","about","above","abuse","actor","acute","adapt","admit","adobe","adopt","adult","after","again","agent","agile","aging","agree","aisle","alarm","album","alert","alien","align","alike","alive","allow","alone","along","aloud","alpha","altar","alter","amber","amend","amino","among","ample","angel","anger","angle","angry","ankle","apple","apply","arena","argue","arise","armor","arose","array","arrow","aside","asset","atlas","audio","audit","avoid","await","awake","award","aware","awful","bacon","badge","badly","baked","baker","baron","bases","basic","basil","basin","basis","batch","beach","beard","beast","begin","being","belly","below","bench","berry","birth","black","blade","blame","blank","blast","blaze","bleak","blend","blind","block","blood","bloom","blown","blues","blunt","board","boast","bonus","boost","booth","borne","bound","brain","brake","brand","brass","brave","bread","break","breed","brick","bride","brief","bring","brisk","broad","broke","brook","brown","brush","build","built","bunch","burnt","burst","buyer","cabin","cable","cache","canal","candy","canon","cargo","carol","carry","catch","cater","cause","cease","chain","chair","chalk","chaos","charm","chart","chase","cheap","check","cheek","cheer","chess","chest","chick","chief","child","chill","china","choir","chose","chuck","civic","civil","claim","clash","class","clean","clear","clerk","click","cliff","climb","clock","close","cloth","cloud","coach","coast","colon","color","comic","condo","coral","corps","couch","cough","could","count","court","cover","crack","craft","crane","crash","crazy","cream","creek","crest","crime","crisp","cross","crowd","crown","crude","cruel","crush","crust","cubic","curry","curve","cycle","daily","dairy","daisy","dance","dated","dealt","death","debit","debut","decay","delay","delta","dense","depot","depth","devil","diary","digit","dirty","dodge","doing","donor","doubt","dozen","draft","drain","drama","drank","drawn","dream","dress","drift","drill","drink","drive","drove","drunk","dusty","dying","eager","eagle","early","earth","eaten","eight","elbow","elder","elect","elite","empty","enemy","enjoy","enter","entry","equal","error","essay","event","every","exact","excel","exert","exile","exist","extra","faint","fairy","faith","false","fancy","fatal","fault","feast","fence","fetch","fever","field","fiery","fifth","fifty","fight","final","first","fixed","flame","flash","fleet","flesh","flies","flint","float","flock","flood","floor","flora","flour","flown","fluid","flung","flush","focal","focus","force","forge","forth","forty","found","frame","frank","fraud","fresh","fried","front","frost","fruit","fully","funny","gamma","gauge","genre","ghost","giant","given","glass","globe","glory","glove","going","grace","grade","grain","grand","grant","graph","grasp","grass","grave","great","greed","green","greet","grief","grill","gross","group","grove","grown","guard","guess","guest","guide","guild","guilt","habit","handy","happy","hardy","harry","harsh","hatch","haven","heart","heath","heavy","hedge","hefty","hello","hence","hobby","holly","homer","honey","honor","horse","hotel","house","human","hurry","ideal","image","imply","incur","index","inner","input","inter","irony","issue","ivory","japan","jenny","jewel","joint","judge","juice","juicy","jumps","karma","kayak","kebab","ketch","kicks","kinda","knife","knock","known","label","labor","laced","lacks","laden","lager","lakes","lambs","lamps","lands","lapse","large","laser","lasts","later","laugh","layer","leads","leafy","leaks","learn","lease","least","leave","legal","lemon","level","lever","light","liked","likes","limbs","limit","lined","linen","liner","lines","links","lions","lists","lived","liver","lives","loads","loans","lobby","local","locks","lodge","logic","looks","loose","lords","loses","loved","lover","loves","lucky","lunar","lunch","lungs","lured","lures","lying","macro","magic","maids","mails","major","maker","males","malls","masks","match","mates","mayor","meals","means","meant","meats","medal","media","meets","melon","menus","mercy","merge","merit","merry","metal","meter","micro","miles","minds","mines","minor","minus","mixed","mixer","mixes","model","modem","modes","moist","money","month","moral","motor","mount","mouse","mouth","moved","moves","movie","music","nails","naked","named","names","nanny","nasty","natal","naval","necks","needs","nerds","never","newer","newly","nicer","niche","night","ninja","ninth","noble","noise","noisy","north","noted","notes","novel","nurse","nylon","ocean","offer","often","older","olive","omega","onion","opens","opera","orbit","order","organ","other","ought","ounce","outer","owned","owner","packs","pains","paint","pairs","panel","panic","pants","paper","parks","parts","party","pasta","patch","paths","pause","peace","peach","peaks","pearl","pedal","peers","penis","penny","perks","pests","petal","phase","phone","piano","picks","piece","piles","pills","pilot","pines","pipes","pitch","pixel","pizza","place","plain","plane","plant","plate","plays","plaza","plead","plows","point","poker","polar","poles","polls","ponds","pools","porch","ports","posed","poses","pound","power","press","price","pride","prime","print","prior","prize","probe","prone","proof","props","proud","prove","proxy","pulse","pumps","punch","pupil","puppy","purse","queen","query","quest","quick","quiet","quilt","quite","quota","quote","raced","races","racks","radar","radio","rails","rainy","raise","rally","ranch","range","ranks","rapid","rated","rates","ratio","reach","react","reads","ready","realm","rebel","refer","reign","relax","relay","relic","remix","renal","renew","rents","reply","reset","resin","rests","retro","rider","rides","ridge","rifle","right","rings","risen","rises","risky","rival","river","roads","robot","rocks","rocky","roles","rolls","roman","rooms","roots","ropes","rough","round","route","royal","ruins","ruled","ruler","rules","rural","sadly","safer","sails","saint","salad","sales","sally","salon","sandy","sauce","saved","saves","scale","scalp","scans","scare","scarf","scary","scene","scent","scoop","scope","score","scout","screw","seals","seats","seeds","seeks","seems","sells","sends","sense","serum","serve","seven","sever","sewed","sewer","shade","shaft","shake","shall","shame","shape","share","sharp","shave","sheep","sheer","sheet","shelf","shell","shift","shine","shiny","shirt","shock","shoes","shoot","shops","shore","short","shots","shout","shown","shows","sides","siege","sight","sigma","signs"]
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

# Check if letters match anywhere 
def check():
    global cor_word_check
    global guess_check
    global score
    global guess
    while score != 5:
        score = 0
        cor_lett = 0
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

# Main menu
def main_menu():
    while game < 0 and game > 2:
            game = int(input(" what game you wanna play:\n1: wordel?\n2:uno "))
            if game == 1
                gen_word()
                check()
            if game == 2
                print("sorry, under construction rn :'(")

main_menu()

