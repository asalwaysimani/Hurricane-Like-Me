#################################################################################
########################PHONE CODE GOES HERE#####################################
#################################################################################


#OPTIONS PAGE FROM THE zPHONE TEMPLATES TUTORIAL#
# Picking up the phone
transform txt_pickup:
    yalign 1.0 xalign 0.5
    yoffset 900
    easein 0.3 yoffset 100

# End the phone conversation
transform txt_hide:
    yalign 1.0 xalign 0.5
    yoffset 100
    easein 0.3 yoffset 1300   
    

transform txt_msg_bubble_tip:
    xoffset 10
    yoffset 1
    
transform txt_msg_bubble_tip2:
    xoffset 165
    yoffset 1

transform scrolling_out_txt:
    easeout 0.1 yoffset -30 alpha 0
        
transform incoming_msg:
    yoffset 100
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message

#### labels to shortcut stuff so you dont need to copypaste stuff repeatedly! #####

label txt_startEir:
    window hide
    show EirPhone at txt_pickup
    $ renpy.pause(0.2)
    return

label txt_startTroy:
    window hide
    show TroyPhone at txt_pickup
    $ renpy.pause(0.2)
    return

    
label txt_msg:
    $ renpy.pause()
    hide screen txt_msg
    $ renpy.pause(0.1)
    return
        
label txt_msg2:
    $ renpy.pause()
    hide screen txt_msg2
    $ renpy.pause(0.1)
    return

label txt_msg3:
    $ renpy.pause()
    hide screen txt_msg3
    $ renpy.pause(0.1)
    return

label txt_msg1:
    $ renpy.pause()
    hide screen txt_msg1
    $ renpy.pause(0.1)
    return

label txt_after_menu:
    hide screen txt_msg
    hide screen txt_msg2
    hide screen txt_msg3
    hide screen txt_msg1
    $ renpy.pause(0.1)
    return    
    
label txt_end:
    $ renpy.pause()
    hide screen txt_msg
    hide screen txt_msg2
    hide screen txt_msg3
    hide screen txt_msg1
    show phone at phone_hide #Show phone refers to image that is phone
    $ renpy.pause(0.2)
    return

label txt(who, what):
    $ renpy.pause()
    hide screen txt_msg
    hide screen txt_msg2
    hide screen txt_msg3
    hide screen txt_msg1
    $ renpy.pause(0.1)
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "me":
        show screen txt_msg2(who, what)
    else:
        show screen txt_msg(who, what)
    return
    
label reply_txt(who, what):
    $ renpy.pause()
    hide screen txt_msg
    hide screen txt_msg2
    hide screen txt_msg3
    hide screen txt_msg1
    $ renpy.pause(0.1)
    show screen txt_msg3(who,what)
    return

label msg_img(who, what,img):
    $ renpy.pause()
    hide screen txt_msg
    hide screen txt_msg2
    hide screen txt_msg3
    hide screen txt_msg1
    $ renpy.pause(0.1)
    show screen phone_message_image(who, what,img)
    return

label msg_start(who, what):
    # if you want to change the players name to be something else than "me" you can change it here
    if who.lower() == "me":
        show screen txt_msg2(who, what)
    else:
        show screen txt_msg(who, what)
    return 
    

init 5:
    style txt_msg_vbox:
        xalign 0.5
        yalign 0
        ypos 380
        xsize 360
        xoffset -40
    
    style txt_menu:
        size 18
        ypadding 10
        xpadding 10

    style txt_msg_frame:
        ypadding 10
        xpadding 10

    style txt_msg_frame2:
        ypadding 10
        xpadding 10
    
    style txt_msg_contents:
        spacing 10
    
    style txt_msg is say_dialogue:
        xoffset 0
        outlines []
        xalign 1
        yalign 0

    style txt_msg2 is say_dialogue:
        xoffset 0
        outlines []
        xalign 1
        yalign 0

    style txt_msg_who is txt_msg:
        size 25

    style txt_msg_what is txt_msg:
        size 24

    style reply_txt is default:
        size 18
        xalign 0.5
        xsize 475
        ypadding 10
        xpadding 10

screen txt_msg(who,what):
    vbox at incoming_msg:
        style_group "txt_msg"

screen txt_msg2(who, what):
    vbox at incoming_message:
        style_group "txt_msg"
        xoffset -584        
        xalign 1.0
        # this one adds the triangular tip for the bubble, if you change colors you change this images too

        frame:
            style_group "txt_msg2"
            xsize 200

            vbox:
                style "txt_msg_contents"
                text who style "txt_msg_who"
                text who style "txt_msg_what"

screen txt_msg3(who, what):
    vbox at incoming_message:
        style_group "txt_msg"
        xoffset -584
        xalign 1.0
        # this one adds the triangular tip for the bubble, if you change colors you change this images too

        frame:
            style_group "txt_msg2"
            xsize 200

            vbox: 
                style "txt_msg_contensts"
                text what style "txt_msg_what"

init python:

    style_button_back = "#282E33"
    style_button_hovr = "#5F6C77"
    style_button_inst = "#14171A"

    style.btn = Style(style.default)
    style.btn.background = style_button_back
    style.btn.hover_background = style_button_hovr
    style.btn.insensitive_background = style_button_inst

    style.bar_vert = Style(style.default)
    style.bar_vert.right_bar = style_button_inst
    style.bar_vert.left_bar = style_button_inst
    style.bar_vert.thumb = style_button_hovr
    style.bar_vert.bar_vertical = True
    style.bar_vert.bar_invert = True
    style.bar_vert.xalign = 1.0
    style.bar_vert.yalign = 0.6
    style.bar_vert.xsize = 10
    style.bar_vert.ysize = 780

    style.txt_base = Style(style.default)
    style.txt_base.font = "fonts/Montserrat-Medium.ttf"
    style.txt_base.xalign = 0.5
    style.txt_base.yalign = 0.5
    style.txt_base.size = 30
    style.txt_base.color = "#fff"

#######Phone Choice Buttons go here#######

screen txt_msg():
    
    #style_prefix "choice"

    #vbox:
    #    for i in items:
    #        textbutton i.caption action i.action

    window:
        style "phone_choice"
        xalign 0.5
        yalign 0.5

        vbox:
            style "phone_menu"
            spacing 2
            for caption, action, chosen in [("test","test2","test3")]:
                if action:
                    if chosen:
                        button:
                            action action
                            style "phone_choice_chosen_button"
                            text caption style "phone_choice_chosen"
                    else:
                        button:
                            action action
                            style "phone_choice_button"
                            text caption style "phone_choice"
                else:
                    text caption style "phone_caption"

init python:
    style.phone_choice_button.background = Frame("gui/Hurricane_Like_Me/Phone_Choice/Base.png", 44,44)
    style.phone_choice_button.hover_background = Frame("gui/Hurricane_Like_Me/Phone_Choice/Bottom_Select_Hover.png", 44, 44)
    style.phone_choice_chosen_button.background = Frame("gui/Hurricane_Like_Me/Phone_Choice/Upper-select_Hover.png", 44, 44)
    style.phone_choice_chosen_button.hover_background = Frame("gui/Hurricane_Like_Me/Phone_Choice/Upper-select_Idle.png", 44,44)

    style.phone_choice.color = "#ffffff"
    style.phone_choice_chosen.color = "#ffffff"
    style.phone_choice.size = 18

    yadj = ui.adjustment()
    store.m_msg = []

    def eir(txt, sound=False):
        store.m_msg.append(("EirBody", txt, sound))
        store.yadj.value = store.yadj.range+300
        renpy.restart_interaction()
        renpy.pause()
    
    def kstar(txt, sound=False):
        store.m_msg.append(("KStar", txt, sound))
        store.yadj.value = store.yadj.range+300
        renpy.restart_interaction()
        renpy.play("music/sfx/new_message.mp3", "sound") #new_message is eirs ringtone for text
        renpy.pause()
    
    def troy(txt, alert=False, sound=False):
        store.m_msg.append(("TroyBoy", txt, sound))
        store.yadj.value = store.yadj.range+300
        renpy.restart_interaction()
        if alert:
            renpy.play("music/sfx/new_message.mp3", "sound") #new_message is eirs ringtone for text
        renpy.pause()
    
    def kingcourt(txt, sound=False):
        store.m_msg.append(("KingCourt", txt, sound))
        store.yadj.value = store.yadj.range+300
        renpy.restart_interaction()
        renpy.play("music/sfx/sound_message.mp3", "sound") #sound_message is Troys ringtone for text
        renpy.pause()
    
    def del_last_msg():
        if len(store.m_msg) > 0:
            del store.m_msg[-1]

    def del_all_msg():
        store.m_msg = []

screen Handphone(msg_name):
    frame:
        if msg_name == "eir":
            background "gui/Hurricane_Like_Me/Handphone/Handphone.png" xysize (600,675) align (0.9, .05 )# CHANGE POSISTION OF BACKGROUND VIA PHOTOSHOP, needs to be centered
        else:
            background "gui/Hurricane_Like_Me/Handphone/Handphone-Purple.png" xysize (600,675) align (0.9,.4) # CHANGE POSISTION OF BACKGROUND VIA PHOTOSHOP, needs to be right justified

        #"messenger/" + msg_name +"/background.png (SHOULD BE HANDPHONE FOLDER FIGURE IT OUT)
        
        #frame background None xysize (560, 510) align (0.5,0.58):
        viewport id "vp_msg" mousewheel True  yadjustment yadj: #position of text msg in phone
            xsize 490
            ysize 770
            xpos 60
            ypos 160
            scrollbars "vertical"

            vbox spacing 15 box_reverse True:
                for message in m_msg[::-1]:
                    $ who, txt, sound = message
                    #$ xgn = 0.0 if who else 1.0
                    if sound:
                        imagebutton auto "messenger/sound_%s.png" xalign xgn action Play("sound", sound)
                    else:
                        frame:
                            background "gui/Hurricane_Like_Me/Handphone/%stextbox.png" % msg_name
                            xmaximum 580
                            ysize 115

                            image "gui/Hurricane_Like_Me/Handphone/AVI/%s.png" % who:
                                xpos 5
                                ypos 5
                            text who:
                                xpos 130
                                ypos -3
                                size 25

                            text txt:
                                xpos 130
                                xsize 330
                                ypos 35
                                color "#000"
                                size 18
                                line_spacing .2

screen EirPhone():
    use Handphone("eir")
    
screen TroyPhone():
    use Handphone("troy")
#################################################################################




#################################################################################
########################PHONE CODE ENDS HERE#####################################
#################################################################################