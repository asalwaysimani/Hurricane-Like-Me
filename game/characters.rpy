###################################################################################
##################################CHARACTERS#######################################
###################################################################################

define ew = Character("Eir", image="Eir")
define kj = Character("Karla", image="Karla")
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

###################################################################################
####################################IMAGES#########################################
###################################################################################

layeredimage Eir:
    always:
        "EirBase"
    group outfit:
        attribute Casual default:
            "EirCasual"
        attribute work:
            "EirWork"
        attribute PJs:
            "EirPJsSweats"
    group position:
        attribute Front default:
            "EirFrontFace"
        attribute Side:
            "EirSide"
    group face:
        attribute Neutral default:
            "EirNeutral"
        attribute Tired:
            "EirTired"
        attribute Surprised:
            "EirSurprised"
        attribute Angry:
            "EirAngry"
        attribute Happy:
            "EirHappy"
        attribute Agitated:
            "EirAgitated"
        attribute Confused:
            "EirConfused"
        attribute Panic:
            "EirPanic"

layeredimage Troy:
    always:
        "TroyBase"
    group outfit:
        attribute Casual default:
            "TroyCasual"
        attribute Barista:
            "TroyBarista"
        attribute BikeMessenger:
            "TroyBike"
    group position:
        attribute Front default:
            "TroyFrontFace"
        attribute Side:
            "TroySide"
    group face:
        attribute Neutral:
            "TroyNeutral"
        attribute Tired:
            "TroyTired"
        attribute Surprised:
            "TroySurprised"
        attribute Happy:
            "TroyHappy"
        attribute Excited:
            "TroyExcited"
        attribute Intense:
            "TroyIntense"


image Jade = "images/by_deji/Jade_Neutral.png"
image side Karla = "images/by_deji/Karla_Neutral.png"
image side Karla Bored = "images/by_deji/Karla_Bored.png"
image side Courtney = "images/by_deji/Courtney_Neutral.png"
image side Courtney Happy = "images/by_deji/Courtney_Happy.png"

image cwPete = "images/by_deji/Coworker2_Neutral.png"
#image cwPete Blush = "images/by_deji/Coworker2_Blush.png"
#image cwPete Embarrassed = "images/by_deji/Coworker2_Embarrassed.png"
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

