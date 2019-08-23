# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cwPete = Character("Pete")
define cwCallahan = Character("Callahan")
define ew = Character("Eir")
define ewChibi = Character("Inner Eir", image="ewChibi")

define chibi_deadpanned = "images/by_RoseSense/Eir_Chibi_Deadpanned.png"
define chibi_panicked = "images/by_RoseSense/Eir_Chibi_Panicked.png"
define chibi_angry = "images/by_RoseSense/Eir_Chibi_Angry.png"

# The game starts here.

label start:

show Troy at right

show cwCallahan at right

cwCallahan "Excuse me Eir?"

show screen thought ("{i}Ugh{/i}, not this guy again.", chibi_panicked, 'right')
show Eir Happy
cwCallahan "Excuse me Eir?{fast}"

show screen thought ("TEST TEXT LEFT.", chibi_deadpanned, 'left')
show Eir Work Happy at left
cwCallahan "Excuse me Eir? TEST"

show screen thought ("TEST TEXT CENTER", chibi_angry, 'center')
show Eir PJs Happy at center
cwCallahan "Excuse me Eir? TEST THREE"



hide screen thought

#ewChibi "{i}Ugh{/i}, not this guy again."



ew "Yes? How can I help?"
cwCallahan "Could you deal with the Johnsons? They’re outside."
ew "Sure! I’ll be right there."
hide cwCallahan
hide Eir
"After a quick chat with the Johnsons, and no help from my coworker, I return to my desk."
" Sheen project, I’m coming for--"
show cwAubrey at right #Panic
cwAubrey "Eir? Oh thank god you’re here!"
show Eir Work Panic at left

##############################################################
##############################################################

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

hide Eir

##############################################################
############################VIA TEXT############################
##############################################################
window hide
show screen EirPhone()
#call txt_startEir
$ del_all_msg()
$ eir ("Because it takes too long geez. Sometimes people are lazy aka me and all I want to do is swipe and there it is. No fuss no muss.")
$ kstar ("Why don’t you have a lock on your phone? That’s like phone having 101 right here.")
$ kstar ("Christ, how are you an adult?")
$ eir ("I ask myself that every day. One day I’m going to look up and realize I’m thirty and have no idea how that happened to me.")
$ kstar ("It happens to the best of us.")
$ kstar ("Anyway i guess it’s a good thing that you don’t lock your phone. Also that in the year of twenty seventeen you have a landline. Like who even has one of those.")
$ eir ("It came with the apartment and its connected to my bell")
$ kstar ("I’m not judging its handy dandy for this exact moment.")

hide screen EirPhone
window show

##############################################################
############################NOT  TEXT############################
##################################S############################

show screen thought ("TEST TEXT CENTER", chibi_angry, 'center')

hide screen thought
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


##############################################################
##############################################################

menu:
    "What should I do?"

    "Drink coffee.":
        "I drink the coffee, and it's good to the last drop."
    "Drink tea.":
        "I drink the tea, trying not to make a political statement as I do."
    

##############################################################
##############################################################

return
