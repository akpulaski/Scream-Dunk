# start of the Scream Dunk Ren'Py script
# This file serves as initial commit for git hub.

label start: 
    play music intro
    $ name = renpy.input("Please enter your name: ")
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
                $ Achievement.add(achievement_name['gotKnife'])
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
    show con2 scared at right 
    "Incredulous Contestant" "He can't be serious. This has to be a joke."
    hide con2 
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
            $ Achievement.add(achievement_name['walkAway'])
            scene black with fade
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
    $ Achievement.add(achievement_name['survivedRun'])
    play audio gunshotFar
    "As I run, I hear gunshots going off towards the back, but I can't look back now."
    play audio womanScream1
    "Pained shrieks fill the air, but I keep running."
    "Beside me, I see the older guy, the athletic woman, and the creep managing to keep good pace."
    play audio horn
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
    $ Achievement.add(achievement_name['diedRun'])
    scene field horror bg 
    play music loss 
    "I run as hard as I can, but soon I find myself faltering."
    show killer at left
    show mc scared at right
    killer "Gotcha!"
    "I feel the knife slip between my ribs, then everything goes black as I fall."
    scene black with fade
    play audio fire 
    "I'm aware of the sloshing of a liquid, then feel the flames lick at my skin."
    "I scream in agony in my last few moments."
    call achievementCheck
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
    $ Achievement.add(achievement_name['survivedJump'])
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
    hide killer
    show bread at left 
    bread "Fine! If you think you can continue, all the best for you!"
    bread "Those who can't though... gather them up!"
    "I try to look away once more as the masked killers pile up the others, taking no care to cause more pain as they drag the bodies out of the pit."
    "The creep seems to be struggling to limp over to the others."
    hide bread
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
    hide athlete 
    show creep at right
    creep "We need to do something! We need to..."
    creep "Kill the Bread Head!"
    menu: 
        "I agree.": 
            hide older 
            show mc at left 
            pov "That's not a bad idea! Maybe we can take them! There's more of us."
            "I feel a rush of energy at the idea, maybe this could work!"
            $ hasIdea = True
        "I disagree": 
            hide older 
            show mc annoyed at left
            pov "Are you kidding? How are we going to do that?"
            creep "We just... jump him and beat the shit out of him."
    hide mc 
    show older shirt annoyed at left 
    older "Boys, now is not the time. Are you forgetting that they have guns?"
    hide older 
    show athlete annoyed at left 
    ath "Besides, you don't really know how many of those masked freaks are with him. There's at least two, but maybe there's more."
    hide athlete
    hide creep
    play audio loudspeakerCrackle
    "Any further discussion is interupted by a voice over the loudspeaker again."
    jump murderSomeone
    
#Round 3 (murder someone)
label murderSomeone:
    show bread at left
    bread "Woohoo! We are halfway there! I'm sure the past games were wonderfully exhilarating but you all deserve a break. You've earned it!"
    bread "This round will be an interesting one, you don't have to compete! You will just have to make a choice."
    bread "Yes, one of you will be eliminated from the game and the remaining ones will move on to the next round, but the choice is up to you!"
    bread "YOU choose who gets to be eliminated."
    bread "Good luck, champs, you are halfway there!"
    hide bread
    "Silence."
    "Everyone in the locker room just cast nervous glances at each other."
    show bluehair annoyed at left
    "Another Bitchy Athlete" "He is halfway dead, isn't he."
    "The creep with a bloodied broken leg is lying on one of the benches. Everyone turns back to look at him."
    show athlete annoyed at right
    ath "I say we get rid of that dirtbag."
    hide bluehair 
    hide athlete
    play music loss
    menu:
        "The air around me grows tense. I decide to..."
        "Sacrifice myself.":        
            jump sacrificeEnd
        "Kill the creep.":
            $ cruel += 1 
            "You resolutely march over to the bench and glare down at the creep with contempt."
            show creep scared at left
            creep "Hey man..."
            creep "P-please don't."
            hide creep
            "Too bad."
            play audio manScream4
            "You ball up your fists and start striking him repeatedly with increasing aggressiveness."
            "His face becomes a disfigured bloody mush."
            "Other contestants, except the old man, also participate in the killing."
            show mc annoyed at left
            pov "..."
            show older shirt scared at right
            older "..."
            "Whatever it takes to win, right?"
            $ Achievement.add(achievement_name['killedSomone'])
        "Kill the bitchy athlete":
            $ cruel += 1 
            show mc annoyed at left
            "You grab a skipping rope and throw it over the girl's neck to strangle her."
            show athlete scared at right
            ath "What the-"
            hide athlete
            play audio womanScream2
            "She tries to loosen the rope by tugging it but it becomes increasingly hard as the rope constricts her neck."
            "Her movements slow down and she is in her death throes."
            "She eventually collapses and her lifeless limp body drops down on the floor..."
            pov "..."
            show older shirt scared at right
            older "..."
            $ Achievement.add(achievement_name['killedSomeone'])
        "Kill the old man":
            $ cruel += 1
            show mc annoyed at left
            "You grab a metal bar and march over to the old guy."
            "One blow a swift strike to his leg and he trips over and lets out a yelp."
            play audio manScream3
            show older shirt scared at right
            older "AAAAARGH!"
            hide older
            play audio crushed
            "You beat him him up as other contestants watch the scene in horror."
            "..."
            "Whatever it takes to win, right?"
            $ Achievement.add(achievement_name['killedSomeone'])
        "Stay out of it.": 
            $ coward += 1 
            play audio crushed
            "I stand beside the older man as the athlete picks up a shot put and pummels the creep."
            "I feel better about myself having not participated in the killing... but does it really matter?"

    play music main
    hide mc
    hide older
    show killer annoyed at left
    "After a few minutes, a few of the masked killers barge into the room and view the bloody scene."
    show killer sad at left
    play audio loudspeakerCrackle
    "They mumble something and the loudspeakers crackle back on as the Bread Head's chirpy voice rings through."
    hide killer
    show bread at left
    bread "Seems like you've got blood on your hands! I like the enthusiasm, heh heh! Well, at least we are closer to the prize, aren't we?"
    bread "So cheer up, chumps, we are halfway there! No breaks here, we've got to get going. VAMOOSE!"
    hide bread
    scene black with fade
    "The contestants plod back to the field, wondering what sort of hellish nightmare awaits them now..."
    jump obstacleCourseStart

label sacrificeEnd: 
    $ Achievement.add(achievement_name['sacrificeThird'])
    play music SadEnd
    $ kind += 1 
    if hasKnife:
        "You pull the knife out from your waistband and stab yourself over and over again frenziedly."
        play audio impaled
        "A stinging pain shoots from your chest and blood gushes out."
        "Everything fades to black..."
        scene black with fade 

    else:
        play audio crushed
        "You find an iron shot put ball and bash your head in with it repeatedly. You feel someone try to pull you away..."
        "Your head is wounded and crimson liquid trickles down from the gaping wound."
        play audio impaled
        "Your vision grows blurry as you grab a javelin spear nearby and stab yourself with it..."
        "Everything fades to black..."
        show black with fade
    call achievementCheck
    return 

label obstacleCourseStart: 
    scene obstacle horror bg
    "While we were in the locker room the masked killers must have been busy. There is an entire obstacle course set up now, covered in pointy spikes and traps."
    show bread at left
    if hasIdea and hasKnife: 
        menu: 
            "It's time for the Bread Head to pay.": 
                jump stabbedBread
            "It won't make a difference.": 
                "I do nothing, and wait."
    bread "Well well well, time to get yer bodies moving! This is a fun one!"
    bread "An obstacle course consisting of various activities that will test your agility." 
    bread "Be quick! Dont' fall behind, unless you want to get stabby stabbed to death of course, heh heh!"
    bread "Good luck, chumps!"
    play audio horn 
    jump obstacleStart

label obstacleEnd: 
    if score >= 15: 
        $ Achievement.add(achievement_name['survivedObstacle'])
        "I make my way up the rope wall, avoiding the glass shards stuck in the rope."
        "I try not to look behind me as the masked killers slowly follow behind with metal poles."
        if not killedBitch: 
            play audio womanScream3
            "I swing across the monkey bars quickly, the athletic woman trying to keep pace. However, she slips and falls."
            "I can't let myself stop."
        if not killedCreep: 
            play audio manScream4
            "I hear the masked killers catch up with the creep who couldn't pull himself up the rope wall with a bum leg."
        play audio manScream2
        "The screams of pain as people fall tears at my stomach."
        "But I don't stop and make it to the end with a solid landing."
        play audio horn 
        show bread at left 
        play music main
        bread "WoooHooo! Enthralling! That's the teamspirit, or the lack of it, should I say hmmm?"
        bread "Haha! Keep it up, you'll definetyly be needing it in the next game!"
        jump gameFiveRules
    else: 
        jump obstacleDeath

label gameFiveRules: 
    scene field horror bg
    show bread at left 
    bread "And here we are at the final round!"
    bread "Woohoo! Pat yourself on the back for making it until here, friends, you've earned it!"
    bread "But don't celebrate quite yet, only one of you can go home with the grand prize!"
    bread "So let's get started with the final game, shall we?"
    bread "An exciting game of javelins. Each f you will have a chance to throw javelins at each other and the last one standing will be the uncontested winner of the match!"
    bread "Good luck, champs!"
    hide bread
    "As the masked killers clear the obstacle course, I see that there's only two of us left. A fitting final end." 
    if killedOld: 
        jump npcFive
    else: 
        jump oldFive

label npcFive: 
    "I stare down with the girl who is left."
    show mc at left 
    pov "We don't have to do this."
    show con2 annoyed at right 
    "Last Contestant" "Don't we?"
    "The masked killers indicate where we're supposed to stand and then hand us each a single javelin."
    menu: 
        "Sacrifice myself.": 
            $ kind += 1 
            play audio impaled
            "I want to go out in my own way, so I turn the javelin in on my self." 
            scene black with fade
            jump sacrificeEpilogue
        "Kill the girl.": 
            "I know I can hit my target at this distance."
            play audio horn 
            "I throw the javelin as soon as the horn goes off."
            play audio impaled
            show con2 scared 
            "She doesn't have a chance to react to the javelin sinking into her chest."
            jump javelinKill
        "Refuse to participate": 
            play audio horn
            "I hold the javelin off to the side, clearly not going to throw it."
            play audio impaled
            show mc scared 
            "She doesn't have the same qualms, and I feel the javelin sink into my stomach."
            scene black with fade
            "Everything fades to black."
            jump badEpilogue

label oldFive: 
    "I stare down with the older man who is left."
    show mc at left 
    pov "We don't have to do this."
    show older shirt at right
    if kind > cruel: 
        older "No, we don't."
    else: 
        older "..."
    menu: 
        "Sacrifice myself.": 
            $ kind += 1 
            play audio impaled
            "I want to go out in my own way, so I turn the javelin in on my self." 
            scene black with fade
            jump sacrificeEpilogue
        "Kill the older man.": 
            "I know I can hit my target at this distance."
            play audio horn
            "I throw the javelin as soon as the horn goes off."
            play audio impaled
            show older shirt scared 
            "He doesn't have a chance to reach to the javelin sinking into his chest."
            jump javelinKill
        "Refuse to participate.": 
            play audio horn
            "I hold the javelin off to the side, clearly not going to throw it."
            if kind > cruel: 
                "The older man does the same thing."
                jump nowinnerEpilogue 
            else: 
                "But the older man doesn't seem to care. Instead he throws the javelin at me."
                show mc scared
                "His aim is true, and the javelin sinks into my chest."
                scene black with fade
                "Everything fades to black."
                jump badEpilogue
            

label javelinKill: 
    "My victim lets out a gurgle and bleeds to death."
    scene podium horror bg 
    show mc at right 
    play music goodEnd noloop
    "I stagger over to the winner's podium and raise my hands into the air in victory."
    show bread at left
    $ Achievement.add(achievement_name['winner'])
    bread "Woohoo! Ding ding ding, we have a winner!"
    bread "Congratulations, you are the uncontested champion of the Dreadfield Games! You were unstoppable out there."
    "Perhaps its the adrenaline or the fear, but I find myself feeling light headed all of the sudden."
    scene black with fade 
    "Everything fades to black."
    call achievementCheck
    return

label nowinnerEpilogue: 
    play music SadEnd
    "I let out a sigh."
    "The Bread Head seems troubled by the whole exchange."
    hide mc 
    hide older 
    show bread at left 
    $ Achievement.add(achievement_name['nowinner'])
    bread "N-no! No. No. No! You can't just not kill each other!"
    bread "This is going against the rules! One of you will have to do it!"
    bread "Kill! Kill! Kill! Don't you want the prize?"
    "He jumps up and down like a petulant child."
    "Once he sees that we have both made up our minds, he seems miffed."
    bread "Hmphf. Bah! no prizes for you then."
    bread "What a buncha losers. But don't think the fun is over yet, heh heh!"
    show killer at right
    killer "..."
    "The masked killer suddenly appears again, cocking a gun."
    "At least it will be quick."
    play audio gunshotClose
    scene black with fade
    "Everything fades to black."
    call achievementCheck
    return

label badEpilogue: 
    play music badEnd noloop
    "No act of mercy here. That isn't how the world works."
    "Your luck had to run out sooner or later."
    "I can here the Bread Head's cheery words as I vaguely feel myself dragged off somewhere."
    call achievementCheck
    return

label sacrificeEpilogue: 
    $ Achievement.add(achievement_name['sacrificeThird'])
    play music SadEnd
    scene black 
    show bread at left
    bread "Ah, how charming. What a gentlemen. A noble act, indeed!"
    bread "Why even bother in the first place then, huh?"
    bread "Strange happenings, but now we finally have a winner!"
    "I can here the Bread Head's cheery words as I vaguely feel myself dragged off somewhere."
    call achievementCheck
    return 


label obstacleDeath: 
    play music badEnd noloop
    "I make it to the climbing nets before a masked killer catches up with me."
    show killer at right 
    play audio crushed
    killer "..."
    "The last thing I see before I die is that stupid orange face."
    $ Achievement.add(achievement_name['diedObstacle'])
    scene black with fade 
    call achievementCheck
    return

label shotBadEnd:
    play music badEnd noloop
    "Maybe walking away wasn't the best idea."
    "Try again?"
    call achievementCheck
    return

#starts the long jump mini game
label start_minigame:
    show screen fable_timer_left
    call screen fable_2_minigame

label end_minigame: #End minigame. And jump continue game
    hide screen fable_2_minigame
    $ renpy.pause(0.3)
    jump longJumpEnding #continue game

label timingFailure:
    $ Achievement.add(achievement_name['diedJump'])
    play music loss 
    "I take a deep breath and then run towards the sand pit."
    "Unfortunately, I do not make the distance I was hoping to..."
    play audio manScream1
    play sound crushed 
    "I scream in pain as I land on a bear trap."
    show bread at left 
    bread "Oh, too bad! That's a lot of blood."
    "I have to agree as everything fades to black."
    scene black with fade 
    "Better luck next time!"
    "Try again?"
    call achievementCheck
    return


label obstacleStart: 
    play music minigame
    centered "Click the Bread Heads as they appear!{w=1}{nw}"
    $setup_reflex_game() #set up the minigame
    call screen reflex_minigame
    
label stabbedBread: 
    "Before he's able to speak in that annoying voice, I jump at the Bread Head with my knife."
    play audio impaled
    "I stab into him repeatedly, but I don't see any blood before the masked killers are on me."
    bread "Oh ho ho, what a fiesty one you are."
    play audio gunshotClose
    "The shot rings out, and soon I feel nothing."
    scene black with fade
    $ Achievement.add(achievement_name['stabbedBread'])
    "Everything fades to black."
    call achievementCheck
    return

label achievementCheck: 
    python: 
        if kind => 3: 
            Achievement.add(achievement_name['kind'])
        if cruel => 3: 
            Achievement.add(achievement_name['cruel'])
        if coward => 2: 
            Achievement.add(achievement_name['coward'])
        if Achievement.has(achievement_name['diedRun'].name) and \
        Achievement.has(achievement_name['diedObstacle'].name) and \
        Achievement.has(achievement_name['diedJump'].name) and \
        Achievement.has(achievement_name['nowinner'].name) and \
        Achievement.has(achievement_name['loser'].name): 
            Achievement.add(achievement_name['allBad'])
