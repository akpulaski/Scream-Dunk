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
        "refuseAdventure": Achievement(name=_("No Adventure for Me Today"), message=_("Refuse to go for a walk"), image='gui/noAdvBadAch.png', priority='hidden'),

        ## The prio, means that the achievement will be displayed greyed-out before it is granted (or achieved).
        ## I use these terms to describe the types of achievements;
        ##            None = default (greyed out and can see the name and description of the achievement.)
        ##        'hidden' = Achievements with this label will be displayed as 'hidden'.
        ##      'platinum' = The final achievement to be granted once all other achievements have been granted.

        "homewrecker": Achievement(name=_("Homewrecker"), message=_("Destroy the Pixie's Home"), image='gui/homewreckerAch.png', priority='hidden'),
        "refusePixie": Achievement(name=_("I Won't Play Your Games"), message=_("Refuse the Pixie's Request"), image='gui/lostBadAch.png', priority='hidden'),
        "spiderBad": Achievement(name=_("Snug As A Fly In A Web"), message=_("String Bad End"), image ='gui/spiderBadAch.png', priority='hidden'),
        "spiderGood": Achievement(name=_("The Old Lady's String"), message=_("Got the String"), image ='gui/gotStringAch.png', priority='hidden'),
        "bumbleGood": Achievement(name=_("Bumblin' Around"), message=_("Got the Flower"), image = 'gui/gotFlowerAch.png', priority = 'hidden'), 
        "bumbleBad": Achievement(name=_("Bumblin' Fool"), message=_("Flower Bad End"), image = 'gui/bumbleBadAch.png', priority = 'hidden'), 
        "rhinoGood": Achievement(name=_("Swole Bros"), message=_("Got the Gum"), image = 'gui/gotGumAch.png', priority = 'hidden'), 
        "rhinoBad": Achievement(name=_("Weaklings"), message=_ ("Gum Bad End"), image = 'gui/rhinoBadAch.png', priority = 'hidden'), 
        "monsterous": Achievement(name=_("Monsterous"), message=_ ("Killed the Spider"), image = 'gui/killedSpiderAch.png', priority = 'hidden'),
        "dragonGood": Achievement(name=_("Ace Flying"), message=_ ("Got the Wrapper"), image = 'gui/flyerAch.png', priority = 'hidden'),
        "dragonBad": Achievement(name=_ ("Murderer!"), message=_ ("Wrapper Bad End"), image = 'gui/murderBadAch.png', priority = 'hidden'),
        "ladyGood": Achievement(name=_("My Fair Lady"), message=_ ("Got the Button"), image = 'gui/gotButtonAch.png', priority = 'hidden'),
        "ladyBad": Achievement(name=_("Aphid Snack"), message=_ ("Button Bad End"), image = 'gui/ladyBadAch.png', priority = 'hidden'), 
        "badAtThis": Achievement(name=_("Bad At This"), message=_("Got All the Bad Endings"), image = 'gui/trophy_icon.png', priority = 'hidden'), 
        "homebuilder": Achievement(name=_("Home Builder"), message=_ ("Rebuilt the Pixie's House"), image = 'gui/homeBuilderAch.png', priority = 'hidden'), 
        "overconfident": Achievement(name=_("Overconfident"), message=_("Tried to Swim Yourself"), image = 'gui/drownedBadAch.png', priority = 'hidden')
        ## More of this is explained in 'achievement_screen.rpy'.

    }

    ## Here we are simply registering the achievements.
    ## This is solely for backend use.
    for k, v in achievement_name.items():
        achievement.register(v.name)

