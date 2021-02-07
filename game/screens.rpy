################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what, side_image=None):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

##########################################
########Eir thought bubbles windows#######
##########################################

screen thought(what, side_image=None, alignment='right'):
    style_prefix "thoughtbox"
    zorder 10

    frame:
        background None
        xfill True
        at thoughtbox_transform
        
        window:
            if alignment == 'right':
                xalign 1.0
                add side_image xpos -300 yalign 0.0
            elif alignment == 'center':
                xalign 0.6
                add side_image xpos -300 yalign 0.0
            else:
                xalign 0.0
                add side_image xpos 750 yalign 0.0
            text what
            
transform thoughtbox_transform:
    on appear:
        ypos -500
        linear 0.3 ypos 0
    on show:
        ypos -500
        linear 0.3 ypos 0
    on hide:
        linear 0.3 ypos -500

##########################################
########END OF THOUGHT BUBBLE CODE########
##########################################


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/Hurricane_Like_Me/Textbox/Textbox.png", xalign=0.5, yalign=1.0)

style thoughtbox_window:
    xalign 0
    xpos 1020
    xsize 874
    yalign gui.thoughtbubble_yalign
    #ysize 500 #gui.thoughtbubble_height
    #L R T B
    padding (50, 20, 100, 80)

    background Frame("gui/Hurricane_Like_Me/Thought/Thought.png", left=430, right= 380, top=0, bottom=115)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    #background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style EirThoughts:
    xpos gui.thoughtbubble_xpos
    xanchor gui.thoughtbubble_xalign
    xsize gui.thoughtbubble_width
    ypos gui.thoughtbubble_ypos
    ysize gui.thoughtbubble_height

    background Frame("gui/Hurricane_Like_Me/Thought/Thought.png", gui.thoughtbubble_borders, title=gui.thoughtbubble_tile, xalign=gui.thoughtbubble_xalign)
    padding gui.thoughtbubble_borders.padding
    

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    #style_prefix "choice"

    #vbox:
    #    for i in items:
    #        textbutton i.caption action i.action

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2
            for caption, action, chosen in items:
                if action:
                    if chosen:
                        button:
                            action action
                            style "menu_choice_chosen_button"
                            text caption style "menu_choice_chosen"
                    else:
                        button:
                            action action
                            style "menu_choice_button"
                            text caption style "menu_choice"
                else:
                    text caption style "menu_caption"

init python:
    ###Choice Buttons go here
    style.menu_choice_button.background = Frame("gui/Hurricane_Like_Me/Choice/1Idle.png", 44,44)
    style.menu_choice_button.hover_background = Frame("gui/Hurricane_Like_Me/Choice/1Hover.png", 44, 44)
    style.menu_choice_chosen_button.background = Frame("gui/Hurricane_Like_Me/Choice/2Idle.png", 44, 44)
    style.menu_choice_chosen_button.hover_background = Frame("gui/Hurricane_Like_Me/Choice/2Hover.png", 44,44)

    #Customize font and color
    style.menu_choice.color = "#ffffff"
    style.menu_choice_chosen.color = "#ffffff"
    style.menu_choice.size = 22

init -2:
    $ config.narrator_menu = True
    style menu_window is default
    style menu_choice is button_text:
        clear
    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.44)
        xmaximum int(config.screen_width * 0.77)

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


define hotspotCoords = [
(),
(1397, 450, 45, 45), # Island
(986, 450, 45, 45), # Red-Blue Intersection Top
(838, 997, 45, 45), # Very bottom Blue
(519, 732, 45, 45), # Red-Pink Intersection Bottom Left
(374, 293, 45, 45), # Very Left Red
]

screen choice_map(items):

    imagemap:

        ground "gui/Hurricane_Like_Me/Map/idle_hor.png"
        idle "gui/Hurricane_Like_Me/Map/selected_hor.png"
        hover "gui/Hurricane_Like_Me/Map/selected_hor.png"

        for x in items:

            hotspot store.hotspotCoords[ x.kwargs["spot"] ]:
                action x.action 
                at mapHover 

transform mapHover():

    on idle:
        alpha 1.0
        linear 0.7 alpha 0.0
        linear 0.7 alpha 1.0
        repeat

    on hover:
        alpha 1.0


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Report an error") action OpenURL ("https://goo.gl/forms/e6kKdM6WdDIffhIj2")
            textbutton _("Prefs") action ShowMenu('Options')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

default _game_menu_screen = "navigation"

screen navigation():

    modal True

    add "gui/Hurricane_Like_Me/Menu/bg.png"

    imagemap:
        align (0.5, 0.5)
        ground None
        idle "gui/Hurricane_Like_Me/Menu/Menu-Idle.png"
        hover "gui/Hurricane_Like_Me/Menu/Menu-Hover.png"

        hotspot (188, 400, 317, 65) action Return()
        hotspot (198, 472, 295, 65) action ShowMenu("load")
        hotspot (208, 549, 277, 65) action ShowMenu("save")
        hotspot (234, 627, 225, 65) action ShowMenu("Options")
        hotspot (273, 704, 145, 65) action MainMenu()

    key "game_menu" action Return()


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.

    style_prefix "main_menu"

    tag menu 

    add "gui/Hurricane_Like_Me/TitleScreen/background.png"

    # Patreon
    imagebutton:
        pos (0, 155)
        idle "gui/Hurricane_Like_Me/TitleScreen/Button_Patreon.png"
        hover "gui/Hurricane_Like_Me/TitleScreen/Button_Patreon_Hover.png"
        action OpenURL("https://www.patreon.com/MargaretCatterDev")

    # Discord
    imagebutton:
        pos (0, 260)
        idle "gui/Hurricane_Like_Me/TitleScreen/Button_Discord.png"
        hover "gui/Hurricane_Like_Me/TitleScreen/Button_Discord_Hover.png"
        action OpenURL("https://en.wikipedia.org/wiki/Puppy")

    # Bottom menu
    imagemap:
        yalign 1.0
        ground "gui/Hurricane_Like_Me/TitleScreen/Menu.png"
        hover "gui/Hurricane_Like_Me/TitleScreen/Menu-Hover.png"
        #selected "gui/Hurricane_Like_me/TitleScreen/Menu-Select.png"
        # hotspot (X, Y, W, H) action
        hotspot (329, 117, 201, 53) action ShowMenu("credits")
        hotspot (569, 117, 201, 53) action ShowMenu("load")
        hotspot (779, 61, 446, 128) action Start()
        hotspot (1254, 117, 201, 53) action ShowMenu("Options")
        hotspot (1494, 117, 201, 53) action Quit()
    
#    frame:
#        style_group "gm_root"
#        xalign .98
#        yalign .98

    #text "[renpy.version_string] \"[renpy.version_name]\"" style "main_menu_version"

    #if gui.show_name:

        #vbox:
            #text "[config.name!t]":
                #style "main_menu_title"

            #text "[config.version!t]":
                #style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_window:
    xsize 280
    yfill True
    background "gui/Hurricane_Like_Me/TitleScreen/Wallpaper.jpg"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xsize 960
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    #use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    #background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            hbox:
                spacing 15
                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]") style "about_small"

            hbox:
                spacing 15
                text _("Written By") style "about_small"
                text _("Rosie | meltycreamcats")

            hbox:
                spacing 15
                text _("Written By") style "about_small"
                text _("Margaret Catter")
            
            null height 15

            hbox:
                spacing 15
                text _("Original Character Art") style "about_small"
                text _("By Deji")

            hbox:
                spacing 15
                text _("Original Character Art") style "about_small"
                text _("By ")

            null height 15

            hbox:
                spacing 15
                text _("Original Background Art") style "about_small"
                text _("By Laynesis")

            hbox:
                spacing 15
                text _("GUI Designed By") style "about_small"
                text _("Re:Alice")

            hbox:
                spacing 15
                text _("Phone Screen Adapted From") style "about_small"
                text _("{a=https://lemmasoft.renai.us/forums/viewtopic.php?p=494322#p494322/}Valentin Bez'chanuk{/a}")

            hbox:
                spacing 15
                text _("Quest Log Adapted From") style "about_small"
                text _("{a=https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=25245}jw2pfd{/a}")

            hbox:
                spacing 15
                text _("Placeholder Sprites By") style "about_small"
                text _("{a=https://lemmasoft.renai.us/forums/viewtopic.php?f=52&t=29421}Deji{/a}")

## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

style about_small:
    size 18
    minwidth 260
    text_align 1.0
    yalign 0.9


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    add "gui/Hurricane_Like_Me/Save and Load/backgroundSave.png"

    # Back
    imagebutton:
        xalign 0.5
        pos (145, 100)
        idle "gui/Hurricane_Like_Me/Save and Load/Button_Back.png"
        hover "gui/Hurricane_Like_Me/Save and Load/Button_Back_Hover.png"
        action Return()

    # Load
    imagebutton:
        xalign 0.5
        pos (1805, 100)
        idle "gui/Hurricane_Like_Me/Save and Load/Button_Load.png"
        hover "gui/Hurricane_Like_Me/Save and Load/Button_Load_Hover.png"
        action ShowMenu("load")

    # Slot 1
    $ currentSlot = 1
    frame:
        background None
        padding (0, 0)
        pos (262, 263)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileSave(currentSlot)

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)

    # Slot 2
    $ currentSlot = 2
    frame:
        background None
        padding (0, 0)
        pos (1097, 263)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileSave(currentSlot) 

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)

    # Slot 3
    $ currentSlot = 3
    frame:
        background None
        padding (0, 0)
        pos (262, 551)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileSave(currentSlot) 

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)

    # Slot 4
    $ currentSlot = 4
    frame:
        background None
        padding (0, 0)
        pos (1097, 551)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

    # Slot 5
    $ currentSlot = 5
    frame:
        background None
        padding (0, 0)
        pos (262, 817)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileSave(currentSlot) 

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)

    # Slot 6
    $ currentSlot = 6
    frame:
        background None
        padding (0, 0)
        pos (1097, 817)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileSave(currentSlot) 

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)

    imagemap:
        ground "gui/Hurricane_Like_Me/Save and Load/Pages.png"
        # idle Null()
        hover "gui/Hurricane_Like_Me/Save and Load/Pages-Select.png"
        pos (1835, 200)

        hotspot (10, 28, 41, 42) action FilePage(1) selected ( FileCurrentPage() == "1" )
        hotspot (10, 79, 41, 42) action FilePage(2) selected ( FileCurrentPage() == "2" )
        hotspot (10, 131, 41, 42) action FilePage(3) selected ( FileCurrentPage() == "3" )
        hotspot (10, 183, 41, 42) action FilePage(4) selected ( FileCurrentPage() == "4" )
        hotspot (10, 238, 41, 42) action FilePage(5) selected ( FileCurrentPage() == "5" )
        hotspot (10, 290, 41, 42) action FilePage(6) selected ( FileCurrentPage() == "6" )
        hotspot (10, 341, 41, 42) action FilePage(7) selected ( FileCurrentPage() == "7" )
        hotspot (10, 393, 41, 42) action FilePage(8) selected ( FileCurrentPage() == "8" )
        hotspot (10, 450, 41, 42) action FilePage(9) selected ( FileCurrentPage() == "9" )
        hotspot (10, 502, 41, 42) action FilePage(10) selected ( FileCurrentPage() == "10" )
        hotspot (10, 554, 41, 42) action FilePage(11) selected ( FileCurrentPage() == "11" )
        hotspot (10, 605, 41, 42) action FilePage(12) selected ( FileCurrentPage() == "12" )
        hotspot (10, 660, 41, 42) action FilePage(13) selected ( FileCurrentPage() == "13" )
        hotspot (10, 712, 41, 42) action FilePage(14) selected ( FileCurrentPage() == "14" )
        hotspot (10, 764, 41, 42) action FilePage(15) selected ( FileCurrentPage() == "15" )
        hotspot (10, 817, 41, 42) action FilePage(16) selected ( FileCurrentPage() == "16" )
        


screen load():

    tag menu

    add "gui/Hurricane_Like_Me/Save and Load/backgroundLoad.png"

    # Back
    imagebutton:
        xanchor 0.5
        pos (145, 100)
        idle "gui/Hurricane_Like_Me/Save and Load/Button_Back.png"
        hover "gui/Hurricane_Like_Me/Save and Load/Button_Back_Hover.png"
        action Return()

    # Load
    if not main_menu:
        imagebutton:
            xanchor 0.5
            pos (1805, 100)
            idle "gui/Hurricane_Like_Me/Save and Load/Button_Save.png"
            hover "gui/Hurricane_Like_Me/Save and Load/Button_Save_Hover.png"
            action ShowMenu("save")

    # Slot 1
    $ currentSlot = 1
    frame:
        background None
        padding (0, 0)
        pos (262, 263)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Action Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileLoad(currentSlot)

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)

    # Slot 2
    $ currentSlot = 2
    frame:
        background None
        padding (0, 0)
        pos (1097, 263)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileLoad(currentSlot) 

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)

    # Slot 3
    $ currentSlot = 3
    frame:
        background None
        padding (0, 0)
        pos (262, 551)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileLoad(currentSlot) 

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)

    # Slot 4
    $ currentSlot = 4
    frame:
        background None
        padding (0, 0)
        pos (1097, 551)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileLoad(currentSlot) 

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)

    # Slot 5
    $ currentSlot = 5
    frame:
        background None
        padding (0, 0)
        pos (262, 817)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileLoad(currentSlot) 

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)

    # Slot 6
    $ currentSlot = 6
    frame:
        background None
        padding (0, 0)
        pos (1097, 817)
        xsize 714
        ysize 206   

        # Wing
        frame:
            padding (0, 0)
            xalign 1.0
            ypos 8
            xsize 365
            ysize 163

            # Background of the Wing
            if FileLoadable(currentSlot):
                background "gui/Hurricane_Like_Me/Save and Load/usedWing.png"
            else:
                background "gui/Hurricane_Like_Me/Save and Load/emptyWing.png"

            # Slot number
            if FileLoadable(currentSlot):
                text "SAVE #{}".format( FileSlotName(currentSlot, 6).zfill(3) ):
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"
            else:
                text "SAVE #000":
                    xpos 200
                    ypos 1
                    size 30
                    font "fonts/AcariSans-Bold.ttf"
                    color "ffffff"

            # Details for saved files
            if FileLoadable(currentSlot):

                # Chapter
                text FileSaveName(currentSlot):
                    xpos 50
                    ypos 55
                    size 44
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"

                text FileTime(currentSlot, format = "%d %b %Y   %H:%M:%S"):
                    xpos 50
                    ypos 110
                    size 24
                    font "fonts/AcariSans-Regular.ttf"
                    color "ffffff"


        # File Screenshot or "Empty Data" image 
        if not FileLoadable(currentSlot):
            add "gui/Hurricane_Like_Me/Save and Load/emptyData.png":
                pos (9, 9)
        else:
            add FileScreenshot(currentSlot):
                size (342, 187)
                pos (9, 9)

        # Tv
        add "gui/Hurricane_Like_Me/Save and Load/tv.png"      

        # Button
        button:
            xsize 714
            ysize 206
            background None
            hover_background "gui/Hurricane_Like_Me/Save and Load/Hover_Selected_File.png"
            action FileLoad(currentSlot) 

        # Delete Button
        if FileLoadable(currentSlot):
            imagebutton:
                idle "gui/Hurricane_Like_Me/Save and Load/Button_Delete.png"
                hover "gui/Hurricane_Like_Me/Save and Load/Button_Delete_Hover.png"
                pos (665, 50)
                action FileDelete(currentSlot)


    imagemap:
        ground "gui/Hurricane_Like_Me/Save and Load/Pages.png"
        # idle Null()
        hover "gui/Hurricane_Like_Me/Save and Load/Pages-Select.png"
        selected_idle "gui/Hurricane_Like_Me/Save and Load/Pages-Select.png"
        pos (1835, 200)

        hotspot (10, 28, 41, 42) action FilePage(1) selected ( FileCurrentPage() == "1" )
        hotspot (10, 79, 41, 42) action FilePage(2) selected ( FileCurrentPage() == "2" )
        hotspot (10, 131, 41, 42) action FilePage(3) selected ( FileCurrentPage() == "3" )
        hotspot (10, 183, 41, 42) action FilePage(4) selected ( FileCurrentPage() == "4" )
        hotspot (10, 238, 41, 42) action FilePage(5) selected ( FileCurrentPage() == "5" )
        hotspot (10, 290, 41, 42) action FilePage(6) selected ( FileCurrentPage() == "6" )
        hotspot (10, 341, 41, 42) action FilePage(7) selected ( FileCurrentPage() == "7" )
        hotspot (10, 393, 41, 42) action FilePage(8) selected ( FileCurrentPage() == "8" )
        hotspot (10, 450, 41, 42) action FilePage(9) selected ( FileCurrentPage() == "9" )
        hotspot (10, 502, 41, 42) action FilePage(10) selected ( FileCurrentPage() == "10" )
        hotspot (10, 554, 41, 42) action FilePage(11) selected ( FileCurrentPage() == "11" )
        hotspot (10, 605, 41, 42) action FilePage(12) selected ( FileCurrentPage() == "12" )
        hotspot (10, 660, 41, 42) action FilePage(13) selected ( FileCurrentPage() == "13" )
        hotspot (10, 712, 41, 42) action FilePage(14) selected ( FileCurrentPage() == "14" )
        hotspot (10, 764, 41, 42) action FilePage(15) selected ( FileCurrentPage() == "15" )
        hotspot (10, 817, 41, 42) action FilePage(16) selected ( FileCurrentPage() == "16" )


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen Options():

    tag menu

    add "gui/Hurricane_Like_Me/Setting/background.png"

    # # Title
    # imagebutton:
    #     xanchor 0.5
    #     pos (145, 100)
    #     idle "gui/Hurricane_Like_Me/Setting/Button_Title.png"
    #     hover "gui/Hurricane_Like_Me/Setting/Button_Title_Hover.png"
    #     action ShowMenu("main_menu")

    # Back
    imagebutton:
        xanchor 0.5
        pos (145, 100) # Was (1805, 100)
        idle "gui/Hurricane_Like_Me/Setting/Button_Back.png"
        hover "gui/Hurricane_Like_Me/Setting/Button_Back_Hover.png"
        action Return()

    # Fullscreen
    imagebutton:
        pos (1329, 347)
        idle "gui/Hurricane_Like_Me/Setting/Button_Fullscreen.png"
        hover "gui/Hurricane_Like_Me/Setting/Button_Fullscreen.png"
        selected_idle "gui/Hurricane_Like_Me/Setting/Button_Fullscreen_Select.png"
        selected_hover "gui/Hurricane_Like_Me/Setting/Button_Fullscreen_Select.png"
        action Preference("display", "fullscreen")

    # Window
    imagebutton:
        pos (1629, 347)
        idle "gui/Hurricane_Like_Me/Setting/Button_Windowed.png"
        hover "gui/Hurricane_Like_Me/Setting/Button_Windowed.png"
        selected_idle "gui/Hurricane_Like_Me/Setting/Button_Windowed_Select.png"
        selected_hover "gui/Hurricane_Like_Me/Setting/Button_Windowed_Select.png"
        action Preference("display", "window")

    # Unread
    imagebutton:
        pos (1329, 506)
        idle "gui/Hurricane_Like_Me/Setting/Button_Unread.png"
        hover "gui/Hurricane_Like_Me/Setting/Button_Unread.png"
        selected_idle "gui/Hurricane_Like_Me/Setting/Button_Unread_Select.png"
        selected_hover "gui/Hurricane_Like_Me/Setting/Button_Unread_Select.png"
        action Preference("skip", "seen")

    # All
    imagebutton:
        pos (1629, 506)
        idle "gui/Hurricane_Like_Me/Setting/Button_All.png"
        hover "gui/Hurricane_Like_Me/Setting/Button_All.png"
        selected_idle "gui/Hurricane_Like_Me/Setting/Button_All_Select.png"
        selected_hover "gui/Hurricane_Like_Me/Setting/Button_All_Select.png"
        action Preference("skip", "all")

    # vbox:
    #     style_prefix "radio"
    #     label _("Rollback Side")
    #     textbutton _("Disable") action Preference("rollback side", "disable")
    #     textbutton _("Left") action Preference("rollback side", "left")
    #     textbutton _("Right") action Preference("rollback side", "right")

    # vbox:
    #     style_prefix "check"
    #     label _("Skip")
    #     textbutton _("Unseen Text") action Preference("skip", "toggle")
    #     textbutton _("After Choices") action Preference("after choices", "toggle")
    #     textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

    ## Additional vboxes of type "radio_pref" or "check_pref" can be
    ## added here, to add additional creator-defined preferences.

    # vbox:
    #     style_prefix "radio"
    #     label _("Language")

    #     textbutton "English" text_font "fonts/Acumin-RPro.otf" action Language(None)
    #     textbutton "Français" text_font "fonts/Acumin-RPro.otf" action Language("french")
    #     textbutton "Русский" text_font "fonts/Acumin-RPro.otf" action Language("russian")
    #     textbutton "Bahasa Melayu" text_font "fonts/Acumin-RPro.otf" action Language("malay")
    #     textbutton "한국어" text_font "fonts/NotoSansKR-Medium.otf" action Language("korean")
    #     textbutton "简体中文" text_font "fonts/NotoSans-Regular.ttf" action Language("simplified_chinese")
    #     textbutton "繁體中文" text_font "fonts/NotoSans-Regular.ttf" action Language("traditional_chinese")
    #     textbutton "Español" text_font "fonts/Acumin-RPro.otf" action Language("spanish")


    # 

    # BGM
    window:
        area (650, 342, 397, 24)
        background "gui/Hurricane_Like_Me/Setting/Slider/Base.png"

        bar:
            area (14, 7, 376, 10)
            left_bar "gui/Hurricane_Like_Me/Setting/Slider/Fill.png"
            right_bar None
            thumb None
            value Preference("music volume")

    # Sound
    window:
        area (650, 413, 397, 24)
        background "gui/Hurricane_Like_Me/Setting/Slider/Base.png"

        bar:
            area (14, 7, 376, 10)
            left_bar "gui/Hurricane_Like_Me/Setting/Slider/Fill.png"
            right_bar None
            thumb None
            value Preference("sfx volume")

    # Ambience
    window:
        area (650, 487, 397, 24)
        background "gui/Hurricane_Like_Me/Setting/Slider/Base.png"

        bar:
            area (14, 7, 376, 10)
            left_bar "gui/Hurricane_Like_Me/Setting/Slider/Fill.png"
            right_bar None
            thumb None
            value Preference("music volume")

        text "Hooked up to Music volume":
            pos (14, 7)

    # Voice
    window:
        area (650, 560, 397, 24)
        background "gui/Hurricane_Like_Me/Setting/Slider/Base.png"

        bar:
            area (14, 7, 376, 10)
            left_bar "gui/Hurricane_Like_Me/Setting/Slider/Fill.png"
            right_bar None
            thumb None
            value Preference("voice volume")

    # Text speed
    window:
        area (650, 734, 397, 24)
        background "gui/Hurricane_Like_Me/Setting/Slider/Base.png"

        bar:
            area (14, 7, 376, 10)
            left_bar "gui/Hurricane_Like_Me/Setting/Slider/Fill.png"
            right_bar None
            thumb None
            value Preference("text speed")

    # Auto speed
    window:
        area (650, 804, 397, 24)
        background "gui/Hurricane_Like_Me/Setting/Slider/Base.png"

        bar:
            area (14, 7, 376, 10)
            left_bar "gui/Hurricane_Like_Me/Setting/Slider/Fill.png"
            right_bar None
            thumb None
            value Preference("auto-forward time")

    # bar:
    #     pos (663, 349)
    #     base_bar "gui/Hurricane_Like_Me/Setting/Slider/Base.png"
    #     left_bar "gui/Hurricane_Like_Me/Setting/Slider/Fill.png"
    #     left_gutter 2
    #     value Preference("music volume")

    # Restore defaults
    imagebutton:
        pos (1325, 690)
        idle "gui/Hurricane_Like_Me/Setting/Button_Restore.jpg"
        hover "gui/Hurricane_Like_Me/Setting/Button_Restore_Hover.jpg"
        action Confirm( "Are you sure you want to return settings to default?", Function(optionDefaults) ) # Add defaults

    # # Return
    # imagebutton:
    #     pos (1156, 900)
    #     idle "gui/Hurricane_Like_Me/Setting/Button_Return.png"
    #     hover "gui/Hurricane_Like_Me/Setting/Button_Return_Hover.png"
    #     action Return()

init -1 python:

    def optionDefaults():
        preferences.fullscreen = False
        preferences.skip_unseen = False

        preferences.set_volume('music', 0.8)
        preferences.set_volume('sfx', 0.8)
        preferences.set_volume('music', 0.8) # "Hooked up to Music volume"
        preferences.set_volume('voice', 0.8)

        preferences.text_cps = 80
        preferences.afm_time = 15

        renpy.restart_interaction()


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    add "gui/Hurricane_Like_Me/Menu/bg.png"

    window:
        background "gui/Hurricane_Like_Me/Confirm/Noticement.png"
        xsize 877
        ysize 419
        align (0.5, 0.5)

        frame:
            background None
            xsize 600
            xalign 0.5
            yanchor 0.5
            ypos 210

            text message:
                align (0.5, 0.5)
                color "ffffff"
                font "fonts/Acumin-RPro.otf"
                size 32

        hbox:
            align (0.5, 0.8)
            spacing 100

            imagebutton:
                idle "gui/Hurricane_Like_Me/Confirm/Button_Yes.png"
                hover "gui/Hurricane_Like_Me/Confirm/Button_Yes_Hover.png"
                action yes_action

            imagebutton:
                idle "gui/Hurricane_Like_Me/Confirm/Button_No.png"
                hover "gui/Hurricane_Like_Me/Confirm/Button_No_Hover.png"
                action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    
    background None

    #background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

#####################################################
################SCREENS I'VE ADDED#######################
####################START#############################

screen invdisplay:
        vbox:
            align (0.0, 0.0)
            text "{u}Workbag{/u}"
            for item in workbag.inventory:
                text ("[item.item]")
        vbox:
            align (0.1, 0.0)
            text "{u}Purse{/u} "
            for item in purse.inventory:
                text ("[item.item]")

screen moodpointdisplay:
        vbox:
            xalign 1.0
            yalign 0.0
            text "Happy :[Mood_Happy]"
            text "Focus :[Mood_Focus]"
            text "Hungry :[Mood_Hungry]"
            text "Chill :[Mood_Chill]"
            text "Sleep :[Mood_Sleep]"
            text "Panic :[Mood_Panic]"
            text "Stress :[Mood_Stress]"
            text "Embarrassed :[Mood_Embarrassed]"



########################END##############################
################SCREENS I'VE ADDED#######################
#########################################################
