# The script of the game goes in this file.

#choosable pronoun stuff

init python:
    def dpronouns(pronouns):
        global MCpronouns
        global Theyare
        global theyare
        global They
        global they
        global Them
        global them
        global Their
        global their
        global Themselves
        global themselves
        global People
        global people
        global verb
        global verbe
        global kid
        global Kid
        if pronouns == "she":
            MCpronouns = "she/her"
            Theyare = "She's"
            theyare = "she's"
            They = "She"
            they = "she"
            Them = "Her"
            them = "her"
            Their = "Her"
            their = "her"
            Themselves = "Herself"
            themselves = "herself"
            People = "Girls"
            people = "girls"
            verb = "s"
            verbe = "es"
            kid = "girl"
            Kid = "Girl"
            plural = False
        if pronouns == "he":
            MCpronouns="he/him"
            Theyare = "He's"
            theyare = "he's"
            They = "He"
            they = "he"
            Them = "Him"
            them = "him"
            Their = "His"
            their = "his"
            Themselves = "Himself"
            themselves = "himself"
            People = "Guys"
            people = "guys"
            kid = "boy"
            Kid = "Boy"
            verb = "s"
            verbe = "es"
            plural = False
        if pronouns == "they":
            MCpronouns = "they/them"
            Theyare = "They're"
            theyare = "they're"
            They = "They"
            they = "they"
            Them = "Them"
            them = "them"
            Their = "Their"
            their = "their"
            Themselves = "Themselves"
            themselves = "themselves"
            People = "People"
            people = "people"
            verb = ""
            verbe = ""
            kid = "kid"
            Kid = "Kid"
            plural = False
        return
        
    def cpronouns(sub, ob, poss, ref, plu):
        global MCpronouns
        global theyare
        global they
        global them
        global their
        global cpron
        MCpronouns = sub+"/"+ob
        if plu:
            theyare = sub+" are"
        else:
            theyare = sub+" is"
        they = sub
        them = ob
        their = poss
        themselves = ref
        cpron = True
        return
    
    def dgender(gender):
        global MCgender
        global person
        if gender == "guy":
            MCgender = "male"
            person = "man"
            sweetheart = "boyfriend"
            spouse = "husband"
            parent = "father"
        if gender == "gal":
            MCgender = "female"
            person = "woman"
            sweetheart = "girlfriend"
            spouse = "wife"
            parent = "mother"
        if gender == "nb":
            MCgender = "nonbinary"
            person = "person"
            sweetheart = "sweetheart"
            spouse = "spouse"
            parent = "parent"
        return

#declaration of characters

define DOE = Character("Deliah")
define ATF = Character("Andy")
define FBI = Character("Felicia")
define TSA = Character ("Tiffany")
define DOD = Character("Donna")
define EPA = Character("Lizzy")
define CIA = Character("Claire")
define FDA = Character("Frankie")
define NASA = Character("Nova")
define NSA = Character("Nayori")
define edwin = Character("Edwin")

#declaration of backgrounds

image bg blackscreen = "blackscreen.jpg"
image bg bus = "placeholder.png"
image bg campus1 = "placeholder.png"

#declaration of flags

default orientation = False
default andy = False

# The game starts here.

label start:

define MC = Character("[MC]")

python:
    MC = renpy.input("What is your name?")
    MC = MC.strip()

    if not MC:
         MC = "MC"

"What are your pronouns?"
label pronques:
menu:
    "What are your pronouns?"
    "He/Him":
        $ dpronouns("he")
        jump pronouns_done
    "She/Her":
        $ dpronouns("she")
        jump pronouns_done
    "They/Them":
        $ dpronouns("they")
        jump pronouns_done
    "Other Pronouns":
        $ pronquestion = True
        show screen bsub
        show screen bob
        show screen bposs
        show screen bref
        show screen cpron
        jump pronouns_done
label pronouns_done:
$ selpron = True
"Great! And what's your gender, again?"
menu:
    "Are you male or female?"
    "Male":
        $ dgender("guy")
        jump gender_done
    "Female":
        $ dgender("gal")
        jump gender_done
    "No":
        $ dgender("nb")
        jump gender_done
label gender_done:
$ selgen = True
"So your name is [MC], your pronouns are [MCpronouns], and you're [MCgender], right? Alright, let's go!"

label intro_1_1:
    
    scene bg blackscreen
    
    play music "Classroom.mov"
    
    "{i}Never thought I’d make it back here in time.{/i}"
    
    "{i}It’s really been a while since I was here again, huh...and now I’m back again.{/i}"
    
    "{i}Oh look, a random guy screaming at nothing. I’m starting to miss Japan.{/i}"
    
    "{i}Well, whatever I don’t have to worry about that for now. I know that mom and dad really wanted me to go to college in the states, but I don’t know if this is the right choice.{/i}"
    
    "{i}I mean, the friendships that I have here are more than likely gone; I even lost track of my best friend.{/i}"
    
    "{i}I don’t think that coming from Japan will improve my chances of getting a partner. At least in Japan some people were interested in foreign [people].{/i}"
    
    "{i}Ah, whatever. I’m thinking too much into this. It’s not like anything major will happen. Just go through college and move right back after.{/i}"
    
    "{i}God, the jet lag must still be lingering...{/i}"
    
    #need to make this emphasized or something
    
    scene bg bus
    
    with fade
    
    play music "Stress.mov"
    
    MC "{b}SHIT!!{/b}"
    
    MC "Missed my damn stop! {b}SIR CAN YOU STOP!?!{/b}"
    
    "Bus Driver" "I am sorry I can’t do that. I am legally not allowed to do that. You’ll have to wait until the next stop."
    
    MC "But I can’t be late for orientation!"
    
    "The bus driver sighs."
    
    "Bus Driver" "You know how many times I hear that this time of the year?"
    
    "Bus Driver" "Just settle in, kid. Next stop is only a five minute walk from the last."
    
    "Bus Driver" "{size=-10}Kids these days can’t walk...{/size}"
    
    MC "But there’s surely something you can do, right?"
    
    "Bus Driver" "No, now just sit your ass down and wait."
    
    "[MC] sighs and just sits down, shakes [their] head and waits for the next bus stop. [They] just hoped to make it in time."

    jump transition_1_1

label transition_1_1:
    
    scene bg campus1
    
    play music "Classroom.mov" fadeout 1.0 fadein 1.0
    
    MC "Well, shit, this school looks really nice, better than I was expecting."
    
    show doe sprite 1
    
    "{i}Huh. There is a girl there reading a shiny book...{/i}"
    
    "???" "Ay yo freshie! You just gonna stare at her or do something about it?"
    
    MC "Shit! Sorry! Was just spacing out."
    
    show doe sprite 1:
        
        xalign 0.5
    
        linear 0.5 xpos 1.5
    
    menu:
        
        "Chase after her.":
        
            jump doe_1_2
        
        "Keep going into the college.":
        
            jump un_1_2
            
label doe_1_2:
    
    play music "Stress.mov" fadeout 1.0 fadein 1.0
    
    "???" "Ahhhhh SHIT! [Theyare] doin’ it! Fuck yeah freshie! Get ‘em!"
    
    MC "Hey! Wait up!"
    
    MC "Like seriously! I swear I’m not a creep..."
    
    MC "As...I chase after you..."
    
    MC "Ah shit, I really am a creep. This isn’t a fucking visual novel. Real life doesn’t work like this."
    
    show doe sprite 1 at center
    with dissolve
    
    play music "Classroom.mov" fadeout 1.0 fadein 1.0
    
    "???" "Listen, I really just want to be left alone. Is that too much to ask?"
    
    MC "Well, no. I just wanted to...I don’t even know. I guess I was curious. Not in a bad way! Ugh, I’m messing this up."
    
    "???" "Uh huh."
    
    MC "Anyways, I’m [MC]. Sorry we had to meet in such an awkward way."
    
    DOE "I’m, uh, Delilah. I’m just gonna...leave now..."
    
    hide doe sprite 1

    MC "Alright. I guess I’ll see ya ar...and you’re gone. Cool."
    
    "{i}Where was the orientation?{/i}"
    
    jump un_1_3_2
    
label un_1_2:
    
    "{i}Ah, whatever. She’ll probably forget about it soon enough.{/i}"
    
    "???" "Damn! Should’ve chased her a little, if ya know what I mean."
    
    show atf sprite 1
    with dissolve
    
    "{i}I never thought I would see the stereotypical Texan here at this college. He has the Texan accent, the friendliness, and the—OH GOD IS THAT AN EXPLOSIVE JUST STUCK IN HIS POCKET?? HOLY SHIT THE FUSE IS LIT OH MY FUCK I’M GONNA DIE HELP—"
    
    "???" "Oh, this little thing? Don’t worry, partner. It won’t hurt you."
    
    "{i}Did he just...pinch it away with his fingers. Okay. Cool.{/i}"
    
    "???" "First days are always boring. Just ditch orientation. You’ll learn all of it along the way!"
    
    menu:
        
        "Accept his offer.":
            
            jump atf_1_3
            
        "Decline his offer.":
            
            jump un_1_3_1

label atf_1_3:
    
    "{i}Eh, what more could I lose?{/i}"
    
    "{i}Yup, that smile was big and flashy.{/i}"
    
    ATF "You got some real guts for a freshie. I’m Andy. Nice to meet ya!"
    
    MC "[MC]. Same with you."
    
    ATF "Well, [MC], how ‘bout I show you around and cut the 30 minute orientation to 30 seconds?"
    
    ATF "That’s the college buildings. That’s the office. Those are the dorms. Food’s over there."
    
    ATF "Also, don’t tell anyone this, but if you turn the corner and walk deeper, that’s the place where you can get some real good stuff, if ya know what I mean. Trust me, I know."
    
    "{i}Maybe I should’ve gone to the orientation. This campus is impossibly huge.{/i}"
    
    MC "O-Okay..."
    
    ATF "Well, I got some shit to go to. See ya soon!"
    
    MC "See you."
    
    hide atf sprite 1
    
    jump un_1_4_2
    
label un_1_3_1:
    
    "{i}I don’t really wanna cause any more trouble than I already did.{/i}"
    
    MC "Thanks, but I’ll skip on the offer."
    
    ATF "Guess freshies really are timid. I’m Andy. See ya ‘round."
    
    hide atf sprite 1
    
    "{i}He didn’t even ask for my name...{/i}"
    
    "{i}Whatever. Time to hurry to the auditorium. I can’t go through all of this and still be late.{/i}"
    
    jump un_1_3_2
    
label un_1_3_2:
    
    "{i}I still don’t know where the auditorium is for the orientation. I suppose wandering will eventually get me to where I need to go...{/i}"
    
    show fbi sprite 1
    with dissolve
    
    "???" "Hey kid, you need any help? Pretty sure the freshmen are supposed to be in the auditorium by now."
    
    "{i}Bingo!{/i}"
    
    MC "Oh yeah. Got lost a bit ago. Wish I had a map, this college is huge."
    
    "???" "I can show you the way there. Should be a door somewhere around here..."
    
    "???" "Ah! There it is. So whatcha studying?"
    
    MC "Oh just some useless degree. Nothing too interesting. "
    
    MC "The way the current recession is facing, the jobs I’m looking at are disappearing, and quickly. No one has time to be spending money where it would help. I’ll likely end up like all my friends, some low life factory technician. It’s not desirable, but what can I do in the face of fate."
    
    "???" "You could do plenty of things to spit in fate’s face!"
    
    "???" "There are still a plethora of jobs still needed! Politicians, policemen and women, hell, if worst comes to worst you can at least do some landscaping."
    
    "[They] laugh[verb]."
    
    MC "That's not funny!"
    
    menu:
        
        "Where you from?":
            
            jump fbi_1_4
            
        "What're you studying?":
            
            jump un_1_4_1
            
label fbi_1_4:
    
    "???" "Just some rural town about a two hour drive from Chicago."
    
    "{i}Huh. Me and my childhood best friend used to live in a similar area.{/i}"
    
    "{i}She has the black hair, same nose.{/i}"
    
    "{i}This couldn’t be her. She’s so old. Aaaand so many people have black hair.{/i}"
    
    "???" "I do miss it sometimes though. The way the creek by my house would freeze up almost the same time each year was a spectacle."
    
    "{i}The mannerisms are just right, she still carries herself the same way. Only one way to know...{/i}"
    
    MC "Felicia?"
    
    FBI "I don’t think I told you my name...?"
    
    MC "Holy crap it really is you! I’m [MC]! How long has it been?"
    
    FBI "[MC]? I thought you went to Japan?!"
    
    MC "I did! My parents sent me back for college. I never thought I’d see you again after..."
    
    FBI "After you forgot to get my phone number, dummy!"
    
    FBI "I know you are supposed to go to the orientation...but they’ll give you a lot of useless information, and try to get you roped in on some boring club. I’ll give you the tour myself."
    
    MC "I don’t want to steal your ti-"
    
    FBI "Oh please. I’m losing my mind to boredom. Besides, I don’t know if I’ll be able to hear all about Japan anytime else!"
    
    jump fbi_1_5
    
label un_1_4_1:
    
    "???" "Same as everyone else: some useless degree. Hoping it’s something that I don’t hate, but like you said, not many people are spending money like they used to."
    
    "???" "Anyways, this is the auditorium. We’ll have to meet up some time, you remind me of someone I once knew."
    
    MC "Yeah, we have to! Thanks for chatting!"
    
    hide fbi sprite 1
    with dissolve
    
    jump un_1_4_3
    
label un_1_4_2:
    
    $ andy = True
    
    "{i}He just left me standing here all by myself like an idiot. What am I supposed to do for the rest of the 29 minutes and 30 seconds?{/i}"
    
    show atf sprite 1
    
    ATF "What, are ya still standing there?"
    
    MC "What else am I supposed to do?"
    
    ATF "If ya really have nothin’ to do, just go back to the damn orientation!"
    
    MC "But I’m already la-"
    
    ATF "You’re welcome! Bye!"
    
    hide atf sprite 1
    
    "{i}Great. All I did was miss the important parts of orientation. I should catch up before I miss out on even more.{/i}"
    
    jump un_1_4_3
    
label un_1_4_3:
    
    $ orientation = True
    
    "{i}Well, that was a whole lot of info.{/i}"
    
    "{i}Where did they say the science building is?{/i}"
    
    "{i}I should have gotten coffee this morning.{/i}"
    
    show tsa sprite 1
    with dissolve
    
    "???" "Um, do you need help?"
    
    MC "Yeah, kinda..."
    
    "???" "The orientation usually isn’t enough for super new students. Here, I have a relatively good memory, so I can show you where your classes will be if you want."
    
    menu:
        
        "Accept her offer.":
            
            jump tsa_1_5
        
        "Decline her offer.":
            
            jump un_1_5
            
label tsa_1_5:
    
    "{i}I definitely need that. I’m probably more of a hands on learner.{/i}"
    
    MC "Yeah, that would be great. Thanks."
    
    "???" "No problem! I always see people wandering around and confused because of the large campus. Don’t worry, I’m always here to help if you need it!"
    
    "???" "Hmm...looks like your first class isn’t too far, it’s just there around the corner. After is a lunch break, so feel free to do whatever you want. The cafeteria is that building on the left, if you wanna buy something from there. Next is in that building upstairs."
    
    "???" "After is a little farther, in the corner of the office building on the left and the library on the right. Your other three classes are there, there and there. Oh yeah, it’s the first day. Then you’ll have three classes, a lunch break, then your other three classes, but for the rest of the days it switches off."
    
    TSA "Wait, did I not introduce myself? Oops. I’m Tiffany. Nice to meet you!"
    
    MC "Nice to meet you, too. I’m [MC]. Thanks a lot for helping me."
    
    TSA "Don’t mention it, [MC]! See you around!"
    
    MC "See you!"
    
    hide tsa sprite 1
    with dissolve
    
    "{i}Well, it looks like I finally have a clearer plan of where I’m going. I better head to the dorms and figure out the housing situation.{/i}"
    
    jump un_1_8
    
label un_1_5:
    
    if orientation:
        
        "{i}I just went through the orientation though...I don't think I need to go through it again.{/i}"
        
    if andy:
        
        "{i}Also, after giving Andy the benefit of the doubt, I don't think I should take another chance.{/i}"
        
    MC "Thanks for your offer, but I think I can figure it out on my own. Practice makes perfect, right?"
    
    "???" "Okay! Good luck!"
    
    hide tsa sprite 1
    with dissolve
    
    "{i}Hmm...I believe it’s time to go to the dorms. Let’s see if I can find it.{/i}"
    
    jump un_1_8
    
label fbi_1_5:
    
    "{i}It was awesome that I managed to bump into Felicia again four years after we parted ways.{/i}"
    
    FBI "Well c’mon! Lemme see your schedule!"
    
    FBI "Hmmm. Looks like I’m TA for your American History class, which is right over there..."
    
    FBI "Why the hell are you taking astronomy? Unless you’re actually planning to use it?"
    
    MC "Maybe I will!"
    
    FBI "Uh huh. Either way, it’s a good hike out over...hmmm...there!"
    
    FBI "Do you have any idea where I am pointing?"
    
    "{i}No.{/i}"
    
    MC "Yeah, right over there."
    
    "Felicia nudges [their] arm to the left a little."
    
    MC "See! I got this!"
    
    FBI "Alright. C’mon. I’m taking you to your classes."
    
    "They start walking off. A moment of silence passes."
    
    MC "So how’s life been?"
    
    FBI "I suppose I should fill you in on what’s been happening."
    
    "{i}She seems to have gotten very serious...{/i}"
    
    MC "What do you mean?"
    
    FBI "I’m...well. It’s...it’s a little difficult to say."
    
    FBI "I'm...I'm..."
    
    FBI "Totally messing around. Life has been as life is in the Midwest, totally boring."
    
    FBI "A few boyfriends have been and gone, nothing good."
    
    FBI "Mom and Dad are the same great as always."
    
    MC "Sounds...actually pretty nice."
    
    FBI "Eh. I’d prefer Japan!"
    
    MC "Well, seeing as we got the ti-"
    
    show fbi sprite 1:
        xalign 0.5
        linear 0.2 xpos 0.85
    
    show dod sprite 1 at center
    show epa sprite 1 at left
    
    "??" "Ahk! Why the {i}fuck{/i} are ya always tryin to prove yourself?!"
    
    "???" "You want me to prove myself?"
    
    "??" "NO! Just leave! Nobody wants ya ‘round here!"
    
    "???" "You gonna try and move me?"
    
    FBI "Ugh. Donna is going at Lizzy again."
    
    MC "Donna?"
    
    FBI "Yeah, she never grew out of middle school, still acting like a bully."
    
    MC "Why don’t we put a stop to it?"
    
    FBI "Pff! You can! I’m not going in there...{size=-10}Not right now anyways...{/size}"
    
    hide fbi sprite 1
    with dissolve
    
    menu:
        
        "Try to stop the fight.":
            
            jump dod_1_6
        
        "Go back to history with Felicia.":
            
            jump un_1_8

label dod_1_6:
    
    play music "Stress.mov"
    
    "{i}Oh dear lord, what did I get myself into?{/i}"
    
    menu:
        
        "Pull out.":
            
            DOD "Uh oh! Looks like fresh meat!"
            
        "Interfere for Lizzy.":
            
            DOD "Uh oh! Looks like fresh meat!"
    
    DOD "You wait here, {i}friend{/i}. I'll be back."
    
    hide epa sprite 1
    with dissolve
    
    "{i}Shit! Looks like I have no choice in the matter. Better think of something quick...{/i}"
    
    MC "Fresh meat? Is that really what you are rolling with?"
    
    DOD "Doesn’t look like you deserve better."
    
    MC "Looks like you are too lazy to think of anything better."
    
    DOD "HA! You’re good. I’ll give ya that. But...words only get ya so far..."
    
    "Whap!"
    
    #if you noticed there's a tiny gap where donna doesn't appear after the flash to black. idk if it's a problem w my coding but i tried putting the show command before the flash but she just doesn't show up. pls help.
    
    scene bg campus1
    with Fade(.1, 0, .1, color="#000")
    
    show dod sprite 1
    
    "{i}I’m way out of my league, but I’m not going down without a fight!{/i}"
    
    menu:
        
        "Swing left.":
            
            jump epacia_1_7
        
        "Swing right.":
            
            jump fda_1_7
            
label epacia_1_7:
    
    "Crack!"
    
    "Donna's aviators go flying."
    
    "{i}I actually hit her!{/i}"
    
    DOD "That all you got?"
    
    "She retrieves her sunglasses."
    
    DOD "I’ll admit you’re quick...but, you might want to work on actually hitting hard."
    
    DOD "For example-"
    
    "Whap!"
    
    scene bg campus1
    with Fade(.05, 0.5, .05, color="#000")
    
    show dod sprite 1
    
    DOD "Or..."
    
    "Whap!"
    
    #idk how to code the black around the screen sorry (black lingers around the side of the screen)
    scene bg campus1
    with Fade(.05, 0.5, .05, color="#000")
    show dod sprite 1
    
    DOD "Last, but far from least..."
    
    "Whomp!"
    
    #idk how to code this either (black screen slowly fades, still lingering around the edges)
    scene bg campus1
    with Fade(.05, 0.5, .05, color="#000")
    show dod sprite 1
    
    DOD "Good hustle though. I'll be seeing you."
    
    hide dod sprite 1
    with dissolve
    
    MC "Aghhhh..."
    
    show epa sprite 1 at center
    
    "??" "Damn! Ya took a good lickin'!"
    
    "??" "C'mon, get up."
    
    EPA "Name’s Elizabeth. Though, since ya did save me, I ‘pose you could call me Lizzy."
    
    MC "Ohhh...I-"
    
    EPA "Oh right! Let me show ya where the nurse’s office is."
    
    "After hobbling towards the main office, the nurse runs out."
    
    "Nurse" "Whatchu doin' gettin' in a fight with Donna? You crazy [kid]?!"
    
    "She pulls [their] head side to side a little to see how bad it is."
    
    "Nurse" "Huh. Looks like you got off well. Too well. I’d be watching my back if I were you."
    
    EPA "[They] came when [they] heard yellin'."
    
    "Nurse" "Uh huh."
    
    "Nurse" "Here, kid, an ice pack. That’s all I’m really ‘llowed to give."
    
    "The nurse retires back to office, mumbling something about staying for the degree."
    
    EPA "What’s ya name?"
    
    MC "I-"
    
    "[They] clear[verb] [their] throat."
    
    MC "I'm [MC]."
    
    EPA "Thank ya [MC]. Why’d ya do that? I’ve dealt with her before. She ain't that bad once ya confront her once or twice...or three times..."
    
    MC "Instinct, I guess. I hear yelling, I start moving."
    
    show cia sprite 1 at left
    with dissolve
    
    "Another girl walks forward."
    
    "???" "I saw what happened. Here, take this, it’d probably help with the pain."
    
    MC "Probably?"
    
    EPA "I ain't givin' [them] drugs."
    
    "???" "Ibuprofen?"
    
    EPA "Oh. Here ya go."
    
    MC "Uck! I'm fine."
    
    EPA "No ya ain't."
    
    "She quickly plops the pill into [their] mouth. It didn't taste right. [They] spit[verb] it out."
    
    MC "Seriously. I'm fine."
    
    MC "A little headache never hurt anyone."
    
    "???" "Well, technically..."
    
    MC "Shh! I'm doing fine."
    
    "???" "Fine and great are not the same thing."
    
    MC "I just got punched out. I don’t think much is going to help me past 'fine.'"
    
    "???" "The ibuprofen would."
    
    MC "Why do you want me to take this drug so badly? I don’t even know your name!"
    
    CIA "Well, you seem smart enough. I’m Claire. It is a pleasure to meet you."
    
    MC "[MC]...?"
    
    EPA "Wait? Those actually were-"
    
    CIA "Easy Lizzy. You know I wouldn’t do any long term damage."
    
    MC "What is even happening today? Bombs, fighting, drugs!"
    
    EPA "That ain’t even the start of it!"
    
    MC "That doesn’t help me at all!"
    
    CIA "If it makes you feel better, only one person has been killed here. Security is tight as far as that goes."
    
    MC "Ha! {i}Only{/i} one?"
    
    EPA "Oh, hush! It could be worse."
    
    EPA "Anyways...Ya should probably start to ya dorm."
    
    MC "Right...I guess it was...an experience meeting you guys."
    
    EPA "Thanks!"
    
    CIA "See you around."
    
    jump un_1_8
    
label fda_1_7:
    
    "[They] swing[verb], but doesn't hit anything."
    
    DOD "Aw, the baby doesn’t know how to fight?"
    
    DOD "Sadly for you, I don’t go easy on babies."
    
    "Whap!"
    
    #help (black lingers around the sides of the screen)
    scene bg campus1
    with Fade(.05, 0.5, .05, color="#000")
    show dod sprite 1
    
    DOD "What, backing out now?"
    
    "Whomp!"
    
    #someone pls (black slowly encroaches into the middle of the screen)
    scene bg campus1
    with Fade(.05, 0.5, .05, color="#000")
    show dod sprite 1
    
    DOD "Come on, not even gonna last enough for me to have some fun?"
    
    DOD "Ugh, fine. I'm done with this."
    
    show fda sprite 1:
        xalign 1.0
        linear 0.4 xpos 1.0
    
    "???" "HEY!"
    
    DOD "Ah, shit."
    
    "???" "What the FUCK are you doing to Lizzy?!"
    
    show epa sprite 1 at left
    with dissolve
    
    EPA "I’m fine, Frankie. She ain’t done nothin’ to me."
    
    DOD "Lizzy's right. I was just talking with her."
    
    FDA "Leave her the fuck alone, bitch."
    
    "She glances at [them]."
    
    FDA "And leave [them] out of it, too."
    
    DOD "Whatever. I won’t be so nice next time I see you."
    
    hide dod sprite 1
    with dissolve
    
    hide epa sprite 1
    with dissolve
    
    show fda sprite 1:
        xalign 1.0
        linear 0.4 xpos 0.75
    
    FDA "You alright?"
    
    "{i}She’s probably talking to Lizzy. They seem very close.{/i}"
    
    "{i}Oh shit. She’s looking at {/i}me{i}.{/i}"
    
    MC "Oh, uh, yeah."
    
    "She stares at [them] again."
    
    FDA "I guess that’s why you got into a fight with Donna. Airhead."
    
    "{i}I’m just gonna let that slide.{/i}"
    
    MC "Thanks for helping me."
    
    FDA "No problem. Even though you’re dumb, you do have some guts to stand up."
    
    "{i}Should I be offended…?{/i}"
    
    FDA "I'm Frankie."
    
    MC "[MC]."
    
    FDA "How bad is it this time, Lizzy?"
    
    "Lizzy was already in the far distance just rounding the corner of the school."
    
    "She sighs."
    
    FDA "Of course she went somewhere again. That’s my sis for you."
    
    MC "You two are siblings?"
    
    FDA "What, surprised? Yes, stupid, she’s my adopted sister."
    
    MC "Alright..."
    
    "She glances away from [them]."
    
    FDA "Anyways...Time is money, and you are a waste of both. Bye."
    
    hide fda sprite 1
    
    MC "Hey wait a sec!"
    
    "{i}And she left. That was weird.{/i}"
    
    "{i}I should check out my dorm room before getting my stuff out of the rental car.{/i}"
    
    jump un_1_8

return
