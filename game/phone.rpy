#################################################################################
########################PHONE CODE GOES HERE#####################################
#################################################################################
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

    yadj = ui.adjustment()

    def eir(txt, who=False, sound=False):
        store.m_msg.append((who, txt, sound))
        store.yadj.value = store.yadj.range+300
        renpy.restart_interaction()
        renpy.pause()
    def kstar(txt, who=False, sound=False):
        store.m_msg.append((who, txt, sound))
        store.yadj.value = store.yadj.range+300
        renpy.restart_interaction()
        if who:
            renpy.play("music/new_message.mp3", "sound")
        renpy.pause()
    def troy(txt, who=False, sound=False):
        store.m_msg.append((who, txt, sound))
        store.yadj.value = store.yadj.range+300
        renpy.restart_interaction()
        renpy.pause()
    def kingcourt(txt, who=False, sound=False):
        store.m_msg.append((who, txt, sound))
        store.yadj.value = store.yadj.range+300
        renpy.restart_interaction()
        if who:
            renpy.play("music/sms-alert-5-daniel_simon.mp3", "sound")
        renpy.pause()
    def del_last_msg():
        if len(store.m_msg) > 0:
            del store.m_msg[-1]

    def del_all_msg():
        store.m_msg = []


screen EirPhone(who, what):
    frame background "gui/Hurricane_Like_Me/Handphone/Handphone.png" xysize (600,675) align (0.9,.4):
        frame background None xysize (560, 510) align (0.5,0.58):
            viewport id "vp_msg" mousewheel True  yadjustment yadj:
                vbox spacing 15 xsize 550 xalign 0.4 box_reverse True:
                    for message in m_msg[::-1]:
                        $ who, txt, sound = message
                        $ xgn = 0.0 if who else 1.0
                        if sound:
                            imagebutton auto "messenger/sound_%s.png" xalign xgn action Play("sound", sound)
                        else:
                            if eir:
                                button xalign xgn xmaximum 580 xpadding 20 ypadding 10 background Frame("messenger/eir.png", 25, 25):
                                    text "%s"%(txt) style "txt_base"
                            elif kstar:
                                button xalign xgn xmaximum 580 xpadding 20 ypadding 10 background Frame("messenger/karla.png", 25, 25):
                                    text "%s"%(txt) style "txt_base"
        #Senders Name And Information
        text "%s"%(msg_name) style "txt_base" size 35 xalign 0.31 xanchor 0.0 yalign 0.04
        #Senders Avatar
        add "messenger/av/"+msg_name.lower().replace(' ', '_')+".png" pos (100,27)
        #Arrow
        imagebutton auto "messenger/arr_%s.png" pos (10, 33) action NullAction()
        #Erase Messages
        button background style_button_inst hover_background style_button_hovr xalign 0.99 yalign 0.03 action Function(del_all_msg) xysize (60,60):
            text "  x  " style "txt_base" size 40 pos (36, -2)
        #Scroller on Side
        vbar value YScrollValue("vp_msg") style "bar_vert"

screen TroyPhone(who, what):
    frame background "gui/Hurricane_Like_Me/Handphone/Handphone-Purple.png" xysize (600,675) align (0.9,.4):
        frame background None xysize (560, 510) align (0.5,0.58):
            viewport id "vp_msg" mousewheel True  yadjustment yadj:
                vbox spacing 15 xsize 550 xalign 0.4 box_reverse True:
                    for message in m_msg[::-1]:
                        $ who, txt, sound = message
                        $ xgn = 0.0 if who else 1.0
                        if sound:
                            imagebutton auto "messenger/sound_%s.png" xalign xgn action Play("sound", sound)
                        else:
                            if troy:
                                button xalign xgn xmaximum 580 xpadding 20 ypadding 10 background Frame("messenger/troy.png", 25, 25):
                                    text "%s"%(txt) style "txt_base"
                            elif kingcourt:
                                button xalign xgn xmaximum 580 xpadding 20 ypadding 10 background Frame("messenger/courtney.png", 25, 25):
                                    text "%s"%(txt) style "txt_base"
        #Senders Name And Information
        text "%s"%(msg_name) style "txt_base" size 35 xalign 0.31 xanchor 0.0 yalign 0.04
        #Senders Avatar
        add "messenger/av/"+msg_name.lower().replace(' ', '_')+".png" pos (100,27)
        #Arrow
        imagebutton auto "messenger/arr_%s.png" pos (10, 33) action NullAction()
        #Erase Messages
        button background style_button_inst hover_background style_button_hovr xalign 0.99 yalign 0.03 action Function(del_all_msg) xysize (60,60):
            text "  x  " style "txt_base" size 40 pos (36, -2)
        #Scroller on Side
        vbar value YScrollValue("vp_msg") style "bar_vert"
#################################################################################


#################################################################################
########################PHONE CODE ENDS HERE#####################################
#################################################################################