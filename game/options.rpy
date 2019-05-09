## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Hurricane Like Me")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "0.2"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
Phone screen system developed by {a=https://lemmasoft.renai.us/forums/viewtopic.php?p=494322#p494322/}Valentin Bez'chanuk{/a}

Quest log adapted from {a=https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=25245}jw2pfd{/a}

Sprites by {a=https://lemmasoft.renai.us/forums/viewtopic.php?f=52&t=29421}Deji{/a}

Troy's phone background by {a=https://www.deviantart.com/wirdoudesigns/art/Family-Portrait-304874174}wirdoudesigns{/a}

""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "HurricaneLikeMe"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "HurricaneLikeMe-1530486320"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon2.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

################# phone code stars ###################
#################################################################################
### Telegram Messenger
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
    style.txt_base.font = "gui/CaviarDreams_Bold.ttf"
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
            renpy.play("new_message.mp3", "sound")
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
            renpy.play("sms-alert-5-daniel_simon.mp3", "sound")
        renpy.pause()
    def del_last_msg():
        if len(store.m_msg) > 0:
            del store.m_msg[-1]

    def del_all_msg():
        store.m_msg = []

#################################################################################

screen telegram():
    frame background "messenger/back.png" xysize (600,675) align (0.9,.4):
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
        text "%s"%(msg_name) style "txt_base" size 35 xalign 0.31 xanchor 0.0 yalign 0.04
        add "messenger/av/"+msg_name.lower().replace(' ', '_')+".png" pos (100,27)
        imagebutton auto "messenger/arr_%s.png" pos (10, 33) action NullAction()
        button background style_button_inst hover_background style_button_hovr xalign 0.99 yalign 0.03 action Function(del_all_msg) xysize (60,60):
            text "  x  " style "txt_base" size 40 pos (36, -2)
        vbar value YScrollValue("vp_msg") style "bar_vert"
#################################################################################


######### phone code ends here ##########
