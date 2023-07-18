screen clicker:
    modal True
    timer .5 repeat True action [If(points <= 0, true=Jump("clickLost"), false=SetVariable("points", points - plus))]
    imagebutton:
        idle "mc temp"
        xpos .8
        ypos 1
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("clickWin"), false=SetVariable("points", points + plus))]
    vbar value StaticValue(points, max_point)

