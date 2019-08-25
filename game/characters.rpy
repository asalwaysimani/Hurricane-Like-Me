init:   
    transform half_size:
            size (400,1114) crop(0,0,806,2244)
            on show:
                yalign 610 xalign 0.5


###################################################################################
##################################CHARACTERS#######################################
###################################################################################

define ew = Character("Eir", image="Eir")

define kj = Character("Karla", image="Karla")
define ewChibi = Character("Inner Eir", image="ewChibi", kind = nvl)
define tc = Character("Troy", image="Troy")
define ct = Character("Courtney", image="Courtney")
define jl = Character("Jade", image="Jade")
define cwPete = Character("Coworker Pete")
define cwAubrey = Character("Coworker Aubrey")
define cwCallahan = Character("Coworker Callahan")
define cwMarcia = Character("Barista Marcia")
define cwHarvey = Character("Barista Harvey")
define cwJulia = Character("Manager Julia")
define sa1 = Character("Station Agent Mindy")
define sa2 = Character("Station Agent Jenny")
define itg = Character("Steve, the IT Guy")
define psg = Character("Customer Service Rep Alan")
define rep = Character("Sheen Representative")
define fdl = Character("Receptionist Jenny")
define ewChibi = Character("Inner Eir", image="ewChibi")
#define chibi_deadpanned = "images/by_RoseSense/Eir_Chibi_Deadpanned.png"
#define chibi_panicked = "images/by_RoseSense/Eir_Chibi_Panicked.png"
#define chibi_angry = "images/by_RoseSense/Eir_Chibi_Angry.png"
###################################################################################
####################################IMAGES#########################################
###################################################################################

layeredimage ewChibi:
    group expressions:
        attribute deadpanned default:
            "images/by_RoseSense/Eir_Chibi_Deadpanned (1).png"
        attribute panicked:
            "images/by_RoseSense/Eir_Chibi_Panicked (1).png"
        attribute angry:
            "images/by_RoseSense/Eir_Chibi_Angry (1).png"
    #group moodlets:
    #    attribute embarrassed:
    #    attribute intense:
    #    attribute tired:
    #    attribute surprised:

layeredimage Eir:
    group outfit:
        attribute Casual default:
            "images/by_Sysen/Eir/Casual.png"
        attribute Work:
            "images/by_Sysen/Eir/Work.png"
        attribute PJs:
            "images/by_Sysen/Eir/PJs.png"
    group expressions:
        attribute Neutral default:
            "images/by_Sysen/Eir/Neutral.png"
        attribute Embarrassed:
            "images/by_Sysen/Eir/embarrassed.png"
        attribute Intense:
            "images/by_Sysen/Eir/intense.png"
        attribute Tired:
            "images/by_Sysen/Eir/Tired.png"
        attribute Surprised:
            "images/by_Sysen/Eir/Surprised.png"
        attribute Angry:
            "images/by_Sysen/Eir/Angry.png"
        attribute Happy:
            "images/by_Sysen/Eir/Happy.png"
        attribute Agitated:
            "images/by_Sysen/Eir/Agitated.png"
        attribute Confused:
            "images/by_Sysen/Eir/Confused.png"
        attribute Panic:
            "images/by_Sysen/Eir/Panic.png"

#image Troy:
#    "images/by_Sysen/Troy/"

layeredimage Troy:
    group outfit:
        attribute Casual default:
            "images/by_Sysen/Troy/Casual.png"
        attribute Barista1:
            "images/by_Sysen/Troy/Barista1.png"
        attribute Barista2:
            "images/by_Sysen/Troy/Barista2.png"
        attribute BikeMessenger:
            "images/by_Sysen/Troy/Bike.png"
    group accessories:
        attribute Glasses:
            "images/by_Sysen/Troy/glasses.png"
        attribute Mask:
            "images/by_Sysen/Troy/mask.png"
    group expressions:
        attribute Neutral:
            "images/by_Sysen/Troy/Neutral.png"
        attribute Bored:
            "images/by_Sysen/Troy/Bored.png"
        attribute Tired:
            "images/by_Sysen/Troy/Tired.png"
        attribute Surprised:
            "images/by_Sysen/Troy/Surprised.png"
        attribute Happy:
            "images/by_Sysen/Troy/Happy.png"
        attribute Excited:
            "images/by_Sysen/Troy/Excited.png"
        attribute Intense:
            "images/by_Sysen/Troy/Intense.png"


image Jade = "images/by_deji/Jade_Neutral.png"
image side Karla = "images/by_deji/Karla_Neutral.png"
image side Karla Bored = "images/by_deji/Karla_Bored.png"
image side Courtney = "images/by_deji/Courtney_Neutral.png"
image side Courtney Happy = "images/by_deji/Courtney_Happy.png"

image cwPete = "images/by_deji/Coworker2_Neutral.png"
image cwPete Blush = "images/by_deji/Coworker2_Blush.png"
image cwPete Embarrassed = "images/by_deji/Coworker2_Embarrassed.png"
image cwAubrey = "images/by_deji/Coworker1_Neutral.png"
image cwCallahan = "images/by_deji/Coworker3_Neutral.png"
image ItGuy = "images/by_deji/ItGuy_Neutral.png"
image psgEmployee = "images/by_deji/StoreEmployee_Bored.png"
image side StationAgent1 = "images/by_deji/StationAgent_Neutral.png"
#image StationAgent2
image side StationAgent2 = "images/by_deji/StationAgent2_Neutral.png"
#image Guard1
#image Guard2
#image FrontDesk

###################################################################################
##################################INFO SCREENS#####################################
###################################################################################

init python:
    xmax = config.screen_width
    ymax = config.screen_height
init -2 python:
    #declares a new style called "infoscreen"
    style.infoscreen = Style(style.default)
    style.infoscreen_text.size = 25
    style.infoscreen_window.background = "infoscreenBG.png"  #<-- This puts a custom background in the area that displays the text and picture
    style.infoscreen_frame.background = Frame("box.png", 10, 10) #<--same as above, but in the area that displays the buttons
    #style.infoscreen_button.idle_background = Frame("box2.png", 10, 10)
    style.infoscreen_button.hover_background = Frame("box3.png", 10, 10)
    style.infoscreen_button_text.idle_color = "#000000"
    style.infoscreen_button_text.hover_color = "#000000"
    style.infoscreen_button_text.selected_color = "#000000"
    style.infoscreen_button.top_padding = 5
    style.infoscreen_button.bottom_padding = 5
    #style.infoscreen_bar.left_bar = "bar_full-checks.png"
    style.infoscreen_bar.right_bar = "bar_empty-checks.png"
    style.infoscreen_bar.xmaximum = 209
    style.infoscreen_bar.ymaximum = 34
    style.infoscreen_bar.right_gutter = 0
    style.infoscreen_bar.left_gutter = 0
    style.infoscreen_bar.thumb = None

###################################################################################
#################################CHARACTER INFO####################################
###################################################################################


init python:

    class char:
        def __init__(self, names, bloodType, age, birthday, sign):
            self.names = names
            self.bloodType = bloodType
            self.age = age
            self.birthday = birthday
            self.sign = sign

init 1:
    $ Eir = char(
    names="Eir Warren",
    bloodType="",
    age="",
    birthday="",
    sign="",
    )

