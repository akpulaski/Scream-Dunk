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

#random choices
default lockerChoices = ('a crudely severed finger', 'a blood-covered rag', 'a couple of loose teeth')

#boolean variables for game choices
default hasKnife = False #found knife in the lockerroom
default hasIdea = False #wants to jump the Bread Head

#stats 
default kind = 0 
default cruel = 0 
default coward = 0
