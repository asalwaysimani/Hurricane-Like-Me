# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.
label start:

show bg rose with w12
pause (.5)
show text "{size=40}Preface{/size}" at truecenter with Pause (4)
hide text with dissolve
hide bg rose with w12
pause (1)
scene bg rose
show Troy Happy at right

# These display lines of dialogue.
tc "So this is they story of me, Troy Colby, and the time I tried to do the right thing and still got stuck literally holding the bag."

show Eir Angry at left

ew "Now wait a second there Troy!"
tc "This is Eir, she's the main character of this game."

ew "Thats right I'm the main character so why are you here doing the intro?"
tc "Because you were late, we were supposed to start this ten minutes ago."

show Eir Embarrassed at left

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
#Add more thanks here from the people who helped me build this. Semi similar to credits at the end
show Eir Happy at left
tc "Okay, enough chatter from the two of us, onto the game!"
hide Eir
hide Troy

label Prelude:
show screen invdisplay

show bg grey with w12
pause (1)
show text "{size=40}Prelude{/size}" at truecenter with Pause (4)
hide text with dissolve
hide bg grey with w12

#INT. EIR’S APARTMENT, DAY - FRIDAY
scene EirBedroomDay
"The alarm clock goes off with a cruel consistency, and I groan under my blankets."
"Beep beep beep."
ew "Please, please be quiet."
show Eir Bored
"My pleas don’t matter to the clock. Eventually I remove my hand from a nest of blankets to slap the alarm clock into submission. I can afford five more minutes."
"...Right?"
"The alarm clock says otherwise, continuing to beep despite my groans and hits."
ew "Argh, what time even is it?"
"I slap around my table for a few seconds until I find my phone, pulling it into the blankets with me."
"It’s 8:15 in the morning."
show Eir Panic
"I have a forty minute commute and it’s 8:15."
"Oh god. Oh my god."
"For a moment I contemplate if I really need a job."
"And then I’m up."
"I rush into the closet, moving past the piles of clothes and digging through my shoes. I take a glance at the outfit I prepared on hanging on the back of my bedroom door. Black shoes will do. I dig out a pair."
show Eir
ew "Okay, I have this in the bag"
"I stumble through the stray shoes and clothes, grab a book from my End Table Of Books™ to read on the way, and change while I get my hair presentable."

$ workbag.add_item("Phone")
$ workbag.add_item("Laptop")
$ purse.add_item("Planner")

"Then, the daily grind begins."

hide Eir

show bg black with w33
pause (1)

#INT. EIR’S OFFICE, DAY FRIDAY
scene EirOfficeDay

"9 AM"
show Eir at left
"I arrive to the office exactly on time. Which given that I ride mass transit it is a testament to my skill."
"Smoothing my skirt down I unshoulder my bag and make my way to my cubicial."
"I have the Sheen Project to work on today, which honestly might take me all day to do."
"However I am waylaid before I even make it there."
show cwAubrey Embarrassed at right
cwAubrey "Eir! Would you mind helping with this here?"
ew "Of course!"
"I look over one of my coworker’s design and give some quick feedback."
show Eir Happy
"I don’t even remember what I’m saying, but I make sure to leave with a smile before heading to my desk."
hide Eir
hide cwAubrey
"I’m about an hour into my work when I’m disrupted again."
show Eir Bored
ew "Okay, the Sheens need this in by 10 am Monday, but I want to turn it in today. For the--"
show cwCallahan at right
cwCallahan  "Excuse me Eir?"
show screen thought ("{i}Ugh{/i}, not this guy again.", chibi_panicked, 'left')
show Eir Happy
ew "Yes? How can I help?"
cwCallahan  "Could you deal with the Johnsons? They’re outside."
ew "Sure! I’ll be right there."
hide cwCallahan
hide Eir
hide screen thought
"After a quick chat with the Johnsons, and no help from my coworker, I return to my desk."
" Sheen project, I’m coming for--"
show cwPete at right #Panic
cwPete "Eir? Oh thank god you’re here!"
show Eir Panic at left
ew "What is it?"
cwPete " I think I accidentally deleted a file for the Mendes drafts, could you come check?"
"{i}Oh you’ve got to be kidding me.{/i}"
show Eir Happy
ew "I’m happy to help! Just let me drop this at my desk real fast"
"I’m not happy to help."
hide cwPete
show Eir Bored
"But I manage to recover the files and power walk to my cubicle without too much trouble."
"I take a quick glance at the clock, then around to see if anyone needs my help."
show Eir
"I sigh in relief when I see no one staring too hard at my desk, and finally get to work."
hide Eir

show bg black with w33
pause (1)

scene EirOfficeAfternoon
"4:30 PM"
show Eir Happy at left
"My jaw cracks a little as I yawn. In my shoes so do my toes as I flex them."
"I glance at my computer clock, thirty minutes until quitting time."
"And then the weekend. The glorious, glorious weekend. "
show cwAubrey at right
cwAubrey  "Eir, Ms Logan needs you in her office. She asked for you by name again."
show Eir Panic
"And poof there goes the dreams of leaving on time today."
show Eir
ew "One second, just saving my work."
hide cwAubrey
"I quickly save and quit out of my work, giving the clock on my computer one more longing glance before collecting my laptop."
"I roll my shoulders once, then twice, then put on my best ‘How can I help you face’ and head towards her office."
show Eir Happy
hide Eir

show bg black with w33
pause (1)

#INT. EIR’S APARTMENT, NIGHT - FRIDAY
scene EirBedroomEvening
show Eir Work
"The second I close the door my shoes are off. Kicked into a heap just out of the way."
" I dump my bag swiftly after and make a beeline for my bedroom."
$ workbag.remove_item("Phone")
$ workbag.remove_item("Laptop")
$ purse.remove_item("Planner")
"In a flash my work clothes have joined the pile and I’m comfortably back in my house wear."
show Eir Happy
"I pad back to the front door and fish out from my bag my work and personal phone."
"The work phone goes straight onto the side table to charge while I pocket my own phone."
ew "God I don’t know how I did it!"
show Eir PJs
"I grab a bag of chips to snack on as I lay on my bed. I’m exhausted, and I still have work tomorrow too."
"I can handle work fine when I’m there, but everything else seems to screw itself up."
ew "I wish I could manage things a little bit easier. Even get some help."
"If I made a lot more money, I’d even consider a maid service at this point. But that’s a pipe dream right now."
"I finish my chips with a sigh, knowing I can’t afford another delivery splurge."
"I trudge over to the kitchen, grab myself some almost expired eggs and a tin of tuna, and prepare dinner."
ew "I'll have to buy groceries on the way back from work."
"With that thought, I take my little sandwich to the kitchen table, not bothering to grab myself a plate."
"After a lackluster end to a stressful day, I head to bed dreading the next week."
hide Eir
show bg black with w33
pause (1)

#INT. EIR’S OFFICE, DAY THURSDAY
scene EirOfficeDay
$ workbag.add_item("Phone")
$ workbag.add_item("Laptop")
$ purse.add_item("Planner")
show Jade at right
show Eir Work at left

jl "Eir! How are you?"
"I pale as I see my boss, Jade Logan, sitting at my desk. What’s she even {i}doing{/i} here?"

show Eir Happy
ew "Hey Ms. Logan! What brings you over here?"
jl "Oh nothing much, just wanted to greet our star employee for an amazing job with the Sheen project?"
ew "They liked it?"
show Eir Panic
jl "They love it!"
"Jade clasps my hands in hers, and I can’t help but grin at that. It always feels good to do well at work, no matter how tiring it is."
show Eir Happy
jl "Now, they’d like to hire you again. But the project’s another rush order, would that be okay?"
ew "Of course"
"So I’m definitely working overtime if I don’t work my butt off."
hide Jade
show Eir at center
"I do my best to look chipper as I sit at my desk, starting on this new project."

hide screen invdisplay
#END OF ACT
show bg black with w9
pause (1)
hide bg black with w9
pause (1)

label Act_One:

show bg black with bites
pause (2)
hide bg black with bites
pause (2)

scene bg white
show text "Act 1" at truecenter with Pause (4)
hide text with dissolve

#INT. EIR’S OFFICE, EVENING THURSDAY
scene EirOfficeNight
show Eir
"I glance at the clock then around the office. No one is heading my way, no one is looking at my funny. "
"This could be my shot. I glance at the clock again."
"Technically I’m done with the draft of the new Sheen project, in record time even for me."
"Technically I could leave. Another glance around the office."
"But no one else has, what are they all working on?"
" For once it seems my coworkers are diligently on top of their own work with no input from me."
ew "This isn’t a dream, right?"
"I consider for a moment sneaking away to the bathroom, hiding out there for a while before circling back to my desk for my things and betting on a hasty retreat home. "
"Well, they do say to be the change you want to see in the world. "
"And I really want to see a world where I leave work early. First stop, the bathroom. "

#INT. EIR’S OFFICE BATHROOM, EVENING THURSDAY
scene EirOfficeBathroom

"I splash water on my face and formulate my plan."
"Under no circumstance will I be deterred. I’m done with work, I can leave."
ew "I got this. All I have to do is leave and not feel too guilty about it. That should be easy."
"I always have this weird tingling feeling in the back of my head when I leave before my coworkers."
"However this time it won’t put me off. I’m positive there is nothing waiting for me and if it is it can definitely wait till tomorrow."
"My plan is firm, grocery store then home."
"I leave the bathroom with a new sense of confidence that is quickly shot down by a coworker waiting at my desk."

scene bg grey

show cwAubrey at right
cw3 "Oh thank god I caught you Eir! I really need your help."
hide cwAubrey
hide Eir

#INT. SUBWAY CAR, EVENING THURSDAY

scene IntSubwayCar
"So much for a quick retreat from work. At least it was still light out."
"And I had an even slower haul to and from the grocery store, but I’m finally heading home."
"Too lazy to get my earbuds out, I settle for listening to the subway and the passing sound of the city."
"It takes all my power not to fall asleep. And even then, I’m startled when I hear it’s my stop."
$ workbag.remove_item("Phone")
$ workbag.remove_item("Laptop")
$ purse.remove_item("Planner")
"Hurrying off, my plan to get home and pass out is all that’s on my mind."
ew "Wait...I’m missing something."
"I do a quick fumble around my bags, and instantly realize my work bag, with all my materials, are still on that train."

#EXT. SUBWAY STATION, EVENING THURSDAY
scene trainstationDusk

show Eir Panic at right
ew "Shit, shit, {i}shit{/i}!"
"I rush over to the station agent as quickly as I can."
show side StationAgent1 at left
sa1 "How can I help you?"
ew "My--my bag! I left my bag on that train."
sa1 "Well, we can’t stop it. You’re close enough to the end of the line that you can wait until it comes back around."
ew "...okay"
#show Eir Sad
"I stand there fo a few minutes, trying not to cry in front of the station agent."
"I might be a mess, but I try to contain that mess in my private life."
hide StationAgent1
hide Eir

"30 Minutes Later"

scene trainstationNight
show StationAgent1
sa1 "You can check the train now, don’t worry, I won’t charge you."
ew "Thank you so much!"
"At least I have that going for me."
hide StationAgent1
show Eir Panic
"I rush onto the train again. Overhead I vaguely hear the station agents voice over the intercom."
"I check where I think I was sitting, check where I didn’t think I was sitting."
"But there’s nothing there. I check the next car, just in case but there’s still nothing there."
"I'm pretty sure now is an okay time to start crying"
"When I switch train cars and head back, I remember thanking the station agent between my frustrated tears before walking home."
"I’m completely defeated, and I don’t know what to do. "

hide Eir Panic

scene IntSubwayStation

#INSERT TRANSITION HERE

show Troy
tc "Man, I really didn’t mean to stay out this late. "
"After my friends took me out for dinner on the other side of town,"
"I’m pretty tired. It’s rare for me to go out and have a good time, and I’m glad I did it."
"But I still feel a sense of guilt I can’t shake off."
tc "God, it's quiet."
"I’m the only one in this car, and I’m waiting until the end of the line."
"Close to my stop, I notice a bag left behind with no owner."
tc "Lost and found might be open around now."
"I pick up the bag, careful not to mess with any of its overflowing belongings. Must be a busy person."
tc "Seems like they have their life together…"
"I say it without realizing. Really Troy? Using a stranger to fuel your self pity? That’s a new low."
"I sigh as the train comes to my stop, and head towards the lost and found office."
"The moment I see the closed sign, I feel a sense of dread."
tc "Well this is unfortunate."
"I usually don’t take the subway back this late, so there’s no way I would’ve known."
"But I can’t just leave it back on the train."
tc "Dear bag owner, please don’t get too mad."
tc "I’m trying to return this to you, but it’ll have to wait till tomorrow morning."
"I head on home, carrying the bag carefully."

scene TeganCondoLivingRoomNight

"My roommates are out for the night, but I still keep quiet."
"Maybe I can make this easier on the bag owner and myself and contact them right away."
tc "Let’s see...is there a phone in here or something?"
"Luckily, there is a phone. I take a look at the home screen, and am prepared to take an emergency call."
"But there’s no passcode."
tc "What kind of person doesn’t have a passcode?"
"I shake my head, this isn’t my business. I search for the number labeled “HOME” to start with."
"Internally, I try to figure out what I’d say to the bag owner."
"{i}Hi! I’m not a thief, I just couldn’t take this to your place.{/i}"
"{i}When can I return your bag? Why don’t you have a passcode?{/i}"
"But the phone continues to ring, without any cue to go to voicemail"
"Eventually, I hang up. I’ll try something else tomorrow, I’m sure the owner of this bag isn’t going anywhere."

#INSERT TRANSITION HERE

scene EirBedroomEvening
show Eir Angry

ew "Ugh, I can’t deal with this right now!"
"The bell in my apartment is buzzing nonstop. I buzzed them in for a bit, but no one showed up."
"I have a feeling the kids from 4G locked themselves out again, but I can’t put up with them coming home at god knows when."
"Eventually, I mute the buzzer."
ew "I need to get another ice pack."
"I put away my ice pack, and exchange one for another."
"Then I head back to my couch, comforted by my blankets and my bunny pajamas."
"I feel my phone vibrate in my hand, and take a look at who’s texting me."

##############################################################
############################VIA TEXT############################
##############################################################

call txt_startEir

kj "Why don’t you have a lock on your phone? That’s like phone having 101 right here."
ew "Because it takes too long geez. Sometimes people are lazy aka me and all I want to do is swipe and there it is. No fuss no muss."
kj "Christ, how are you an adult?"
ew "I ask myself that every day. One day I’m going to look up and realize I’m thirty and have no idea how that happened to me."
kj "It happens to the best of us."
kj "Anyway i guess it’s a good thing that you don’t lock your phone. Also that in the year of twenty seventeen you have a landline. Like who even has one of those."
ew "It came with the apartment and its connected to my bell"
kj "I’m not judging its handy dandy for this exact moment."


##############################################################
############################NOT  TEXT############################
##############################################################

EirThoughts "I’m being judged. I can feel it through the phone."


##############################################################
############################VIA TEXT############################
##############################################################

ew "What does one even do to get their stuff back after losing it on a train anyway?"
kj "Practical me says suck it up and buy new things."

##############################################################
############################NOT  TEXT############################
##############################################################

"Argh so helpful."

##############################################################
############################VIA TEXT############################
##############################################################

kj "Optimistic me says check lost and found?"

##############################################################
############################NOT  TEXT############################
##############################################################

"Oh, promising. I hadn't even thought about a lost and found."
"I send up a fervent prayer that some kind old lady found my bag and turned it in to the lost and found."
"{i}I roll off the couch to my feet. Tonight is a loss of epic proportion plus it’s late, I may as well head to bed.{/i}"
"{i}I’ll figure out in the morning what I need to do to replace my things{/i}"

label Act_Two:

scene bg white
show text "Act 2" at truecenter with Pause (4)
hide text with dissolve

label Act_Three:

scene bg white
show text "Act 3" at truecenter with Pause (4)
hide text with dissolve

label credits:
    $ credits_speed = 20 #scrolling speed in seconds
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
    credits = ('Backgrounds', 'Uncle Mugen'), ('Sprites', 'Deji'), ('Writing', 'meltycreamcats'), ('Writing', 'margaretcatter'), ('Programming', 'margaretcatter'), ('Music', 'Kevin MacLeod'), ('Music', 'XXX'), ('SFX', 'Mike Koenig'), ('GFX Wipes', 'Kia')
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
