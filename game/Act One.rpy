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
"I glance at the clock then around the office. No one is heading my way, no one is looking at me funny. "
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

call txt_startEir from _call_txt_startEir

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

