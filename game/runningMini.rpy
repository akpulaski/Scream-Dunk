screen clicker:
    modal True
    timer .5 repeat True action [If(points <= 0, true=Jump("clickLost"), false=SetVariable("points", points - plus))]
    timer .5 repeat True action [If(points > 0, true=Call("showKiller"), false=Jump("clickLost"))]
    imagebutton:
        idle "mc"
        xpos .6
        ypos .3
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("clickWin"), false=SetVariable("points", points + plus))]
    
    
label showKiller:    
    if points > 75: 
        show killer annoyed at far, left
    elif points > 50: 
        show killer annoyed at closer, left
    else: 
        show killer annoyed at left
    call screen clicker

transform far: 
    zoom .5

transform closer: 
    zoom .75
