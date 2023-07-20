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
        show mc at left 
        pov "Hey hey hey. What?!"
        pov "I just found it lying over here in all this junk! It's not mine."
        hide mc 
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
    show creep at right 
    "Man " "Heya, juniors. Whatcha whippersnappers up to, ey?"
    "Man " "Things going fiiiiiiiine - hic- in here?"
    "He slurs his words with a disingenuous smile."
    "He staggers towards the bitchy athlete."
    "Man ""Well, you a pretty thing ain't ya?"
    "He leers down at her as she cringes."
    show mc annoyed at left 
    pov "Dude, back off."
    hide mc
    jump olderIntroduction

label olderIntroduction: 
    "Another man, older, comes in the room."
    "Concern is written all over his face."
    hide creep
    show older suit at right 
    older "Hey guys. Just wanted to check in. Everything alright in here?"
    "He looks towards the girl and I, pointedly ignoring the creep."
    show mc at left
    pov "Yessir. We were just having a discu--"
    hide mc 
    show athlete annoyed at left
    ath "Absolutely not! This pisshead right here is downright an absolute creep. Disgusting."
    hide athlete 
    show creep annoyed at left 
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
            show mc annoyed at right 
            pov "Stop it! Now."
            show creep scared 
            creep "What the f-"
            "The creep jumps back, and so does the older man."
        "Try to break up the fight.":
            $ kind += 1
            "I quickly move forward to try and intercept the creep."
            hide older 
            show mc at right
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
    show creep scared at right 
    creep "Psh. Incredibly \'funny\'."
    hide creep
    menu: 
        "Nerves rise in my stomach and I..."
        "Stay in line.": 
            show con1 scared at right 
            "Scared Contestant" "The fuck, dude?!? Only ONE winner??? I don't care man, I'm outta here."
            "The man starts to walk away."
            bread "Come back here, friend! Trust me, you do not want to face the consequences!"
            "But he doesn't listen to the Breadhead's warning."
            "Scared Contestant" "Yeah, whatever. Consequences be damned."
            "He continues to walk away."
            hide con1 
            play audio gunshotFar
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
            play audio gunshotFar
            "A gunshot rings out, and I suddenly feel a deep pain in my back before another, and another."
            "Everything fades to black."
            jump shotBadEnd
    

label firstDeath: 
    bread "Oops! What a pitiful ending! I'm sorry you had to see that, friend!"
    bread "Just a mere interruption. I trust that it will be the last."
    bread "Well, that brings us to the third and final rule: No one is allowed to exit the game!"
    bread "After all, you made the choice to play games for a handsome reward, didn't you? A high reward always comes at high stakes!"
    "Did I sign up for something like this? I don't feel like I did..."
    "I try to speak up but the BreadHead continues without so much as a breath."
    bread "I believe it's best we immediately start off the games, we're already behind because of the disruption caused by our poor littel friend."
    bread "There will be a totla of five games of various exciting adventures."
    bread "Some of you will be eliminated, but I wish nothing but the best to all of you, friends!"
    bread "So let's move on to the first round!"
    jump distanceRun

label distanceRun: 
    "The air immediately shifts, and the area seems darker."
    "Everyone looks uneasily between each other, but everyone moves to follow the Bread Head."
    show field horror bg 
    show bread at left 
    bread "A game of distance running, how exciting! There's only one rule: Just keep running! That's right, all you have to do is not stop."
    bread "Now, move on now! Time's a-wastin'!"
    hide bread
    "We all shuffle towards the tracks."
    show older at right 
    older "Good luck, kid."
    show mc at left 
    pov "Uh... thanks?"
    hide older 
    show ath at right 
    ath "Psh."
    hide mc 
    hide ath
    play audio gunshotClose
    "I get ready to run, but I still stumble at the sound of the gunshot."
    bread "Go go go, friends! We are just getting started! Hurrah!"
    jump clickerBegin

label clickerBegin:
    scene field horror bg
    centered "Click your character to run.{w=1}{nw}"
    call screen clicker

label clickWin:
    play audio gunshotFar
    "As I run, I hear gunshots going off towards the back, but I can't look back now."
    "Pained shrieks fill the air, but I keep running."
    "Beside me, I see the older guy, the athletic woman, and the creep managing to keep good pace."
    "A horn blares out, we all hesitantly slow."
    show bread at left
    bread "Aaaaand that brings us to the end of the game, champs! You all did well!"
    bread "It's a shame that some of our friends will have to leave us."
    "I try to look the other way as the masked killers gather up the bleeding out contestants left in their wake."
    show killer at right
    play audio fire
    "The killer then douses the pile and lights it aflame with the drop of a match."
    "Putrid smell fills the air as the screams slowly die out."
    jump 

label clickLost:
    scene field horror bg 
    "I run as hard as I can, but soon I find myself faltering."
    show killer at left
    show mc scared at right
    killer "Gotcha!"
    "I feel the knife slip between my ribs, then everything goes black as I fall."
    play audio fire 
    "I'm aware of the sloshing of a liquid, then feel the flames lick at my skin."
    "I scream in agony in my last few moments."
    return


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