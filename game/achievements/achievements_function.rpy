python early:


    class Achievement(NoRollback):
        def __init__(self, name='', image='', message='', priority=None, **kwargs):
            ## The name of the achievement.
            self.name = name

            ## The image of the achievement.
            if image == '':
                ## If image is None, a default image will be used.
                self.image = Transform('gui/trophy_icon.png', fit='contain')
            else:
                self.image = Transform(image, fit='contain')

            ## The message associated with the achievement.
            self.message = message

            ## Set the priority of the achievement.
            ##            None = default (greyed out and can see the name and description of the achievement.)
            ##        'hidden' = Achievements with this tag will be displayed as 'hidden'.
            ##      'platinum' = The final achievement to be granted once all other achievements have been granted.
            self.priority = priority

        def __eq__(self, value):
            ## Since we are using a persistent list we need to do an equality check.
            ## Below we are simply checking 'self.name == value.name, self.message == value.message'
            return all((self.name == value.name, self.message == value.message))

        def add(trophy):
            ## Add/Grant Trophies/Achievements to the list.
            ## As a standard python expression  ::  Achievement.add( <trophy> )
            ## As a screen action  ::  Function( Achievement.add, <trophy> )
            if not achievement.has(trophy.name):
                achievement.grant(trophy.name)
                store.achievement_is_done = False
                store.achievement_notification_timer = 3.0
                store.achievement_notification_list.append(trophy)

            if trophy not in persistent.my_achievements:
                ## New acheievements will appear first in the list.
                persistent.my_achievements.insert(0, trophy)
            achievement.sync()

        def purge(self):
            ## This will clear the achievements AND persistent list.
            ## As a standard python expression  ::  achievements.purge()
            ## As a screen action  ::  Function( achievements.purge )
            achievement.clear_all()
            persistent.my_achievements.clear()


## DO NOT TOUCH/REUSE/CHANGE THIS AT ANY TIME!
## To clear this list use ::  achievements.purge()
default persistent.my_achievements = []
default achievements = Achievement()

init python:

    ## Note - This has not been implemented to work with Steam.
    ##        You'll have to work that out on your own if you want it to work with steam.
    ##        I have left some Steam stuff in place, but these haven't been elaborated upon.
    achievement.steam_position = "bottom right"

    achievement_name = {

        ## -------------------------- IMPORTANT (1) --------------------------
        ## 
        ## How to set up achievements
        ## "achievement_key": Achievement(name=_("Name of Achievement"), message=_("Description"), image='<image_path_here>', priority='<type>'),

        ## -------------------------- IMPORTANT (2) --------------------------
        ## Note: If you decide to add/amend any achievement's data long after the game has started or
        ##       an achievement has been granted you will have to do a full reset of the game for those
        ##       changes to be reflected. I.e. Delete persistent data.

        ## -------------------------- EXAMPLES -------------------------- 
    

        ## The prio, means that the achievement will be displayed greyed-out before it is granted (or achieved).
        ## I use these terms to describe the types of achievements;
        ##            None = default (greyed out and can see the name and description of the achievement.)
        ##        'hidden' = Achievements with this label will be displayed as 'hidden'.
        ##      'platinum' = The final achievement to be granted once all other achievements have been granted.

        "gotKnife": Achievement(name=_("Sharper than Expected"), message=_("Unlocked for acquiring a knife and embracing the cutting edge of danger. Watch your step!"), image = 'gui/knifeAch.png', priority='hidden'), 
        "survivedRun": Achievement(name=_("The Last Lap"), message=_("Cruised to success and claimed the win in the death race!"), image = 'gui/runWinAch.png', priority='hidden'),
        "diedRun": Achievement(name=_("Fatal Fumble"), message=_("Met the masked killer's deadly embrace after a chilling run-in."), image = 'gui/runLossAch.png', priority='hidden'),
        "walkAway": Achievement(name=_("Rebel Without A Cheer"), message=_("Chose defiance over the deadly games and faced a fateful farewell shot. A free spirit till the end!"), image = 'gui/walkAwayAch.png', priority='hidden'), 
        "survivedJump": Achievement(name=_("Leap of Legends"), message=_("Nailed the long jump game and lived to tell the tale! Gravity's got nothing on you!"), image = 'gui/jumpWinAch.png', priority = 'hidden'), 
        "diedJump": Achievement(name=_("Trapped in Misfortune"), message=_("Fell victim to a bear-y unfortunate end after a botched long jump. Watch your step!"), image = 'gui/jumpLossAch.png', priority = 'hidden'),
        "sacrificeThird": Achievement(name=_("Conscience Cuts Deep"), message=_("Made a life-altering choice and turned the knife on yourself instead. A haunting decision."), image = 'gui/SuicideOneAch.png', priority = 'hidden'), 
        "killedSomeone": Achievement(name=_("Deadly Decision Maker"), message=_("Chose a dark path and became a willing participant in another's demise. A chilling turn of events."), image = 'gui/killerAch.png', priority = 'hidden'), 
        "stabbedBread": Achievement(name=_("Flour Power"), message=_("Tried to take down the masked mascot but got stabbed instead. A half-baked plan!"), image = 'gui/breadStabber.png', priority = 'hidden'), 
        "diedObstacle": Achievement(name=_("Obstacle Obliteration"), message=_("Tried to conquer the deadly obstacle course, but stumbled into perilous pitfalls. A trial to regret."), image = 'gui/obstacleLossAch.png', priority = 'hidden'), 
        "survivedObstacle": Achievement(name=_("Perilous Path Master"), message=_("Conquered the labyrinth of danger in the deadly obstacle course."), image = 'gui/obstacleWinAch.png', priority = 'hidden'), 
        "nowinner": Achievement(name=_("Bread Dead"), message=_("Survived till the fifth round, and chose compassion. Slain for being \"no fun.\""), image = 'gui/noFunAch.png', priority = 'hidden'), 
        "loser": Achievement(name=_("Spear-itual Delimna"), message=_("Hesitated in the final round but your opponent had never faltered. Their javelin finds its mark."), image = 'gui/loserAch.png', priority = 'hidden'), 
        "winner": Achievement(name=_("Dreadfield Victor"), message=_("Embraced destiny's duel, and won. Victory ending in triumph in the Dreadfield's brutal arena."), image = 'gui/winnerAch.png', priority = 'hidden'),
        "allBad": Achievement(name=_("Rest In Peace"), message=_("Get every bad ending"), image = 'gui/allBadAch.png', priority = 'hidden'), 
        "kind": Achievement(name=_("Kind Soul"), message=_("Pick all the Kind options throughout the game"), image = 'gui/kindAch.png', priority = 'hidden'), 
        "cruel": Achievement(name=_("Crimson Reaper"), message=_("Pick all the Cruel options throughout the game"), image = 'gui/cruelAch.png', priority = 'hidden'), 
        "cowardly": Achievement(name=_("Faint of Heart"), message=_("Pick all the cowardly options throughout the game "), image = 'gui/cowardAch.png', priority = 'hidden')
        ## More of this is explained in 'achievement_screen.rpy'.

    }

    ## Here we are simply registering the achievements.
    ## This is solely for backend use.
    for k, v in achievement_name.items():
        achievement.register(v.name)

