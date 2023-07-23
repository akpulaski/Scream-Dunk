#clicker game stuff
default points=20
default plus=2
default max_point=100
default clicked = True

#timing game stuff 
init 15 python:
    fable_minigame_bar = 90
    fable_minigame_score = 0
    fable_you_press_button = 0
    max_score_required = 0

#obstacle wack a mole stuff 
default button_states = [] # Will contain the different states of the buttons ("idle" or 'lit')
default buttons = 6 #how many buttons will be on the screen
default random_button_indexes = [] # will contain randomly generated numbers 
default current_button_index = 0 # keeps track of the currently picked button index.
default score = 0 # keeps track of the player's score
default play_time = 20 # keeps track of the time left. 
default initial_countdown = 3 #how many seconds the countdown timer will count down before the game starts


#random choices
default lockerChoices = ('a crudely severed finger', 'a blood-covered rag', 'a couple of loose teeth')

#boolean variables for game choices
default hasKnife = False #found knife in the lockerroom
default hasIdea = False #wants to jump the Bread Head
default killedOld = False #killed the old man 
default killedBitch = False #killed the bitchy athlete
default killedCreep = False #killed the creep

#stats 
default kind = 0 
default cruel = 0 
default coward = 0
default name = "John"