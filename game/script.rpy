# start of the Scream Dunk Ren'Py script
# This file serves as initial commit for git hub.

label start: 
    play music intro
    show locker bg with dissolve
    "I blink a few times as I wake with a splitting headache."
    show mc at left
    pov "Is this a locker room?"
    hide mc 
    "I look around the room, stumbling back some as I see a bloodied baseball bat."
    menu: 
        "Look around further.": 
            jump exploreLockers
        "Close my eyes and hope to wake up somewhere else.": 
            jump bitchyIntroduction

label exploreLockers: 
    $ lockerItem = renpy.random.choice(lockerChoices)
    "I look in a locker and find [lockerItem] and a knife." 
    "Despite my better judgement, I pick up the knife."
    $ hasKnife = True
    jump bitchyIntroduction

label bitchyIntroduction: 
    "Suddenly a woman enters the room with her arms crossed."
    "She narrows her eyes at me."
    show athlete annoyed at right 
    "Athletic Woman" "Who might you be and what business do you have here?"
    pov "I could ask you the same question."
    hide mc 
    if hasKnife: 
        "Athletic Woman" "Is that a fucking knife you brought here?!? That's against the rules! I'm telling everyone."
        "Athletic Woman" "I knew something was off when I saw you here!"
        "What the hell is her problem?"
        pov "Hey hey hey. What?!"
        pov "I just found it lying over here in all this junk! It's not mine."
        "Athletic Woman" "Yeah, sure. I don't give a shit, rookie. I'm winning anyway."
        "She speaks with a sneer."
        menu: 
            "Keep the knife.": 
                "I don't fully feel safe. I should keep this."
            "Put the knife down.": 
                $ hasKnife = False 
                "I probably don't want to have this on me."
    else: 
        "Athletic Woman" "Well, whatever. We should join the others."
    jump creepIntroduction

label creepIntroduction: 
    hide athlete 
    "Just then another man barges into the room."
    "Man " "Heya, juniors. Whatcha whippersnappers up to, ey?"
    "Man " "Things going fiiiiiiiine - hic- in here?"
    "He slurs his words with a disingenuous smile."
    "He staggers towards the bitchy athlete."
    "Well, you a pretty thing ain't ya?"
    "He leers down at her as she cringes."
    pov "Dude, back off."
    jump olderIntroduction

label olderIntroduction: 
    "Another man, older, comes in the room."
    "Concern is written all over his face."
    show older suit at right 
    older "Hey guys. Just wanted to check in. Everything alright in here?"
    "He looks towards the girl and I, pointedly ignoring the creep."
    pov "Yessir. We were just ahvinga discu--"
    show athlete annoyed at left
    ath "Absolutely not! This pisshead right here is downright an absolute creep. Disgusting."
    hide athlete 
    creep "Watch yer language, missy. Or I might have to teach ya some manners."
    "The creep steps forward, but the older man steps in the way."
    show older suit annoyed at right
    older "Get the hell outta here."
    creep "Or what?"
    creep "Watchuuuuu-hic-gunna do?"
    show older suit scared at right
    "The creep takes a swing at the older man."
    "I should do something."
    menu: 
        "Pull the knife on the creep." if hasKnife: 
            $ cruel += 1
            "I pull the knife out from my waistband and point it at the creep."
            pov "Stop it! Now."
            creep "What the f-"
            "The creep jumps back, and so does the older man."
        "Try to break up the fight.":
            $ kind += 1
            "I quickly move forward to try and intercept the creep."
            pov "Stop it! Don't we have more important things to deal with?!" 
            "The creep takes a swing at me as well, striking my face hard."
        "Flee and look for help.": 
            $ coward += 1 
            "I run out of the room, looking for someone to get involved."
            show field bg 
            ath "Coward!"
            "I try to not let the call after me bother me."
    jump loudspeaker

label loudspeaker: 
    "Suddenly, a voice comes across the loudspeaker with a crackle."
    "The fight settles as we all listen."
    bread "Gooooooood Morning champions! Rise and shine! What a beautiful day for some fun-filled activities."
    bread "Now, before we jump to our games, I request all the contestants to line up in the middle of the track field."
    bread "Get going chums! You do not want to be late!"
    "My eye twitches at the annoyingly cheery and upbeat voice."            
    "Looking to the others, I can tell we're all in agreement."
    "Whatever is going on here, it's best we go find out."
    jump initialLineup

label initialLineup: 
    play music main
    show field bg 
    show bread at left
    bread "Very well! Now I'm sure you all know why you are here. Play games, win prizes of course! HaHa!"
    bread "But there's a catch! So let me explain the rules to you. Don't worry friends, only 3 rules! How simple!"
    bread "Rule Number One: There can be only one winner at the end of the games. Yes, the winner takes it all!"
    bread "Rule Number Two: If you lose, you WILL die. This will be your last stop."
    "At this, the group protests as panic washes over them."
    "Incredulous Contestant" "He can't be serious. This has to be a joke."
    creep "Psh. Incredibly \'funny\'."
    menu: 
        "Nerves rise in my stomach and I..."
        "Stay in line.": 
            "Scared Contestant" "The fuck, dude?!? Only ONE winner??? I don't care man, I'm outta here."
            "The man starts to walk away."
            bread "Come back here, friend! Trust me, you do not want to face the consequences!"
            "But he doesn't listen to the Breadhead's warning."
            "Scared Contestant" "Yeah, whatever. Consequences be damned."
            "He continues to walk away."
            "Then a gunshot rings out."
            "A panicked shriek erupts from the group as they watch the scene in horror."
            "Almost out of nowhere, two masked men appear."
            show killer at right 
            killer "...."
            bread "Clear out the body please."
            hide killer
            "The masked men go to carry away the body."
            jump firstDeath
        "Start to walk away.": 
            pov "I'm out of here! Whatever this is, it's sick."
            "Everyone else stays in line, waiting to see what happens."
            bread "Come back here, friend! Trust me, you do not want to face the consequences!"
            "I continue to walk."
            "A gunshot rings out, and I suddenly feel a deep pain in my back before another, and another."
            "Everything fades to black."
    

label firstDeath: 

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
    jump gameOneConclusion

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

label shotBadEnd:
    "Maybe walking away wasn't the best idea."
    "Try again?"
    return