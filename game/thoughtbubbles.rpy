init python:
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve


    style.nvl_dialogue.drop_shadow = [(1, 1)] # If you want a Drop Shadow for your NVL text, 1 pixel to the right and 1 pixel down.

    ## ------ Framed (adjustable) NVL box ---------
    style.nvl_window.background = Frame("gui/Hurricane_Like_Me/Thought/Thought.png")

    ## ---- No Frame (non-adjustable) Nvl Box------
    # style.nvl_window.background = "NVLbox02.png" 
    ## margins ------------------------------------
    # Changes the shape of the BOX.

    style.nvl_window.top_margin = 0
    style.nvl_window.bottom_margin = 30
    style.nvl_window.left_margin = 0
    style.nvl_window.right_margin = 0
    
    ## padding ---------------------------------
    # Changes the placement of the TEXT.

    style.nvl_window.top_padding = 50
    style.nvl_window.bottom_padding = 0
    style.nvl_window.left_padding = 530
    style.nvl_window.right_padding = 30
    
    ## Interblock spacing: ------------------
    # The space between Blocks of paragraphs. 

    style.nvl_vbox.box_spacing = 15
    