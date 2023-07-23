screen countdown_timer: 
    frame: 
        background "#00000000"
        xfill True 
        yfill True 
        text "[initial_countdown]" size 120 text_align 0.5 align(0.5,0.5)

    timer 1.0 action If(initial_countdown > 1, SetVariable("initial_countdown", initial_countdown - 1), Hide("countdown_timer")) repeat If(initial_countdown > 1, True, False)

screen reflex_minigame: 
    on "show" action Show("countdown_timer")
    image "horrorObstacleBackground.png"

    grid int(buttons/2) 2: 
        xspacing 100 
        yspacing 100
        #anchor(.5,.5)
        align(.5,.85)
        for i in range(buttons): 
            imagebutton idle "button_%s.png" % button_states[i] focus_mask True action Function(reflex_game_bpress, btn = i)
    text "[score]" size 78 align(.90,.145) text_align .5 
    text "[play_time]" size 78 color "#FFFFFF" align(.90,.355) text_align .5 

    if renpy.get_screen("countdown_timer") == None: 
        if "lit" not in button_states:
            timer 0.1 action Function(light_button) repeat False
        timer 1.0 action If(play_time > 1, SetVariable("play_time", play_time -1), Jump("afterObstacle")) repeat If(play_time >1, True, False)   
            
init python: 
    import random

    def reflex_game_bpress(btn): 
        global score
        
        if button_states[btn] == "lit": 
            score += 1
            button_states[btn] = "idle"

    def setup_reflex_game(): 
        #Function to setup the mini-game before it starts
        global random_button_indexes
        for i in range(buttons): 
        #fill state with idle
            button_states.append("idle")
        random_button_indexes = random.sample(range(buttons), k = buttons)
    
    def light_button(): 
        global random_button_indexes
        global current_button_index

        if current_button_index < buttons - 1: 
            current_button_index += 1
        else: 
            current_button_index = 0
            random_button_indexes = random.sample(range(6), k =6)
        random_button_index = random_button_indexes[current_button_index]
        button_states[random_button_index] = "lit"

