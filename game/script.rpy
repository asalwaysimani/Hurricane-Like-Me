# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



image L3rd = "images/Backplate5.png"
define config.layers = ['master', 'transient', 'screens', 'overlay']

init python:
    mp = MultiPersistent("HurricaneLikeMe.renpy.org")

#The game starts here.



show bg grey with w12
pause (.5)
show text "{size=40}Preface{/size}" at truecenter with Pause (4)
hide text with dissolve
hide bg grey with w12
pause (1)
scene bg grey
show TroyBase at right

#These display lines of dialogue.

tc "So this is they story of me, Troy Colby, and the time I tried to do the right thing and still got stuck literally holding the bag."
pause (15)
show EirAngry at left

ew "Now wait a second there Troy!"
# tc "This is Eir, she's the main character of this game."

show TroyHappy at right
ew "Thats right I'm the main character so why are you here doing the intro?"
tc "Because you were late, we were supposed to start this ten minutes ago."

show EirEmbarrassed at left

ew "Ek, no we were supposed to start when I got here! I'm the main character!"

show TroyBored at right

tc "We're the main, you know what never mind. We're here we're starting this."

show TroyIntense at right

tc "Welcome to Hurricane Like Me."

show EirHappy at left

ew "A visual novel written for Summer Novel Festival in 2018."
tc "Please keep in mind this was our first visual novel so there are some kinks to work out."
tc "In fact any and all feedback is welcomed."
ew "Our creator even made a handy dandy feedback form on the bottom in the menu"
ew "Also, while the story is complete there are several visual assets that aren't fully implimented."
tc "Like sprites & backgrounds"

show EirBored at left

tc "Hence our current form and this lovely dove grey behind us."
#ew "Exactly. So our lovely creator has used the even lovelier Deji's placeholder sprites in their places."

show EirHappy at left

#show Coworker1 at center

#ew "Aren't they so stinking cute?"
tc "Okay, enough chatter from the two of us, onto the game!"
hide Eir
hide Troy
hide cwPete

label Prelude:
show screen invdisplay

show bg grey with w12
pause (1)
show text "{size=40}Prelude{/size}" at truecenter with Pause (4)
hide text with dissolve
window hide
hide bg grey with w12
pause (1)

#INT. EIR’S APARTMENT, DAY - FRIDAY
scene EirApartmentDay

show text "{size=40}{font=Roboto-Black.ttf}Friday{/size}{/font}" at truecenter with Pause (4)
hide text with dissolve



"The alarm clock goes off with a cruel consistency, and I groan under my blankets."

play sound "music/alarm_clock.mp3" fadein 1.0

stop sound fadeout 1.0

ew "Please, please be quiet." 

show screen moodpointdisplay

$Mood_Hungry -= 1 
$Mood_Chill += 10
$Mood_Sleep += 2

show Eir Bored in PJs

"Her pleas don’t matter though, not to this demon of a clock. She removes her hand from a nest of blankets to slap the alarm clock into submission. She can afford five more minutes."

"...Right?"

"The alarm clock says otherwise, continuing to caw at her despite her groans and hits."

ew "Argh, what time even is it?"

"She slaps around her table for a few seconds until she finds her phone, pulling it into the blankets with her."

"It’s 8:15 in the morning."

$Mood_Happy -= 5
$Mood_Focus += 9
$Mood_Chill -= 10
$Mood_Panic += 8

show Eir Panic in PJs

"She has a forty minute commute and it’s 8:15."

ew "Oh god. Oh my god."

show Eir Surprised in PJs

"{i}Oh god. Oh my god{/i}"

ew """For a moment she contemplate if she really need a job.

And then she is up and ready to go

She rushes into the closet, moving past a pile of clothing, and finally digging through her shoes. She takes a glance at the outfit she's prepared hanging on the back of her bedroom door. Black shoes will do. She digs out a pair"""

show Eir Neutral in Work

ew "Okay, I have this in the bag"

"She stumbles through the stray shoes and clothes, grabbing a book from her End Table of Books. Pausing to maker her hair presentable before rushing out of the door"

$Mood_Happy += 7
$Mood_Chill += 10
$Mood_Panic -= 8
$ workbag.add_item("Work Phone")
$ workbag.add_item("Laptop")
$ workbag.add_item("Planner")
$ workbag.add_item("Work ID")
$ purse.add_item("Personal Phone")
$ purse.add_item("Headphones")

"Then, the daily grind begins."

hide Eir

#Potential CG Here#

scene IntSubwayCarDay

"Eir is on the train, she is reading and listening to music. 
She is sitting with her head down buried in her book."

"The train isn't very crowded." 

"In the distance at the other end of the train is Troy standing in his bike messenger uniform with headphones on.
He is leaning on his bike, standing by the doors. The train hurtles down the tracks."

#TODO: Title Appears on screen here 

window hide
show bg black with w33
pause (1)

#INT. EIR’S OFFICE, DAY FRIDAY
scene EirOfficeDay

show text "{size=40}{font=Roboto-Black.ttf}9 AM{/size}{/font}" at truecenter with Pause (4)
hide text

show EirWork at left

"I arrive to the office exactly on time. Which given that I ride mass transit it is a testament to my skill."

"She arrives at the office exactly on time. Which given that she had to ride mass transit is a testament to her time management skills."

"Smoothing her jacket down, she unshoulders her purse and workback and makes her way to her cubicle." 

"She has the Sheen Project to work on today, which might take her all day to do."

"However, she is waylaid before she even makes it there."

show cwPete Embarrassed at right

cwPete "Eir! Would you mind helping with this?"

"If Pete weren't so close, Eir would hae cussed under her breath. She shakes off the last reminates of sleep and put's her game face on."

$Mood_Happy -= 5
$Mood_Focus += 1
$Mood_Chill -= 5
$Mood_Sleep -= 2

ew "Of course!"

"She looks over Pete's design and gves some quick feedback. She doesn't even remember what she's saying,
but she makes sure to leave with a smile before heading to her desk finally"

$Mood_Happy -= 2

hide EirWork
hide cwPete

show text "{size=40}{font=Roboto-Black.ttf}10:30 AM{/size}{/font}" at truecenter with Pause (4)
hide text

"She's about an hour into her work when she's distrupted again."

show EirHappy at left

ew "kay, the Sheen projects needs to be ready by 10 am Monday, but I want to turn it in today. For the--"

show cwAubrey at right

cwAubrey "Excuse me Eir?"

"{i}Ugh, not Aubrey again.{/i}"

ew "Yes? How can I help?" 
#show EirChibiAngry at topleft
show Eir VHappy

cwAubrey "Could you deal with the Johnsons? They’re outside."

ew "Sure! I’ll be right there."

hide cwAubrey
hide Eir

"After a quick chat with the Johnsons and no help from Aubrey, she returns to her desk." 

"{i}How did I end up as the people person in this office? 
I never know what to say to people?, get it together Eir{/i}" #Upper screen text as if in a thought 

"The Sheen Project, she's coming for--"

show Eir Tired at left
show cwCallahan Panic at right

cwCallahan "Eir! Oh thank god you're here"

show EirPanic

ew "What is it?"

cwCallahan "I think I accidentally deleted a file for the Mendes drafts, could you come check?"
"{i}Oh you’ve got to be kidding me.{/i}" #Upper screen text as if in a thought 

show EirHappy
#show EirChibiAngry at topleft

ew "I’m happy to help! Just let me drop this at my desk real fast"

"She is not happy to help. She manages to recover the file, which shockling has actually been deleted and power walks back to her cubicle without much trouble."

"She takes a quick glance around at the clock, almost half the day wasted there's no way that she's going to turn in the Sheen project early. So much for that hope and dream."

"She then looks around to see if anyone needs her help"

"{i}God help her if they need her help{/i}"

"Eir sighs in relief when she sees no one staring too hard at her desk or even in her general direction."

hide EirOfficeDay

window hide
show bg black with w33
pause (1)

scene bg grey

show text "{size=40}{font=Roboto-Black.ttf}5:30 PM{/font}{/size}" at truecenter with Pause (4)
hide text

show EirHappy at left

"Her jaw cracks a little as she yawns. She flexes her toes in her shows, they crack a little as well.
Glancing at her computer clock"

"{i}Thirty minutes until quitting time{/i}"

"And then it's the weekend. The glorious, glorious weekend."

show EirTired

show cwAubrey at right

cwAubrey "Eir, Ms Logan needs you in her office"

"She leans in and whispers it in a conspiratorial manner"

cwAubrey "She asked for you by name"

$Mood_Chill -=5
$Mood_Panic -=5

"{i}Oh god, I'm going to get fired...on a Friday{/i}" #Upper screen text as if in a thought bubble 

"And poof! There goes Eir's dreams of leaving on time today. And probably also having a job."

ew "One second. Just saving my work"

show EirNeutral
#Show Eir Panic at top left

"She quickly saves and closes her work, giving the clock on her desktop computer one more longing glance
before collecting her laptop {i}definitely not hugging it to her chest{/i}. She rolls her shoulder once, then twice,
then puts on her best 'How can I help you face' and heads past Aubrey towards Ms. Logan's office"

hide cwAubrey
hide Eir
hide bg grey

scene IntJadeOffice

#TODO: Scene to be written goes here.

$Mood_Happy +=5
$Mood_Focus +=5
$Mood_Panic -=3

show bg black with w33
pause (1)

#INT. EIR’S APARTMENT, NIGHT - FRIDAY
scene EirBedroomEvening
show Eir at left

"The second she closes the door her shoes are off. Kicked into a heap just out of thdoorway.
Just as quickly she dumps her bag, then makes a beeline for her bedroom"
$ workbag.remove_item("Phone")
$ workbag.remove_item("Laptop")
$ purse.remove_item("Planner")
hide Eir

"In a flash, her work clothes have joined the pile and she is comfortably back in her house wear"
show EirPJsSweats

#TODO: Add footstep sfx

"""She zooms back to the front door and fishes out her phones from her bag juggling both, her own personal phone and her too large work phone in her small hands.

The work phone goes straight onto the side table to charge while she pockets her own phone"""

ew "I don't know how I did it!"

"She grabs a bag of chips to snack on as she lays on her bed exhausted."

#Add chips sound sfx here

"And here is still work tomorrow, on the weekend no less! She can handle work fine when she is there but everything seems to be screwed up the second she leaves the office, case and point her apartment."

"She looks around her apartment, saying it is kind of a mess would be an understatement. 
There is a pile of pens on the floor, several sheets of paper she's been working on laying about, a blanket and a pillow in a heap in front of the couch, gods when was the last time that she cleaned?"

$Mood_Happy -=3

ew "Man, I wish I could manage things a little bit better. Even if it means getting some help"

show EirNeutral

"If she made just a little bit more money, she'd even consider a maid service. But that's a pipe dream for right now."

"She finishes her chips with a sigh."

#stop sound

"Knowing that she can't afford another delivery splurge she considers" 

"{i}Do chips count as dinner? They are technically vegetables{/i}" #Upper screen text as if in a thought bubble  

"She trudges into the kichen, grabs herself some almost expired eggs, a tin of tuna, and prepares dinner."

ew "I'll have to buy groceries on the way back from work tomorrow"

"{i}Argh work on a Saturday{/i}"#Upper screen text as if in a thought bubble

"""The thought of going grocery shopping on a weekend sends a shudder through her body but she has too,
her fridge is practically bare. Pushing that thought from her mind she takes her little sandwhich to the kitchen island not even bothering to grab herself a plate.
After a lackluster end to a stressful day, she heads to bed mouring the fact she's given up her weekend for extra work.
At least she's putting in a good impression with Jade."""

"{i}At least there is that.{/i}"

hide Eir

#Weekend work montage, Eir in her mostly empty office with headphones firmly on. Eir trying to go grocery shopping two nights in a row only for her to have left the office and the line be super long on Saturday afternoon when she goes and too late on Sunday as it closes early. 

#Skips a week 

show text "{size=40}{font=Roboto-Black.ttf}Wednesday{/font}{/size}" at truecenter with Pause (4)
hide text with dissolve
window hide
show bg black with w33
pause (1)

scene ExtJadeOffice
$ workbag.add_item("Phone")
$ workbag.add_item("Laptop")
$ purse.add_item("Planner")

show JadeHappy at right
show Eir at left

jl "Eir! How are you?"

"She pales as she sees her boss between her and her cubicle."

"{i}What is she even doing here this early? Is this about the weekend?{/i}"

ew "Hi, Ms Logan! WHat brings you over here?"

#Show ChibiEirPanic at top left

jl "Oh nothing much, just wanted to thank our star employee for an {i}amazing{/i} 
job on the Sheen Project and then the last minute Dennis Project as well"

show EirSuprised

ew "They liked it?"

show JadeIntense

jl "They love it! I'm so impressed with what you got done, and in a weekend no less!"

"Jade clasp Eir's hands in hers. Eir hopes Jade doesnt realize how sweaty they are.
She manages to force a grin onto her face, it does always feel good to do well at work no matter how tiring it is."

show EirHappy

jl "Now they want to hire you, personally for another project. But the project is another rush order, 
as the Dennis Project was from last weekend, would that be okay?"

ew "Of course!"

"So she's definitely going to be working overtime and unfortunately the weekend as well probably. 
But she doesn't mind working her butt off. She does her best to look chipper as she slideds into her desk chair, 
ready to start on this new project."

hide Jade
hide Eir

show text "{size=40}{font=Roboto-Black.ttf}Wednesday{/font}{/size}" at truecenter with Pause (4)
hide text with dissolve
window hide
show bg black with w33
pause (1)

scene IntRestaurantDay

show TroyBarista at left

"Troy Colby is making his thrid macchiato for a customer when his coworker Marcia enters."

show MarciaWork at right

"He would sigh in relief but the customoer is watching him avidly as he makes their drink. He maintains his best work smile.
He gets it, but this happens all the time. Thankfully he doesn't have a shift anywhere else after so he doesn't mind staying later. 
Regardless, he nods his hell at Marcia as she pulls her apron over her head and comves around the counter."

tc "Hey!"

cwMarcia "I’m sorry about being late man, my car broke down and--"

tc "It's no problem, shit happens. I get it. I'll finish this up and get out of your way."

"Troy really wishes she'd at least waited a couple of months before using the old car excise again. But he wasn't going to call her out for it."

cwMarcia "I'll bring it over to the customer."

"Troy gives her the same smile he gives customers."

cwMarcia "So what are your plans for Friday?"

tc "Probably passing out after my shift at the courier shop, why"

"Troy knows he's about to walk into a trap."

show HarveyWork at right #TODO: make sure they don't overlap with Marcia

cwHarvey "Seriously, you don't remember? Friday is Julia's promotion party!"

"Oh yeahhhhhhhhh, that was a thing that was happening and he might have even recalled promising Julia that he wouldn't miss it."

tc "I thought that was next Friday. I'm going to be beat, I doubt I'll be able to make it."

cwHarvey "COme on dude, our manager, who's great --"

"She is."

cwHarvey "--is going to be totally running this place, at least stop in and say hi."

"Argh, he could see where this was going already, a trap just as he suspected. But he has to try anyway."

tc "I'll send her a text or something, I know I'm going to be exhausted."

"Really he's always in a state of exhaustion. Which given his lifestlye and work habits isn't really surprising."

cwMarcia "You know,s eh said she was really looking forward to seeing you."

"And here comes the guilt. Which he is weak to."

tc "Alright alright I'll try to make it. Just don't be pissed if I can't and pass out."

cwMarcia "It's alright, I have arms of steel I'll drag you myself if I have to."

cwHarvey "I'll help."

tc "Well I'm {i}definitely{/i} going now."

"With the choice taken out of his hands, Troy takes his apron off and heads towards to door. On his way out he pulls out his phone and adds a reminder alert for Friday."

hide Troy
hide Marcia
hide Harvey

show text "{size=40}{font=Roboto-Black.ttf}Friday{/font}{/size}" at truecenter with Pause (4)
hide text with dissolve
window hide
show bg black with w33
pause (1)

scene IntEirOfficeDay

label start:

    $ Mood_Happy = 0
    $ Mood_Focus = 0
    $ Mood_Hungry = 0
    $ Mood_Chill = 0
    $ Mood_Sleep = 0
    $ Mood_Panic = 0
    $ Mood_Stress = 0

    $ RelationshipCW = 0
    $ RelationshipJade = 0

show text "{size=40}{font=Roboto-Black.ttf}9:15 AM{/font}{/size}" at truecenter with Pause (4)
hide text 

show EirWork at left
show cwAubrey at right

#TODO: finish writing and fleshing out start of this scene

menu NoseyCoworker:
    "What should Eir do?"
    "Overly polite shooing, Eir turns the conversation to Aubrey's own project.":
        $Mood_Happy +=2
        $RelationshipCW -=2
        if RelationshipCW >=2:
            "Aubrey agrees that she does need to finish her own project but she invites Eir come check it out with her."
            menu DrinksWithCoworkers:
                "Yes, Eir comes to look at Aubrey project which is admittedly pretty nice.":
                    $RelationshipCW +=2
                "Promises to come check it out later, wants to knock out her own project first.":
                    $RelationshipCW +=1
    "Passive agressive shooing, mentioning isn't Aubrey behind on their own project?":
        $Mood_Happy -=2
        $RelationshipCW -=2
        if RelationshipCW is -2:
            "Aubry leaves in a huff, shooting Eir annoyed looks over the cubicle wall as she passes by."
    "Escape to the bathroom and loiter until the coast is clear.":
        $Mood_Happy +=1
        if RelationshipCW >=1:
            "When Eir comes back from the bathroom no one is waiting for her. 
            She is able to continue working. She mouths sorry at Aubrey when they make eye contact."

show text "{size=40}{font=Roboto-Black.ttf}1:45 PM{/font}{/size}" at truecenter with Pause (4)
hide text

show EirNeutral at left

"As Eir finishes up her lunch at her desk she notices Pete peaking over at her out of the corner of her eyes.
She gets up to throw her trash away and yup he is totally watching her as she returns from the kitchen."

menu:
    "Eir returns to her desk and tries to look very busy.":
        "Eir is feeing pretty happy. The Sheen version two project is going well, it is getting done fast and it is even good.
        As she works she overhears Pete asking one of her other coworkers a question and since everything is going so well for her she chimes to help. 
        Pete's question is a fun and easy thing for her to solve. She understands where he got tripped up and appreciate that he asked someone else instead of coming to her."
        $Mood_Chill +=4
        $Mood_Happy +=4
        $RelationshipCW +=4
        if Mood_Happy >=5: #TODO: Check Eir Happy mood points as of right now
                call LeaveEarly
    "Eir ask what is up and Pete comes over.":
        "Eir is pretty tired thankfully the Sheen version two project is going well. 
        It's going to get done but she's probably going to have to stay late to get it done on time if she doesn't want to come in on the weekend. 
        As she is taking a mental break she see's Pete is still looking at her and calls him over. It turns out that his question while interesting is long and complicated. 
        It takes them a while to sort it out and she sort of wishes he had googled what was wrong before coming to her as a head start."
        $Mood_Chill -=2
        $Mood_Stress -=2
        $RelationshipCW +=2
        if Mood_Stress >=5: #TODO: Check Eir Stressed Mood points here
                call LeavesLate
    "Eir looks at Pete before quickly looking away but it's too late eye contact had been made.":
        "Can this day just end. Eir can get nothing done constantly being intrupted by her coworkers. First Aubrey this morning being nosy.
        Now Pete with his never ending questions about everything. The eye contact seeme to signal to Pete that Eir was able to help him out even if that wasn't what she meant to do.
        Eir however is too nice and too much of a pushover to tell him no. She spends a long time trying to figure out his project band then returns to her work. 
        However she can't stop herself from stewing about the time she has wasted helping him. Now she's totally behind on the Sheen project and mad about it."
        $Mood_Chill -=4
        $Mood_Focus -=4
        $Mood_Stress -=4
        $Mood_Happy -=4
        if Mood_Chill <=0:
                call WeekendWork
hide Eir

scene ExtStreetAfteroon

#TODO:Replace with actually written scene at later date.

"Troy biking around delivering packages. Troy has to deliver five packages to different people all over the city. Depending on time of day this may be easier or harder due to traffic. While he is biking around his phone pings with a reminder. Julia's party is in a half an hour."

show bg black with w33
pause (1)

hide screen invdisplay
#END OF PRELUDE

show bg black with w9
pause (1)
hide bg black with w9
pause (1)

label Act_One:

show bg black with bites
pause (2)
hide bg black with bites
pause (2)

#INT. SUBWAY CAR, EVENING THURSDAY



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
"My roommates are out for the night, but I still keep quiet."
"Maybe I can make this easier on the bag owner and myself and contact them right away."
tc "Let’s see...is there a phone in here or something?"
"Luckily, there is a phone. I take a look at the home screen, and am prepared to take an emergency call."
"But there’s no passcode."
tc "What kind of person doesn’t have a passcode?"
"I shake my head, this isn’t my business. I search for the number labeled “HOME” to start with."
"Internally, I try to figure out what I’d say to the bag owner."
"Hi! I’m not a thief, I just couldn’t take this to your place."
"When can I return your bag? Why don’t you have a passcode?"
"But the phone continues to ring, without any cue to go to voicemail"
"Eventually, I hang up. I’ll try something else tomorrow, I’m sure the owner of this bag isn’t going anywhere."

#INSERT TRANSITION HERE

scene EirBedroomNight

ew "Ugh, I can’t deal with this right now!"
"The bell in my apartment is buzzing nonstop. I buzzed them in for a bit, but no one showed up."
"I have a feeling the kids from 4G locked themselves out again, but I can’t put up with them coming home at god knows when."
"Eventually, I mute the buzzer."
ew "I need to get another ice pack."

"I put away my ice pack, and exchange one for another."
"Then I head back to my couch, comforted by my blankets and my bunny pajamas."
$ renpy.pause(1.0)
play sound "new_message.mp3"
$ renpy.pause()
"I hear my phone ding in my hand, and take a look at who’s texting me."

##############################################################
############################VIA TEXT############################
##############################################################


$ msg_name = "KSTAR"
$ m_msg = []
$ gg_msg = "Eir"

window hide
show screen telegram
with dissolve

$ renpy.pause(1.0)

python:

    kstar("Why don’t you have a lock on your phone?")
    kstar("That’s like phone having 101 right here.", who=True)
    eir("Because it takes too long geez. Sometimes people are lazy aka me \nand all I want to do is swipe and there it is. No fuss no muss.", who=False)
    kstar("Christ, how are you an adult?", who=1)
    eir("I ask myself that every day. One day I’m going to look up \nand realize I’m thirty and have no idea how that happened to me.")
    kstar("It happens to the best of us.", who=1)
    kstar("Anyway i guess it’s a good thing that you don’t lock your phone. \nAlso that in the year of twenty seventeen you have a landline. Like who even has one of those.", who=1)
    eir("It came with the apartment and its connected to my bell")
    kstar("I’m not judging its handy dandy for this exact moment.", who=1)


##############################################################
############################NOT  TEXT############################
##############################################################

"I’m being judged. I can feel it through the phone."

##############################################################
############################VIA TEXT############################
##############################################################

python:

    eir("What does one even do to get their stuff back after losing it on a train anyway?")
    kstar("Practical me says suck it up and buy new things.")

##############################################################
############################NOT  TEXT############################
##############################################################

"Argh so helpful."

 ##############################################################
 ############################VIA TEXT############################
 ##############################################################

python:

    kstar ("Optimistic me says check lost and found?")

##############################################################
############################NOT  TEXT############################
##############################################################



"Oh, promising. I hadn't even thought about a lost and found."
"I send up a fervent prayer that some kind old lady found my bag and turned it in to the lost and found."

hide screen telegram

"I roll off the couch to my feet. Tonight is a loss of epic proportion plus it’s late, I may as well head to bed."
"I’ll figure out in the morning what I need to do to replace my things"
"Hopefully i’ve engendered enough good will in the office that getting new stuff won’t be terrible."

#EXT. SUBWAY STATION - DAY (FRIDAY)

#INT. EIR’S OFFICE - DAY (FRIDAY)
scene bg grey

"I’m only late by a few minutes, but it feels like all eyes are on me."
"I try to smile at one of my coworkers and fail miserably. She comes over with a look of concern I’m not used to."

show Coworker1
show Coworker2 at left
show Coworker3 at right

cwPete "Eir is everything okay?"
ew "Uh, yeah I’m fine."
cwPete "Really?"
ew "...not really. I need a favor, actually."

"Anxiety curls up in my throat. I don’t like asking for favors, especially from my coworkers. But I have to do this."

ew "I need to go to IT. I, uh, lost my bag."
ew "I need to head to IT to get my lost items replaced. Could you guys cover me?"
cw2 "Of course!"

"My other coworkers nod in agreement."

cw3 "We’re here to help, since you always do the same for us."
cw2 "This makes us even, right?"

"I can tell she’s joking, but it really doesn’t make things even. I choose not to dwell on it though."

ew "Thanks so much! I’ll be back as soon as I can."
cw1 "Take your time Eir, we got this."
cw3 "We can hold down the fort."

hide Coworker1
hide Coworker2
hide Coworker3

"They probably can but..,I still rush down to IT to get this mess sorted out."
"Best to get everything resolved quickly so I can get back to work. And if I could get the same models in everything, it’ll be just like it never happened."

#INT. EIR’S OFFICE IT DEPT - DAY
scene bg blue grey

show ItGuy

itg "I’m sorry to hear about your lost items, but I just can’t give you new ones."
ew "What?"

"The IT guy gives me a very sympathetic look before continuing."

itg "We only have a select number of items we can give out, and we don’t carry your old phone’s make and model."
itg "We can reimburse your purchase if you buy a new phone though."
ew "But I like {i}my{/i} stuff."

"God I sound whiny even to my own ears."
"The IT guy is nice enough to continue smiling at me regardless, as if he’s seen this a thousand times before"

ew "Wait, what about my work?"
itg "That should all on the cloud, so you can continue working as usual. Just make sure to come get reconnected when you get a new phone and laptop first."
ew "Oh, Okay, thank you again."

hide ItGuy

#INT. PHONE psg - DAY (FRIDAY)
scene bg blue

ew "You’re a grown woman, you can do this."
"It’s an empty pep talk, but I can’t add any false cheer to my voice."
"I don’t like technology psgs very much, too many people trying to sell you on things you don’t need."
"Maybe I’m just old fashioned like that, but the psg’s sterile energy combined with the people cooing over new gadgets makes me wildly uncomfortable."
ew "I have my list of what I should get, but it’ll still take some getting used to."

show psgEmployee

psg "Hi! How can I help you?"
ew "Oh, hi. How are you today?"
psg "How can I help you?"
ew "Uh...okay. I’d like a new phone and laptop for work, and I have the requirements written down here."

"I show him my list, and he nods quickly."

psg "I see! Well, this is a slightly outdated model. I’d like to show you our newest model here--"
ew "Oh, you don’t have to do that."

"I try to plead a bit with my eyes. I know I’m not the best with technology."
"I definitely don’t need the newest anything. Besides, I don’t want to burden the company more than I have to. "

psg "No, I insist. You seem like a hard working woman, you deserve the best."

"I usually like being complimented on my work, but this rubs me the wrong way."

ew "Thank you, but I prefer what I have. You know how it is, right?"
psg "Not really, no. I think it’s okay to treat yourself though!"
ew "But I don’t want t--"

#show psgEmployee Intense

psg "Look here at the uPhone 17, with…"

"My brain shuts off the moment the salesperson starts talking about the three thousand ways this phone is better than mine."

menu phone_shop:
    "But what can I do about it?"

    "Give in and get what the salesperson recommends.":
            ew "...I’ll get that and a new laptop please."
            "Anything to stop the sales pitch, please"
            psg "Glad to hear it! Let me ring you up over here. Good thing your company covers all this, right?"
            ew "Right…"
            "Guilt gnaws at me as I finish my purchase. I know Jade would be okay with it, but I wish I could’ve asserted myself a bit more."

    "Fight for what you believe in!":
            ew "No, I want what I used to have."
            psg "Hm?"
            ew " I’m old fashioned, you know? All those features sound great, but I prefer something I know gets the job done. So if I could get what’s on my list, that would be great."
            psg "If you insist, I’ll ring that up for you."
            "I’m pretty sure I got a massive stink eye, and while I do feel a little bad, I’m happier that I got what I wanted, still fancier than my old phone but definitely not a uPhone 17."

hide psgEmployee

"I head to the office more exhausted than if I’d done a full day of work, and that’s saying something."

#INT- OFFICE, EVENING

show Eir

ew "I’m back everyone."

"I’m drained, but I still want to work on Sheen 2.0."
"For once, everyone’s immersed in their own work and not looking for me, so my quiet entrance goes completely unnoticed."
"I wish I didn’t get this new stuff, but unless someone miraculously gets my stuff to me, I have no choice."

ew "Hello?"

"I say that a little louder this time, but no one greets me back."
"It’s not professional in the slightest, but I can at least make a quick call to lost and found."
"I go to the break room and find the number for lost and found."

#show side StationAgent2 at right

ew "Hello? Is this lost and found?"
sa2 "Yes it is, how can we help you?"
ew "I wanted to know if anyone turned in some items…"
sa2 "We don’t have any items that match your description, sorry. We’ll contact you if anything similar gets turned in."
ew "Thanks so much, have a good day!"
sa2 "You too."

#hide side StationAgent2

"Okay, I hate everything. I let out an exasperated groan into the air, leaning my lower back against the counter in the process."
"I really do try. I try to do everything right, try to be a good worker, and one stupid misstep has me out of my comfort zone."

###########################################################################################
###########################################################################################
########################################TO BE CONTINUED #######################################
###########################################################################################
###########################################################################################

#INT. EIR’S APARTMENT - EVENING (FRIDAY)
scene EirBedroomDusklighton

ew "Home sweet home!"
"It’s a cliche phrase, but I could shout it a million times right now. After the phone store trip from hell, I need any form of stress relief I can get."
ew "I got some leftovers from last night, so that’s one less thing I have to do."
"I quickly change into my pajamas after leaving my things at the door."
ew "Wait. No. I need to take my bag with me."
"The least I can do now is organize the new bag, since half the stuff in it’s gone anyways. "
"With that bitter thought, I drag my bag over to my bed and open it up. First step: cleaning out the business cards."
ew "Half of these have changed since I started my job anyways, this should make me feel a bit better."
"I remember my own business card in the middle of sorting, and then I realize."
ew "...I could call my phone, right?"
"Quickly, I grab my nice old brick of a personal cell phone and dial the number. This is it!"

$ renpy.pause(1.0)
play sound "Music_Box-Big_Daddy-1389738694.mp3"
$ renpy.pause()

"...I hear my phone. The new phone I had to buy today ring, and I wish I’d thought of all this earlier."
ew "I don’t know what to do."
"The only thing left is to continue organizing, maybe eat some of my feelings, and go to bed."

#INT. EIR’S OFFICE - MORNING (MONDAY)

scene bg grey

"The weekend ends up being a whole lot of nothing with a huge helping of self pity. "
"But I think it helps a little, as I go to work ready to finish Sheen 2.0 and get back to my regular life."
ew "Let’s do this!"

#TRANSITION GOES HERE#

"I didn’t realize how stir crazy I got at home until I checked the time. It’s 12:45, and Sheen 2.0 is finalized. Holy shit."
ew "Gotta report this one to the boss."
"With a newfound sense of triumph, I head up to report my progress."

show Jade

jl "Oh! I was just looking for you."
"My boss, composed as always, gives me a smile."

#show Jade Happy

jl "I’m assuming this is about Sheen 2.0?"
ew "It is, I just completed it."
jl "That’s great! I was about to go to a late lunch, would you care to come with me?"
ew "I’d love to!"
"We head off to whatever chic new place is in the area. Even though I’ve done this before, it still feels more that a little nerve wracking."

hide Jade

label Act_Two:

scene bg white
show text "Act 2" at truecenter with Pause (4)
hide text with dissolve

scene bg green

show Jade at right
show Eir at left

jl "So, I’d like to discuss the presentation with you a bit. What were your plans?"
ew "Well, both of the Sheen projects have had an emphasis on a clean composition."
ew "I’ve created a draft on Presi I think works well with this."
ew "In terms of content, I want to focus on the fact that this is a family owned business and appeal to the project’s goals by talking about the already existing Sheen community."
ew "If that makes sense?"
jl "It does, and it’s good thinking. Eir, you’ve gone above and beyond with these two projects."
jl "I wouldn’t be surprised if they tried to hire you permanently for in house work."
ew "I wouldn’t do that. After all, I’m only good here if I’m being honest."
jl "I appreciate your sentiments, but self deprecation is not a good look on you."
jl "You’re a stellar employee, and whether you stay here or go elsewhere, I can guarantee you’ll have a bright future."

show Eir Panic

ew "...thank you."
"I’m at a loss for words. It’s weird getting a pep talk at lunch. It’s weird thinking about how little confidence I have in myself when it comes to being “capable”."
"Still, if I focused on my low self esteem all day, I wouldn’t be able to present. And if my boss has faith in me, I think I can pull this thing off."

show Eir VHappy

ew "Thanks so much!"
jl "It’s no problem, now, shall we eat?"

#show Jade VHappy
"She gives me a refreshing smile as we finish our meals. Even though the losing my bag incident was just last week, it really feels like I’ve moved forward."

hide Eir
hide Jade

#INT. OFFICE - AFTERNOON
scene bg blue

ew "Hello, I’m Eir Warren for those who don’t know, and I’m the designer in charge of both of the Sheen projects. Today in my presentation I will talk about…"
"Even though I wanted to vomit five minutes earlier, when the words I practiced in the bathroom come out, they’re smooth and precise."
"I make sure to smile plenty, keep my voice at a good volume, and get through it quickly."

#TRANSITION HERE#

"Once I’m finished, Jade is the first one to speak."

#show Jade Proud

jl "Ms. Warren is a fantastic asset for our company, and I hope you’ve been satisfied with her performance."
rep "It was a great presentation. Thank you in assisting our company’s path forward Ms. Warren."
ew "It was my pleasure."
"After another flurry of handshakes, introductions, and contact information being exchanged, I’m beckoned by Jade to follow her."

hide Jade

#INT. EIR’S OFFICE - AFTERNOON

scene bg grey

jl "Great job today! I think we’re going to have many more Sheen projects in the future. Do you think it’s a little early for a drink?"
ew "Uh, I don’t kn--"
jl "It is, isn’t it? It’s not even three yet. We can get drinks another time, right?"
ew "Right…"
"I should feel good about all the praise, but I don’t feel I deserve it. Not after losing my bag like I did."
jl "You look like you’re beating yourself up again."
ew "I’m just thinking, it’s nothing to worry about."
jl "I understand I’m your boss, and that naturally provides a sense of distance. But if you do need some assistance with work, let me know. You’ve earned it."
ew "Thank you, I really appreciate it."

# show Jade Proud

jl "And I really do mean it."

hide Jade

#[Change of POV--TROY]

#INT. TROY’S APARTMENT - DAY

scene bg purple grey

tc "Sorry in advance mysterious bag owner."
"I’ve been stuck with this bag for too long, but that’s about to change. This is a little weird, sure, but it’s the only thing I can think of."
tc "Here we go..."
"I gently empty out the contents of the bag onto my floor, and immediately reach for the laptop. I open it up."
tc "Password protected...Not what I was expecting given the phone situation but yet somehow... Let’s see if there’s anything else I can dig through."
"The planner catches my eye, and I open it, feeling incredibly creepy in the process."
tc "Thank god this person’s organized."
"I find three events coming up on the planner today. I don’t want to be that guy, but maybe if I can get to one of these places, I can return the bag to whoever it belongs to."

menu Planner:
    "How should I do this though?"
    "Go to the events in the order the planners lists.":
        scene purple grey
        tc "Well, I have my bike, let’s hope I get somewhere on time."
        "I bike over to the first location, only to be stuck in a traffic jam and forced to detour to the next location."
        show Troy at left
        "I manage to get a decent spot on a bike rack a few steps away from what looks like a large corporate building."
        tc "I feel like a bull in a china shop."
        "I’m dressed pretty casually, so every step I take inside the building is an awkward one. When I spot the receptionist, I give her a polite smile"
        #show FrontDeskLady
        fdl "How can I help you?"
        tc "I’m here to return a bag, it belongs to an Eir Warren?"
        fdl "Oh, Ms. Warren!"
        #show Troy Intense
        "Jackpot"
        #show Troy
        tc "You’ve heard of her? I found her bag the other--"
        fdl "She’s been here before, but she doesn’t work here. Sorry about that."
        tc "Oh, Thanks for helping me out, have a good day."
        fdl "You too."
        #hide FrontDeskLady
        #show Troy Sad
        "I hop back on my bike and go to the last location, which I hope works. I don’t know a thing about Eir Warren, but she’s making this difficult for me."
        #hide Troy
        #TRANSITION GOES HERE#

        scene pink grey
        "Eventually, I reach the last place. I don’t bother to be shy about heading towards the building."
        "As soon as I enter I realize this isn't going to go my way, everyone is tapping badges to pass through a security turnstile"
        tc "And I need an ID badge. Great."
        "I look around to see if anyone can let me in, but it’s no use."
    #"Go to the events in reverse order":
        #block of code to run


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
