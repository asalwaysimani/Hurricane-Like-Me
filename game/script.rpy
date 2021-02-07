# The script of the game goes in this file.
init python:
    mp = MultiPersistent("HurricaneLikeMe.renpy.org")

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.

transform eir_moodletbounce:
    block:
        xpos 150
        ypos 600
        linear .175 yoffset -10
        linear .175 yoffset 0
        linear .175 yoffset -4
        linear .175 yoffset 0
        yoffset 0
        repeat 5

label start:

    $ Mood_Happy = 0
    $ Mood_Focus = 0
    $ Mood_Hungry = 0
    $ Mood_Chill = 0
    $ Mood_Sleep = 0
    $ Mood_Panic = 0
    $ Mood_Stress = 0
    $ Mood_Embarrassed = 0

    $ RelationshipCW = 0
    $ RelationshipJade = 0

    if Mood_Chill >= 1:
        show ewChibi neutral with eir_moodletbounce

show bg rose with w12
pause (.5)
show text "{size=40}Preface{/size}" at truecenter with Pause (4)
hide text with dissolve
hide bg rose with w12
pause (1)
scene bg rose

#show screen moodpointdisplay

show Troy Happy at right

# These display lines of dialogue.
tc "So this is they story of me, Troy Colby, and the time I tried to do the right thing and still got stuck literally holding the bag."                               

show Eir Angry at left

ew "Now wait a second there Troy!"
tc "This is Eir, she's the main character of this game."

ew "Thats right I'm the main character so why are you here doing the intro?"
tc "Because you were late, we were supposed to start this ten minutes ago."

show Eir Embarrassed at left

$ Mood_Embarrassed += 1

ew "Ek, no we were supposed to start when I got here!"

show Troy Bored at right

tc "Which, you know what never mind. We're here we're starting this."

show Troy Happy at right

tc "Welcome to Hurricane Like Me."

show Eir Happy at left

ew "A visual novel written for Summer Novel Festival 2018."
tc "Please keep in mind this was our first visual novel so there are some kinks to work out."
tc "In fact any and all feedback is welcomed."
ew "Our creator even made a handy dandy feedback form on the bottom in the menu"

tc "In theory this demo is about fifiteen minutes long depending on reading speed."

ew "We hope you enjoy this peek at {i}Hurricane Like Me{/i}"
#Add more thanks here from the people who helped me build this. Semi similar to credits at the end
show Eir Happy at left
tc "Okay, enough chatter from the two of us, onto the game!"
hide Eir
hide Troy

label Prelude:
#show screen invdisplay

show bg grey with w12
pause (1)
show text "{size=40}Prelude{/size}" at truecenter with Pause (4)
hide text with dissolve
hide bg grey with w12

#INT. EIR’S APARTMENT, DAY - FRIDAY
scene EirBedroomDay
play sound alarmclockcaw

"The alarm clock goes off with a cruel consistency, and Eir groans underneath her blankets."

"Beep beep beep."

ew "Please, please be quiet."

show Eir Tired PJs at left

"Her pleas don’t matter though, not to this demon of a clock. She removes her hand from a nest of blankets to slap the alarm clock into submission."

ew "Five more minutes, please just five more"

"She can totally afford five more minutes."

"...Right?"

"The alarm clock says otherwise, continuing to beep despite her groans and hits."

ew "Argh, what time even is it?"

"She slaps around on her table for a few seconds until she finds her phone, pulling it into the blankets with her."

"It’s 8:15 in the morning."

show Eir Panic at left

$ Mood_Happy -= 5
$ Mood_Focus += 9
$ Mood_Chill -= 10
$ Mood_Panic += 8 

"She has a forty-minute commute and it’s 8:15"

show ewChibi panicked at topleft
show screen thought ("Oh god, shit. Oh my god, shit.")

"For a moment she contemplates if she really needs a job."

"And then she is up and ready to go."

hide screen thought
hide ewChibi

play sound WakeUpWalla

"She rushes into the closet,"

"Moving past the piles of clothes, and finally digging through her shoes. She takes a glance at the outfit she prepared on hanging on the back of her bedroom door. Black shoes will do. She digs out a pair."

show Eir Work NReutral at center
ew "{i}Okay, I have this in the bag{/i}"

"She stumbles through the stray shoes and clothes, grabbing a book from her End Table Of Books™. Pausing to make her hair presentable before rushing out the door."

$ Mood_Happy += 7
$ Mood_Chill += 10
$ Mood_Panic -+ 8

$ workbag.add_item("Phone")
$ workbag.add_item("Laptop")
$ purse.add_item("Planner")

"Then, the daily grind begins."

hide Eir

############################INSERT OPENING CG HERE################################

#Eir sitting on the train, she is reading and listening to music. Her head is down and she isn’t paying any mind to anyone else on the train. The train isn't very crowded, with plenty of space for everyone to stand or sit if they choose. At the opposite end of the train is Troy standing in his bike messenger outfit also with headphones on, bike leaning against the train wall. He is leaning on his bike, standing bopping his head to his music. The train hurtles down the tracks.#

##################################TITLE GFX HERE##################################

show bg black with w33
pause (1)

#INT. EIR’S OFFICE, DAY FRIDAY
scene EirOfficeDay

show text "{size=+50}{font=fonts/CaviarDreams_Bold.ttf}9AM{/font}{/size}" at top with Pause (10)
hide text with dissolve

show Eir Work at left
"She arrives at the office exactly on time. Which given that she had to ride mass transit it is a testament to her time management skills."

"Smoothing her jacket down, she unshoulders her bag and makes her way to her cubicle."

"She has the Sheen Project to work on today, which honestly might take her all day to do."

"However, she is waylaid before she even makes it there. "

show cwPete at right

menu:
    cwPete "Eir! Would you mind helping with this here?"

    "Help, visibly happy to help":
        ew "Of course I can help! Give me one second!"
        "Eir isn’t actually in a helpful mood, but it’d be better to play the part."
        
        $ Mood_Stress += 5
        $ Mood_Sleep -= 2
        $ Mood_Focus += 1
        $ RelationshipCW += 3

        "She looks at Pete’s desk and gives in depth feedback. She makes sure to smile the entire time, and answers his follow up questions to the best of her ability."

    "Help, is visibly grumpy about it":
        "If Pete weren’t so close, Eir would’ve cussed under her breath."

        $ Mood_Happy -= 5
        $ Mood_Focus += 1
        $ Mood_Chill -= 5
        $ Mood_Sleep += 2

        ew "Of course!"

        show Eir Work Intense at left
        
        "She looks over Pete’s design and gives some quick feedback. She doesn’t even remember what she’s saying, but she makes sure to leave with a smile before heading to her desk finally."

        $ RelationshipCW -= 1

    "Help, is annoyed and snappish about it":

        "Eir definitely cusses under her breath loud enough for Pete to hear. She’s annoyed out of her mind right now, and can’t help showing it."

        ew "Okay, will do"

        show Eir Work Agitated at left

        "Eir grumbles as she looks over Pete’s design. Her feedback is short and curt. She leaves as quickly as she can, ignoring Pete’s frustrated look."

        $ RelationshipCW -= 3

hide Eir
hide cwPete

"She’s about an hour into her work when she’s disrupted again."

show Eir Work Neutral at left

show ewChibi deadpanned at topleft
show screen thought ("Okay, the Sheen projects needs to be ready by 10 am Monday, but I want to turn it in today. For the--")

show cwCallahan at right

cwAubrey "Excuse me Eir?"

show ewChibi panicked at topleft
show screen thought ("{i}Ugh{/i}, not Aubrey again.")

$ Mood_Happy -= 2
$ Mood_Chill -= 2
$ Mood_Sleep += 2

show Eir Happy

hide screen thought
hide ewChibi

ew "Yes? What's up, can I help you with anything?"

cwAubrey "Could you deal with the Johnsons? They’re outside."

ew "Sure! I’ll be right there."

menu:
    "Help, visibly happy to help":
        ew "Hey, how are you doing? I’m so glad to see you today."
        
        "Eir is lays it on thick, which is frustrating. But the Johnsons leave satisfied. Aubrey doesn't help in the slightest, but they seem relieved when she walks out unschathed."

        $RelationshipCW += 3

    "Help, is visibly grumpy about it":
        "Eir shoots an annoyed glance at Aubrey before going to speak with the clients. After a quick chat with the Johnsons and no help from Aubrey, Eir thinks she did okay. However, she can’t help being snappish at Aubrey as she comes back."

        $RelationshipCW -= 1

    "Help, is annoyed and snappish about it":
        ew "Hello, what brings you in today?"

        "Eir barely manages to hold onto professionalism as she talks to the Johnsons. When she finishes her chat, she’s even more annoyed than she was before."

        "She glares at Aubrey and mouths {i}helpful much?{/i} when they make eye contact as Eir passes to return to her desk."

        $RelationshipCW -= 3
        $ Mood_Happy -= 5

hide cwAubrey
hide Eir

"After a quick chat with the Johnsons, and no help from my coworker, I return to my desk."
show ewChibi deadpanned at topleft

show screen thought ("Sheen project, I’m coming for--")
hide screen thought
hide ewChibi

show cwCallahan at right #Panic

cwCallahan "Eir? Oh thank god you’re here!"

show Eir Work Panic at left

ew "What is it?"

cwCallahan "I think I accidentally deleted a file for the Mendes drafts, could you come check?"

show ewChibi panicked at topleft
show screen thought ("{i}Oh you’ve got to be kidding me.{/i}")

show Eir Work Happy

ew "I’m happy to help! Just let me drop this at my desk real fast"

show ewChibi angry at topleft
show screen thought ("I’m not happy to help.")
hide screen thought
hide ewChibi
    
menu:
    "Help, visibly happy to help.":

        show Eir Intense

        "Her face says that she is happier to help than she really is. She recovers the file that has actually been deleted, {b}surprise surprise{/b} before getting back to her cubicle in record time."
        
        $RelationshipCW += 3
    
    "Help, is visibly grumpy about it":

        show Eir Tired

        "She’s not happy to help. She manages to recover the file, which shockingly has actually been deleted and power walk to her cubicle before Callahan can say anything else to her, her face set in a soft confused frown."

        $RelationshipCW += 1
    
    "Help, is annoyed and snappish about it.":

        show Eir Agitated

        "She narrows her eyes at Callahan. Eir can’t believe he’d be so incompetent when she needs all her coworkers to just mind their own business. She recovers the file wordlessly, and storms back to her cubicle."

        $RelationshipCW -= 3

hide cwCallahan

show Eir Work Neutral

"But she manages to recover the files and power walk to her cubicle without too much trouble."

"She takes a quick glance at the clock, then around to see if anyone needs her help. {i}better safe than sorry{/i}"

"She sighs in relief when she sees no one staring too hard at her desk or even in her general direction, and finally gets to work."

hide Eir

show bg black with w33
pause (1)

scene EirOfficeAfternoon
show text "{size=+50}{font=fonts/CaviarDreams_Bold.ttf}5:30 PM{/font}{/size}" at top with Pause (10)
hide text with dissolve

show Eir Work Happy at left
"Her jaw cracks a little as she yawns."

#SFX: YAWN

"She flexes her toes in her shoes, they crack a little as well."

"Glancing at her computer clock,"

show screen thought ("Thirty minutes until quitting time.")


"She thinks to herself. And then it’s the weekend. The glorious, glorious weekend."

hide screen thought

show cwAubrey at right
cwAubrey  "Eir, Ms Logan needs you in her office. She asked for you by name again."

$ Mood_Chill -= 5
$ Mood_Panic -= 5

show Eir Panic

#SFX: POOF

"And poof! There go Eir’s dreams of leaving on time today."

show Eir

ew "One second, just saving my work."

"She quickly saves and closes her work, giving the clock on her desktop computer one more longing glance before collecting her laptop."

"She rolls her shoulders once, then twice, then puts on her best ‘How can I help you face’ and heads towards Ms. Logan’s office."

show Eir Happy
hide cwAubrey
hide Eir

show bg black with w33
pause (1)

#INT. JADES OFFICE

scene IntJadeOffice #Needs to be changed to evening variate of this background

show Jade VHappy at right
show Eir Work Happy at left

jl "It’s good to see you Eir!"

"Jade Logan waves at Eir from her desk."

ew "It’s good to see you too Ms. Logan. How are you?"

jl "I’m doing well. How are you doing? Did I take you away from anything too pressing?"

"Eir shakes her head."

ew "Nothing since I finished the Sheen project."

show Jade Intense

"Jade perks up at that."

jl "You finished already?"

show screen thought ("Oh god, Is that a good thing or bad thing????")
show ewChibi panicked at topleft
show Eir Confused

ew "Yeah I did."

jl "May I see it?"

hide screen thought
hide ewChibi

"Eir’s grateful she brought her laptop for this impromptu meeting. Jade’s friendly, but tends to keep people on their toes. Eir wants to make sure she has it together at all times."

"Eir to the other side of Jade’s desk and opens her laptop. After she pulls up the Sheen project, Eir places her laptop in front of Jade and takes a step back."

jl "Thank you."

"Jade is quiet except for a few hums. She nods to herself as she scrolls, and Eir tries to subtly look over Jade’s shoulder."

show Jade Neutral

jl "This is great."

"Jade looks up at Eir and smiles. Eir can’t help being surprised at that. Jade has her business smile for clients, and one for her subordinates that’s a little more clipped, but this smile is different somehow."

show Jade Intense

jl "Say, would you like to work on something larger? It’s a bit of a rush job though, and you’d have to have it in to the client by Tuesday and give me Monday to skim through it."

"Eir freezes. This is a great career opportunity, but she’d basically have to work all weekend to get it done. She ponders for a moment. Jade has never asked Eir for something like this before. She’s gotta take this chance."

ew "Yes! I'd do it!"

"Jade nods before extending her hand. Eir takes it, and they shake hands."

jl "Good to hear. I’m expecting something fantastic."

show ewChibi panicked at topleft
$ Mood_Panic += 5

"Eir laughs at that. She hopes Jade can’t tell how nervous she is."

ew "I’ll do my best."

hide ewChibi

"As Eir walks out of Jade’s office, she thinks her best will have to be good enough."

show bg black with w33
pause (1)

#INT. EIR’S APARTMENT, NIGHT - FRIDAY
scene EirBedroomNight

show Eir Work

"The second she closes the door her shoes are off. Kicked into a heap just out of the doorway. Just as quickly she dumps her bag, then makes a beeline for her bedroom."

$ workbag.remove_item("Phone")
$ workbag.remove_item("Laptop")
$ purse.remove_item("Planner")

"In a flash, her work clothes have joined the pile and she is comfortably back in her house wear"

show Eir PJs Happy

$ Mood_Happy += 5
$ Mood_Hungry += 5
$ Mood_Chill += 7
$ Mood_Sleep += 2
$ Mood_Panic -= 8
$ Mood_Embarrassed -= 1

"She zooms back to the front door and fishes out her phone from her bag juggling both too large her work and personal phone in her small hands."

#SFX Footfalls on woodfloor

"The work phone goes straight onto the side table to charge while she pockets her own phone."

ew "God I don’t know how I did it!"

"She grabs a bag of chips to snack on as she lays on her bed, exhausted. And there is still work tomorrow, one weekend no less!"

"She can handle work fine when she’s there, but everything else seems to screw itself up the second she leaves the office."

"She looks around her apartment, it is kind of a mess. There is a pile of pens on the floor, several sheets of paper she had been working on laying about, a blanket and pillow in heap in front of the couch, gods when was the last time she really cleaned?"

$ Mood_Happy -= 3

ew "I wish I could manage things a little bit easier. Even get some help."

"If she made a just a little bit more money, she’d even consider a maid service. But that’s a pipe dream right now."

"She finishes her chips with a sigh, knowing she can’t afford another delivery splurge"

show screen thought ("Do chips count as dinner? They're technically vegetables.")

"She trudges into the kitchen, grabs herself some almost expired eggs, and a tin of tuna, and prepares dinner."

hide screen thought

ew "I’ll have to buy groceries on the way back from work tomorrow."

"The thought of going to the grocery store on a weekend sends a shudder through her body but she has too, her fridge is practically bare."

"Pushing that thought from her mind, she takes her little sandwich to the kitchen table, not bothering to grab herself a plate. After a lackluster end to a stressful day, she heads to bed mourning the fact she’s given up her weekend for extra work. At least she’s putting in a good impression with her boss."

hide Eir
show bg black with w33
pause (1)

########################################INSERT  CG HERE########################################

#Weekend work montage, Eir on a crowded Eir in her mostly empty office with headphones firmly on. Eir trying to go grocery shopping two nights in a row only for her to have left the office and the line be super long on Saturday afternoon when she goes and too late on Sunday as it closed. 


#INT. EIR’S OFFICE, DAY WEDNESDAY

#$ Mood_Happy += 0
#$ Mood_Focus = 0
#$ Mood_Hungry = 0
#$ Mood_Chill = 0
#$ Mood_Sleep = 0
#$ Mood_Panic = 0
#$ Mood_Stress = 0
#$ Mood_Embarrassed = 0

scene EirOfficeDay

$ workbag.add_item("Phone")
$ workbag.add_item("Laptop")
$ purse.add_item("Planner")

show Jade at right
show Eir Work at left

jl "Eir! How are you?"

"She pales as she sees her boss, Jade Logan, sitting at her desk."

show screen thought ("What’s she even doing here this early? Is this about over the weekend?")
show ewChibi panicked at topleft

show Eir Happy

ew "Hey Ms. Logan! What brings you over here?"

jl "Oh nothing much, just wanted to thank our star employee for an amazing job with the Sheen project and that last minute Dennis Project?"

hide screen thought
hide ewChibi

ew "They liked it?"

show Eir Panic

jl "They love it! I’m so impressed with what you got done, in a weekend no less!"

show Jade Intense

"Jade clasps Eir’s hands in hers. Eir hopes Jade doesn’t realize how sweaty they are. She manages to force a grin onto her face, it does always feel good to do well at work, no matter how tiring it is."

show Eir Happy

jl "Now, they’d like to hire you again. But the project’s another rush order, would that be okay?"

ew "Of course"

"So I’m definitely working overtime if I don’t work my butt off."

hide Jade

show Eir at center

"I do my best to look chipper as I sit at my desk, starting on this new project."

hide Eir
#hide screen invdisplay

show bg black with w33
pause (1)

#CHANGE OF POV: TROY
#INT. RESTAURANT, DAY WEDNESDAY

scene bg green

show Troy Barista2 Bored at right

"Troy Colby makes his third macchiato for a customer when his coworker enters, fifteen minutes late. He would sighs in relief but the customer is watching him avidly make their drink, he maintains his work smile. He gets it, but this happens all the time."

show cwMarcia at left

"Regardless, he nods his hello at Marcia as she pulls her apron over her head and comes around the counter."

tc "Hey!"

cwMarcia "I’m sorry about being late man, my car broke down and--"

tc "It’s no problem. Stuff happens, I get it. I’ll finish this up and go to the back. You can bring it to the customer."

"Troy wishes his coworker could’ve at least wait a couple months before using the old car excuse again."

cwMarcia "Hey Troy, what are your plans for Friday?"

tc "Probably passing out after my shift, why?"

hide cwMarcia
show cwHarvey at left

"Another one of Troy’s coworkers looks over from the register."

cwHarvey "You seriously don’t remember? Friday’s Julia’s promotion party!"

tc "I thought that was next Friday. I’m beat, I don’t think I’ll be able to make it."

cwHarvey "Come on dude, our manager’s gonna own this place. At least come say hi."

tc "I’ll send her a text or something, I’m going to be exhausted after my messanger shift."

hide cwHarvey
show cwMarcia at left

cwMarcia "You know, she said she was looking forward to seeing you."

"Well, that does it. Troy owes Julia a lot, he should show up for her."

tc "Alright, alright. I’ll show up. Don’t wanna piss you all off too much."

cwMarcia "You know what they say, I got arms of steel. I’ll drag you over myself if I have to!"

hide cwMarcia
show cwHarvey at left

cwHarvey "I’ll join you on that one."

tc "I’m {i}definitely{/i} going now."

"With that decided for him, Troy heads home. On the way, he makes sure to mark Julia’s party on his phone calendar."

hide cwMarcia
hide Troy

#INT. EIR’S APARTMENT, EVENING - THURSDAY

scene EirBedroomNight

##############################################################
############################VIA TEXT############################
##############################################################

show screen EirPhone
#call txt_startEir
$ del_all_msg()
$ kstar("So, when are we hanging? Did you say you wanted to do Saturday or Sunday?")
$ eir("Why not booooth! I got a bunch done so I can swing it if you can") # alert=True)
$ kstar(">:) I’m hella down. This week’s been disgusting, as you already know.")
$ eir("Lol I can’t believe what your coworker tried to pull.")
$ kstar("RIGHT? But enough about that, I’m gonna get mad again if I talk about my week.")
$ kstar("How's yours been?")

menu:
    
    "Detailed recount of all the ways she loves her jobs just wishes her coworkers were more independent.":
        jump detailed
        #block of code to run
    "Minor gripes about work, mostly glossed over":
        jump minor
    "Glosses over everything and deflects when Karla tries to press her":
        jump glossy

label detailed:
    show screen txt_msg

    $ eir ("Soooo much, you down to hear it?")

    $ kstar ("Yeah definitely")

    $ eir ("Okay so I love my job but my coworkers are way too dependent on me!! Any time anything happens I’m the one who has to fix it! AND my boss gave me a huge project to work on that’ll help my career, but how am I supposed to get it done with all this bullshit! Ugh, I hate people.") 

    $ kstar ("Damn that sucks. Guess we both have some work problems, huh?")

    $ eir ("Tell me about it. I’m just exhausted Karla, I don’t know when I’ll fuck it up.")

    $ kstar ("Who says you will though? You could pull all this off.")

    $ eir ("I guess lol? I just don’t have that much faith in myself")

    $ kstar ("Well maybe you should, stop being stupid Eir")

    $ eir ("I got it, I got it.") 

    hide screen txt_msg
    jump txt_after_menu

label minor:
    show screen txt_msg

    $ eir ("Work’s just being a bitch")

    $ kstar ("How so?")

    $ eir ("I just got a bunch of new work, but I’ll manage.") 

    $ kstar ("If you say so...I’m worried though.") 

    $ eir ("Don’t be!! Might be a mess in life, but I usually don’t fuck up work too badly.")

    $ kstar ("Okay that’s true.") 
    hide screen txt_msg
    jump txt_after_menu

label glossy:
    show screen txt_msg

    $ eir ("It’s nothing! Life’s just a little tough right now but it’s all good now.")

    $ kstar ("Are you sure??")

    $ eir ("Super sure!")

    $ kstar ("Weren’t you just saying you had a project or something? You can talk to me you know.")

    $ eir ("I know I can. I’m fine though, seriously.") 

    $ kstar (":/")

    $ eir (":)")
    hide screen txt_msg
    jump txt_after_menu

hide screen EirPhone
#call txt_end

##############################################################
#######################END  TEXT##############################
##############################################################

#INT. EIR’S OFFICE, MORNING FRIDAY

scene EirOfficeDay

show text "{size=+50}{font=fonts/CaviarDreams_Bold.ttf}8:26AM{/font}{/size}" at top with Pause (10)
hide text with dissolve

"Eir comes into the office thirty minutes early for the first time in--well, the first time ever. She prides herself on many things, but coming in early has never been one of them. This is a good sign."

show Eir Work at center

"As she sits down at her desk, Eir feels confident she can get work done. For once, her confidence isn’t unfounded. She’s doing pretty well for herself. That is, until lunch rolls around."

show cwAubrey at right

cwAubrey "Hey Eir!"

show screen thought ("Oh god what is it now? How? Why")

show Eir Happy

ew "Hey Aubrey, what’s up?"

cwAubrey "You know, I really wanted to talk to you about this project I’ve been working on."

hide screen thought

ew "Uh, what about it?"

"Eir loudly clears her throat to indicate she’s working on something. That hint flies past Aubrey, who pulls up a chair next to her and starts talking."

show screen thought ("Please take the hint, please take the hint, please take the hint")

cwAubrey "I wanted to say that I’m really interested in how I can explore the aspect of communal food that my client--"

show screen thought ("She did not take the hint.")

"Aubrey goes on. And on. And on. Normally, Eir would be thrilled to have a coworker approach for something without asking for help. But these are not normal circumstances."

ew "Uh, Aubrey--"

hide screen thought


#END OF ACT
show bg black with w9
pause (1)
hide bg black with w9
pause (1)

call Beta_Ending from _call_Beta_Ending

label credits:
    $ credits_speed = 30 #scrolling speed in seconds
    scene bg black #replace this with a fancy background
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

init python:
    credits = ('Backgrounds', 'Uncle Mugen'), ('Sprites', 'Deji'), ('Writing', 'meltycreamcats'), ('Writing', 'margaretcatter'), ('Programming', 'margaretcatter'), ('Programming', 'Arsym'), ('GUI Design', 'Re:Alice'), ('Music', 'Kevin MacLeod'), ('Music', 'XXX'), ('SFX', 'Mike Koenig'), ('GFX Wipes', 'Kia')
    credits_s = "{size=60}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n7.0.0.196" #Don't forget to set this to your Ren'py version
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    # This ends the game.
return
