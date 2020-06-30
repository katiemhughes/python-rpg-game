import sys,time,os,random

def Look_for_a_clue():
    print("You begin to look around the room")
    print("")
    time.sleep(2)
    print("There's a set of lockers and a Table with some papers on it")
    print("")
    time.sleep(1)
    print("What do you want to look at?")
    print("")
    choice = input("[Open locker / Look at the table]")
    if choice == "Open locker" or choice == "open locker" :
        print("")
        time.sleep(2)
        print("")
        print("It's EMPTY!!!!!")
        time.sleep(2)
        print("")
        print("Is there anything else you can look at")
        Look_for_a_clue()
    elif choice == ("Look at the table") or choice == ("look at the table"):
        print("There's a post it note here, it reads:")
        print("")
        time.sleep(2)
        print("James....... this is the third time this week. Do not lose this - The password is drowssaP")
        print("")
        time.sleep(2)
        print("This must be the password, let's give it a try")
        print("")
        time.sleep(2)
        print("You walk over to the keypad by the door")
        print("")
        Password_attempt_one()

def Password_last_go():
    print("Please enter your third and final attempt")
    print("")
    user_guess = input("")
    if user_guess == "drowssaP" or user_guess == "drowssap":
        print("DOOR OPENING")
        print("")
        print("..........")
        time.sleep(2)
        print("ACCESS GRANTED")
        print("")
        time.sleep(2)
        print("The Door opens....... You push both doors open and feel the fresh air against your face")
        print("")
        time.sleep(2)
        print("You've escaped, Congratulations")
        print("""              ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'
​
~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^""")
    else:
        print("Password incorrect, you have one attempt remaining. Maybe there's a clue somewhere") 
        print("")
        time.sleep(2)
        print("You have had 3 attempts, you had a chance to look for clues")
        print("")
        time.sleep(2)
        print("Your password has failed. The alarm has been set off")
        print("")
        time.sleep(2)
        print("You hear the horde of Zombies rushing towards you")
        print("")
        time.sleep(2)
        print("They break down the door......")
        print("")
        print("The Zombies climb over each other to rush towards you.....")
        print("")
        time.sleep(2)
        print("GAMEOVER")
        # start_game()

def Password_second_attempt():
    print("Please enter your second attempt")
    user_guess = input("")
    if user_guess == "drowssaP" or user_guess == "drowssap":
        print("DOOR OPENING")
        print("")
        time.sleep(2)
        print("ACCESS GRANTED")
        print("")
        time.sleep(2)
        print("The Door opens....... You push both doors open and feel the fresh air against your face")
        print("")
        time.sleep(2)
        print("You've escaped, Congratulations")
        print(r"""              ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'
​
~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^""")
    else:
        print("Password incorrect, you have one attempt remaining. Maybe there's a clue somewhere") 
        print("Look for clues / Try one more time")
        user_guess = input("")
    if user_guess == "Look for clues" or user_guess == "look for clues":
        Look_for_a_clue()
    else:
        Password_last_go()

def Password_attempt_one():
    print("TERMINAL = Please enter your Password")
    user_guess = input("")
    if user_guess == "drowssaP" or user_guess == "drowssap":
        print("DOOR OPENING")
        print("")
        time.sleep(2)
        print("ACCESS GRANTED")
        print("")
        time.sleep(2)
        print("The Door opens....... You push both doors open and feel the fresh air against your face")
        print("")
        time.sleep(2)
        print("You've escaped, Congratulations")
        print(r"""              ,.  _~-.,               .
           ~'`_ \/,_. \_
          / ,"_>@`,__`~.)             |           .
          | |  @@@@'  ",! .           .          '
          |/   ^^@     .!  \          |         /
          `' .^^^     ,'    '         |        .             .
           .^^^   .          \                /          .
          .^^^       '  .     \       |      /       . '
.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '
&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  .
%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,
&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=
%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'
##mjy#####*"'
_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'
​
~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^""")
    else:
        print("Password incorrect, you have two attempts remaining")
        Password_second_attempt() 
            
def The_Password():
    print("You made it through the door and quickly bolt it from the otherside.")
    print("")
    time.sleep(1)
    print("You look around to see a few lockers, a table and a big set of bolted doors, they're locked")
    print("")
    time.sleep(1)
    print("You're locked inside!!!!!")
    print("")
    time.sleep(1)
    print("Next to the door there is a keypad. 'Oh no'! It needs a password!")
    print("")
    time.sleep(1)
    print ("What would you like to do?")
    print("")
    choice = input("Would you like to: [Attempt the password/Look for a clue]")
    if choice == "attempt the password" or choice == "Attempt the password":
        print("Okay good luck")
        Password_attempt_one()
    elif choice == "Look for a clue" or choice == "look for a clue":
        print("Okay, let's look around the room")     
        Look_for_a_clue()
    else:
        print("Was that an option???")
        The_Password()

def The_attack():
    import random
    Attack_options = [
    "You run at the Zombie, you seriously underestimated how big he was. He knocks you to the floor and pounces on you. What were you thinking???", 
    "You run towards the Zombie as fast as you can. You manage to knock him to the floor sustaining only a little scratch in the process",
    "You pick up speed and run full pelt towards the Zombie, thankfully he's slow and completely misses you",
    "You gather all your strength and push the zombie to the wall avoiding his scratching and biting as you make your way to the door",
    "You run towards the zombie, tripping on a piece of rubbish and twisting your ankle. The Zombie falls on top of you and bites you. Game over",
    "The Zombie is big, but he's also slow. You run past it with ease and get through the door"
    ]
    attack_result = random.choice(Attack_options)
    print("")
    print(attack_result)
    print("")
    if attack_result == "The Zombie is big, but he's also slow. You run past it with ease and get through the door" or attack_result == "You gather all your strength and push the zombie to the wall avoiding his scratching and biting as you make your way to the door" or attack_result == "You run towards the Zombie as fast as you can. You manage to knock him to the floor sustaining only a little scratch in the process" or attack_result == "You pick up speed and run full pelt towards the Zombie, thankfully he's slow and completely misses you":
        The_Password()
    elif attack_result == "You run at the Zombie, you seriously underestimated how big he was. He knocks you to the floor and pounces on you. What were you thinking???" or attack_result == "You run towards the zombie, tripping on a piece of rubbish and twisting your ankle. The Zombie falls on top of you and bites you. Game over":
        print("")
        print("That was just a bit of bad luck really, let's try again")
        print("")
        chapter_4()

def chapter_4():
    time.sleep(2)
    print("")
    print("You walk down a dark corridor, the lights are flickering and you can hear sounds up ahead.")
    print("")
    time.sleep(2)
    print ("'EURGHHHHHHHH', It's another Zombie! Stood right by the 'staff exit' door.")
    print("")
    time.sleep(2)
    print("'EURRRRGGHHHHHHHHHHH', You look ahead!!!")
    print("")
    print("")
    time.sleep(3)
    print(r"""__________
    |STAFF EXIT|
     ----------
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      "/""`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~) """)
    time.sleep(2)
    print("")
    print("It looks like a security guard that was bitten.")
    time.sleep(1)
    print("")
    question = input("You're going to have to make a choice, do you turn back the way you came or do you tackle the security guard Zombie?.[Go for it/Turn back]")
    if question == "Go for it" or question == "go for it":
        print("Great, let's go.")
        The_attack()
    elif question == "Turn back":
        print("Not the best idea given how many Zombie you had to get pass to get here")
        The_attack()
    else:
        print("Try again, I didn't recognise that.")

def anothermove():
    another_move = input("Do you want to attempt to wrestle the zombie off you, knee its private parts or wait and hope it becomes tired and gives up? [wrestle/knee/wait]") 
    if another_move == "wrestle" or another_move == "Wrestle" or another_move == "WRESTLE":
        
        
        i = 0
        for rand in range (1):
            rand=random.randint(0,20)  
            i+= 1
    
    if rand < 10:
        print("You need to keep trying to wrestle the zombie")
        # print (rand)
        anothermove()
    elif rand > 10:
        # print (rand)
        print("You managed to fling the zombie off you and succesfully make it onto the corridor")
        chapter_4()
    
    elif another_move == "knee" or another_move == "KNEE" or another_move == "Knee":
        print("You drive your knee into the zombies private parts")
        time.sleep(2)
        print("THUD!!!")
        time.sleep(2)
        print("The zombie is not phased by your attack try something else!!")
        anothermove()
    elif another_move == "wait" or another_move == "WAIT" or another_move == "Wait":
        print ("As you wait you get caked in drool and your thoughts are drowned out by the snarling")
        time.sleep(2)
        print ("The zombie doesn't seem to tire but you start to lose your strength")
        time.sleep(2)
        print ("Before you know it your face it being torn apart")
        time.sleep(2)
        print ("GAME OVER!!!")
        # play_again = input("Play again? [Y/N] ")
        # if play_again == "Y" or "y":
        #     # start_game()
        # elif play_again == "N" or "n":
        #     print("I think someone is scared of losing again")
        # else:
        #     print("Get out of here!")
    
def next_event():
    time.sleep(3)
    print("As you turn onto the corridor you are knocked off guard by a solo zombie")
    time.sleep(2)
    print("The vile and hideous creature suddenly appears and jumps at you, pinning you to the ground ")
    time.sleep(2)
    print("There are only inches between your face and the zombies as your arm is the only thing stopping it from literally kissing you")
    anothermove()


def choice_run():
    print("You make a dash for it and as you approach the horde you realise this was a pointless choice")
    time.sleep(2)
    print("There is no turning back now, it is too late. You attempt to barge through the horde but before you know it...")
    time.sleep(2)
    print("You are lying on the floor being feasted on, entrails and guts everywhere...")
    time.sleep(2)
    print("Game Over!!!")

def choice_connect():
    print("You have managed to find a bluetooth speaker that is still switched on")
    time.sleep(2)
    print("A sigh of relief! You only have one song on your phone so you know time is of the essence")
    time.sleep(2)
    print("The song starts to play from the store and the horde become distracted and start heading towards the store")
    time.sleep(2)
    print("As you run around the back of the distracted crowd of zombies you run towards a corridor that you suddenly notice")
    next_event()
            
def chapter_three():
    print("As the adrenaline takes control you start to gain confidence and become less fearful and more aware of your surroundings") 
    time.sleep(1.5)
    print("Crouched behind a huge floral display your heart lowers as you start to gain control of your breathing")
    time.sleep(1.5)
    print("Around to the right you can hear nothing but snarls and growls as a horde of Zombies approach")
    time.sleep(1.5)
    print("To the left of you is an audio and hi-fi store")
    time.sleep(1.5)
    print("Time to make a decision. Do you . . .")
    time.sleep(1.5)
    print("Attempt to run and push through the horde or . . .")
    time.sleep(1.5)
    print("Try and see if you can connect to one of the store's speaker via bluetooth and distract the horde with music")
    time.sleep(1.5)
    
    
    run_or_connect = input ("What would you like to do? [Run/Connect]")
    
    if run_or_connect == "run" or run_or_connect =="Run" or run_or_connect == "RUN":
        choice_run()     
    elif run_or_connect == "connect" or run_or_connect == "CONNECT" or run_or_connect == "Connect":
        choice_connect()

number = random.randint(10, 20)

def chap_two_sect_four():
    answer_3 = input("Do zombies eat each other? \na. Yes \nb. No \nc. I don't know \n Answer: ")
    if answer_3 == "b" or answer_3 == "no":
        print("Correct")
        time.sleep(1.5)
        chapter_three()
    else:
        print("incorrect! The answer is no. ")
        time.sleep(1.5)
        print("Try again")
        time.sleep(1)
        print("\n")
        chap_two_sect_four()

def chap_two_sect_three():
    answer_2 = input("How do you kill a zombie? \na. Slapping them \nb. Pushing them\nc. Shooting their brain \n Answer: ")
    if answer_2 == "c" or answer_2 == "C" or answer_2 == "Shooting their brain" or answer_2 == "shooting their brain":
        print("Correct")
        time.sleep(2)
        print("\n")
        chap_two_sect_four()
    else:
        print("Incorrect! The answer is shooting their brain. ")
        time.sleep(2)
        chap_two_sect_three()


def chap_two_sect_two():
    time.sleep(1)
    print("Whilst running out of the first door in excitement, I see that there are stairs pointing to the exit.")
    time.sleep(2)
    print("I quickly climb the stairs and find another door.")
    time.sleep(2)
    print("Oh no! Not again, I am exhausted.")
    print("Boom! Multiple choice questions to escape appeared!")
    
    answer_1 = input("What do zombies eat? \na. Plants \nb. Human flesh \nc. Vegetables \n Answer: ")
    if answer_1 == "b" or answer_1 == "B" or answer_1 == "human flesh" or answer_1 == "Human flesh":
        print("Correct!")
        time.sleep(2)
        print("\n")
        chap_two_sect_three()
    else:    
        print("Incorrect! The answer is human flesh. ")
        time.sleep(2)
        print("\n")
        chap_two_sect_two()
        
def trial_error_guess():
    global number
    time.sleep(1)
    guess = int(input("Type a number between 10 & 20...Have a guess:"))
    if guess == number:
        print("You guessed right - the door is open.")
        time.sleep(1)
        chap_two_sect_two()
    elif guess > number:
        print("Your guess was too high.")
        time.sleep(1)
        print("Try again")
        trial_error_guess()
    else:
        print("Your guess was too low.")
        time.sleep(1)
        print("Try again")
        trial_error_guess()
def the_door():
    question = input("Do you want to open the door? [Y/N]:")
    if question == "n" or question == "no" or question == "N" or question == "NO":
        time.sleep(2)
        print("You have been bitten by a zombie. Game over!") 
        chapter_two()
    elif question == "y" or question == "yes" or question == "Y" or question == "YES":
        time.sleep(2)
        trial_error_guess()
def chapter_two():
    print("While I am resting and thinking about an escape route, zombies start walking towards me...  ")
    time.sleep(2)
    print("I turn around and they are approaching very fast, with their mouths wide open.  ")
    time.sleep(2)
    print("In a panic, I start looking around to find something to beat them up. ")
    time.sleep(2)
    print("Finally...! I see a fire extinguisher and spray them to give me time to escape. ")
    time.sleep(2)
    print("I look up and see a door with a code on it, asking me if i want to open the door. ")
    time.sleep(2)
    the_door()


def chap_one_q_two():

    print("It is now charging at full speed around the shopping centre - you need to find a good place to hide! Where do you hide?")
    time.sleep(2)
    print("A) Jump over the counter into the vegan restaurant in the food court.")
    time.sleep(1.5)
    print("B) In a dark store cupboard - well hidden!")
    time.sleep(1.5)
    print("C) You run into a costume shop hoping to find a disguise.")
    chap_one_q_two = input("[A/B/C] ")

    if chap_one_q_two == "A)" or chap_one_q_two == "a)" or chap_one_q_two == "A" or chap_one_q_two == "a":
        print("Great idea! No zombies in sight - they only eat meat, obvs.")
        chapter_two()

    elif chap_one_q_two == "B)" or chap_one_q_two == "b)" or chap_one_q_two == "B" or chap_one_q_two == "b" :
        print("Good idea for now, but how will you keep an eye out for zombies roaming? Try again.")
        chap_one_q_two()
    
    elif chap_one_q_two == "C)" or chap_one_q_two == "c)" or chap_one_q_two == "C" or chap_one_q_two == "c" :
        print("The costume shop was full of zombies trying on their own disguises! They surround you...GAME OVER!")
        start_game()

    else:
        print("Please try again.")
        chap_one_q_two()

def decision_function():
    decision = input()

    if decision == "A)" or decision == "a)" or decision == "A" or decision == "a":
        print("You escape from it- you're safe - for now. You head to the toilets to drink from the water fountain as you're parched.")
        chapter_two()

    elif decision == "B)" or decision == "b)" or decision == "B" or decision == "b":
        print("You manage to beat the zombie to the ground! Now run, fast!")
        chap_one_q_two()

    elif decision == "C)" or decision == "c)" or decision == "C" or decision == "c":
        print("You're stood there like an absolute lemon and become zombie chow. You are now dead.")
        start_game()
    else:
        print("You can try again - just this once!")
        decision_function()

def chap_one_q():


    print("Let us begin...............................")
    time.sleep(1)
    print("With a gasp of breath and your heart pounding a million miles an hour, you awaken.")
    time.sleep(1)
    print("Through blurred vision, you look across the shopping centre floor, expecting to see the usual crowds of people.")
    time.sleep(1)
    print("But instead, the place is empty and deafeningly silent.")
    time.sleep(1)
    print("Hoisting yourself off the floor, you head towards the automatic exit to your left.")
    time.sleep(1)
    print("But as you approach, you realise - to your horror - that the doors aren't opening.")
    time.sleep(1)
    print("You're trapped!!!")
    time.sleep(1)
    print("As you try to force them open with all your might, something even worse happens.")
    time.sleep(1)
    print("BEEEEEEEEP! BEEEEEEEEEP! BEEEEEEEEP!")
    time.sleep(1)
    print("The security alarms are set off. Oh god, what to do now?...")
    time.sleep(1)
    print("..But oh no, that's not all.")
    time.sleep(1)
    print("The sound of a strange gargling and growling is approaching from behind you, along with a nauseating smell of decomposing flesh.")
    time.sleep(1)
    print("The footsteps beating down towards you at a quickening pace compel you to turn around.")
    time.sleep(1)
    print("Quick, what do you do...?")

    for i in range(9, 0, -1,):
        time.sleep(1)
        print(i)
        time.sleep(1)

    time.sleep(2)
    print("You have three options. Do you:")
    time.sleep(2) 
    print("A) Run away as fast as you can?")
    time.sleep(1.5)
    print("B) Loot the sports shop and attack the zombie with a baseball bat?")
    time.sleep(1.5)
    print("C) Stand there paralysed with fear?")
    time.sleep(1.5)
    decision_function()

def start_game():
    print("Hello and welcome to the game.")
    time.sleep(1)
    global name
    name = input("What is your name?")
    time.sleep(1)
    print("Hello {}, it's so great to meet you.".format(name)) 
    time.sleep(1)
    response = input("Are you ready to play? [Y/N] ")
    if response == "Y" or response == "y":
        print("Great, let's go.")
        chap_one_q()
    elif response == "N" or response == "n":
        print("Then why are you playing here")
        start_game()
    else:
        print("Try again, I didn't recognise that.")
        start_game()
        
start_game()