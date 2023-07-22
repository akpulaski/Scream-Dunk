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
    play music gamesBegin
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
            play audio manScream2
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
            play music loss
            show black with fade
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
    play music main
    show field horror bg 
    "Everyone looks uneasily between each other, but everyone moves to follow the Bread Head."
    show bread at left 
    bread "A game of distance running, how exciting! There's only one rule: Just keep running! That's right, all you have to do is not stop."
    bread "Now, move on now! Time's a-wastin'!"
    hide bread
    "We all shuffle towards the tracks."
    show older shirt at right 
    older "Good luck, kid."
    show mc at left 
    pov "Uh... thanks?"
    hide older  
    show athlete at right 
    ath "Psh."
    hide mc 
    hide athlete
    play audio gunshotClose
    "I get ready to run, but I still stumble at the sound of the gunshot."
    bread "Go go go, friends! We are just getting started! Hurrah!"
    play music minigame
    jump clickerBegin

label clickerBegin:
    scene field horror bg
    centered "Click your character to run.{w=1}{nw}"
    call screen clicker

label clickWin:
    play audio gunshotFar
    "As I run, I hear gunshots going off towards the back, but I can't look back now."
    play audio womanScream1
    "Pained shrieks fill the air, but I keep running."
    "Beside me, I see the older guy, the athletic woman, and the creep managing to keep good pace."
    "A horn blares out, we all hesitantly slow."
    play music main 
    hide killer
    show bread at left
    bread "Aaaaand that brings us to the end of the game, champs! You all did well!"
    bread "It's a shame that some of our friends will have to leave us."
    play audio manScream3
    "I try to look the other way as the masked killers gather up the bleeding out contestants left in their wake."
    show killer at right
    play audio fire
    "The killer then douses the pile and lights it aflame with the drop of a match."
    "Putrid smell fills the air as the screams slowly die out."
    bread "Nearly as unpleasant as it was necessary. Now we are closer to the prize. Just a few more games to go!"
    jump longJump

label clickLost:
    scene field horror bg 
    play music loss 
    "I run as hard as I can, but soon I find myself faltering."
    show killer at left
    show mc scared at right
    killer "Gotcha!"
    "I feel the knife slip between my ribs, then everything goes black as I fall."
    show black with fade
    play audio fire 
    "I'm aware of the sloshing of a liquid, then feel the flames lick at my skin."
    "I scream in agony in my last few moments."
    return


label longJump: 
    scene long bg 
    show bread at left 
    bread "It's time for the second round! Just a simple competition of long jump!"
    bread "Each one of you will just have to pick any random number, from one to ten, which will determine your position in the jumping order."
    bread "Hop on now. Take your pick!"
    menu: 
        "I pick a smaller number, better to get it over with.": 
            $ max_score_required = 8
        "I pick a mid-range number, some before some after seems safest.": 
            $ max_score_required = 13
        "I pick a higher number, best to develop a strategy.": 
            $ max_score_required = 18
    "Once everyone has picked a number, Bread Head gets us all to line up in order."
    bread "Oh, one last thing! The distance will be determined by the best jumper before you! But we can't start with nothing."
    scene long horror bg
    "Masked killers make their way out onto the field, filling the sand with traps and broken glass."
    "I swallow hard, waiting my turn in the order."
    play music minigame
    centered "Press the space bar in the green area to aim.{w=1}{nw}"
    jump start_minigame

label longJumpEnding: 
    "Finally, everyone has jumped except the final person: the creepy guy."
    "Those who failed have been left to lie where they fell. Making the field a broken mess of bodies, blood, and traps."
    show bread at left 
    bread "You're next, friend! Go big or go home!"
    bread "Just kidding, you have no choice here. All the best anyways!"
    show creep annoyed at right 
    creep "Shut the fuck up."
    hide bread
    "He then takes a running leap... and almost makes it!"
    play audio manScream4
    show creep scared at right
    creep "Ah! My leg, my leg!"
    show killer at left 
    "He's approached by one of the masked killers, but he takes a swing at them."
    creep "No, no! I'm... fine... I can keep competeing."
    show killer sad 
    killer "..."
    show bread at left 
    bread "Fine! If you think you can continue, all the best for you!"
    bread "Those who can't though... gather them up!"
    "I try to look away once more as the masked killers pile up the others, taking no care to cause more pain as they drag the bodies out of the pit."
    "The creep seems to be struggling to limp over to the others."
    menu: 
        "I go and help him.": 
            show creep 
            creep "Thanks, man. You're... not so bad."
            show mc at left 
            pov "No problem, this whole thing is fucked."
            $ kind += 1 
        "I let him struggle.": 
            show creep annoyed 
            creep "Let's just get on with it."
            $ cruel += 1
    jump halfTime

label halfTime: 
    scene locker bg 
    play music main 
    "Everyone gathers around the locker room, falling into the benches."
    "I look around the exhausted faces, shell shocked and terrified."
    show older shirt at left 
    older "How's everyone holding up?"
    show athlete annoyed at right 
    ath "How's everyone holding up?! We're being killed out there!"
    ath "I knew I'd have to work hard to get this money, but I didn't expect to leave a pile of bodies in my wake!"
    "I narrow my eyes at her... Even now she's still insistant that she's going to win."
    show creep at right
    creep "We need to do something! We need to..."
    creep "Kill the Bread Head!"
    menu: 
        "I agree.": 
            show mc at left 
            pov "That's not a bad idea! Maybe we can take them! There's more of us."
        "I disagree": 
            show mc annoyed at left
            pov "Are you kidding? How are we going to do that?"
    "Here's the end of the current build. Thanks for playing!"
    return 

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

#starts the long jump mini game
label start_minigame:
    show screen fable_timer_left
    call screen fable_2_minigame

label end_minigame: #End minigame. And jump continue game
    hide screen fable_2_minigame
    $ renpy.pause(0.3)
    jump gameTwoConclusion #continue game

label timingFailure:
    play music loss 
    "I take a deep breath and then run towards the sand pit."
    "Unfortunately, I do not make the distance I was hoping to..."
    play audio manScream1
    play sound crushed 
    "I scream in pain as I land on a bear trap."
    show bread at left 
    bread "Oh, too bad! That's a lot of blood."
    "I have to agree as everything fades to black."
    show black with fade 
    "Better luck next time!"
    "Try again?"
    return