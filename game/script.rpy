# start of the Scream Dunk Ren'Py script
# This file serves as initial commit for git hub.

label start: 
    "You wake up in a locker room."
    "Characters are introduced."
    older "I'm the older guy. And I just want to make sure everyone is alright."
    ath "I'm the bitchy athlete and I don't know why I'm here."
    creep "I'm the creep and I can give you a good time since you're already here. ;)"
    bread "And I'm the mascot thats going to explain your situation!"
    bread "Haha, horrible murderous plans! I'm explaining the games!"
    jump outsideGameOne

label outsideGameOne: 
    show field bg
    "The group is now outside, ready for the first game."
    bread "You've got to run away from the masked killer! Else he'll stabby stab!"
    bread "He'll probably be content when he kills three people!"
    "Here there's a clicker game."
    jump clickerBegin

label clickerBegin:
    centered "Click your character to run.{w=1}{nw}"
    call screen clicker

label clickWin:
    $ renpy.pause(2, hard=True)
    centered "Wow you didn't die!"
    return

label clickLost:
    centered "Oops dead."
    return

label gameOneConclusion: 
    "You run for what feels like forever. One, two, then three others fall and the masked killer stops chasing."
    "Hestitantly people slow and eventually come to a stop when they confirm the killer is satisfied."
    bread "Wow congratz! You survived! Next game time! No times for breaks!"
    jump outsideGameTwo

label outsideGameTwo: 
    "Long jump goes here. Distance set by previous successes. So further for those who go later."
    "Maybe a timing mini game."
    jump gameTwoConclusion

label gameTwoConclusion: 
    bread "Wow you did it again! That guy didn't do it and now he's in agnoizing pain!"
    bread "On to the next thing!"

label outsideGameThree: 
    "This stage is less a game and more just brutal murder!"
    bread "Kill someone!"
    older "Kill the creep."
    creep "Wait no."
    menu: 
        "Sacrifice yourself.": 
            jump sacrificeEnd
        "Kill the creep.": 
            jump killedSomeone
        "Kill the bitch.": 
            jump killedSomeone
        "Kill the old man.": 
            jump killedSomeone

label sacrificeEnd: 
    "Oh how noble."
    return

label killedSomeone: 
    "Someone is dead now and you did it!"
    jump outsideGameFour

label outsideGameFour: 
    "Maybe we put an obstacle course here. I don't have a mini game to go with that necessarily.Suggestions welcome."
    jump gameFourConclusion

label gameFourConclusion: 
    bread "Wow that sure was something!"
    bread "Now that there's only two of you left, it's time for the real fun!"
    jump outsideGameFive

label outsideGameFive: 
    bread "Throw javelins at each other!"
    menu: 
        "Sacrifice yourself.": 
            jump sacrificeEnd
        "Kill the other contestant.": 
            jump winner
        "Refuse to participate.": 
            if goodPerson: 
                jump breadTantrum
            else: 
                jump brutallyMurdered
        "Aim at the other contestant, without confidence.": 
            jump bleedOut

label winner: 
    "You did it! You survived Dreadfield Games!"
    return

label breadTrantrum: 
    bread "No! You can't just not kill each other!"
    bread "One of you have to do it!"
    "But you and the other contestant don't."
    return

label brutallyMurdered: 
    "You don't attack, but the other contestant has other ideas."
    return

label bleedOut: 
    "You stab without conviction. So does your opponent."
    "You both bleed out wishing that the other had more backbone and killed you more quickly."
    return