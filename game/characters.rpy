image Troy = "images/by_deji/Troy_Neutral.png"
image Troy Bored = "images/by_deji/Troy_Bored.png"
image Troy Happy = "images/by_deji/Troy_Happy.png"
image Troy VHappy = "images/by_deji/Troy_VHappy.png"
image Troy Angry = "images/by_deji/Troy_Angry.png"
image Troy Blush = "images/by_deji/Troy_Blush.png"
image Troy Embarrassed = "images/by_deji/Troy_Embarrassed.png"
image Troy Panic = "images/by_deji/Troy_Panic.png"

image Eir = "images/by_deji/Eir_Neutral.png"
image Eir Happy = "images/by_deji/Eir_Happy.png"
image Eir VHappy = "images/by_deji/Eir_VHappy.png"
image Eir Angry = "images/by_deji/Eir_Angry.png"
image Eir Bored = "images/by_deji/Eir_Bored.png"
image Eir Embarrassed = "images/by_deji/Eir_Embarrassed.png"
image Eir Panic = "images/by_deji/Eir_Panic.png"

image Jade = "images/by_deji/Jade_Neutral.png"
image side Karla = "images/by_deji/Karla_Neutral.png"
image side Karla Bored = "images/by_deji/Karla_Bored.png"
image side Courtney = "images/by_deji/Courtney_Neutral.png"
image side Courtney Happy = "images/by_deji/Courtney_Happy.png"

image Coworker1 = "images/by_deji/Coworker1_Neutral.png"
image Coworker1 Blush = "images/by_deji/Coworker1_Blush.png"
image Coworker1 Embarrassed = "images/by_deji/Coworker1_Embarrassed.png"
image Coworker2 = "images/by_deji/Coworker2_Neutral.png"
image Coworker3 = "images/by_deji/Coworker3_Neutral.png"
image ItGuy = "images/by_deji/ItGuy_Neutral.png"
image psgEmployee = "images/by_deji/StoreEmployee_Bored.png"
image side StationAgent1 = "images/by_deji/StationAgent_Neutral.png"
#image StationAgent2
#image side StationAgent2 = "images/by_deji/StationAgent2_Neutral.png"
#image Guard1
#image Guard2
#image FrontDesk

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
