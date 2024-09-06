import drawly

drawly.start("Jonny's snowman", background="lightblue")
drawly.set_speed(7)

def title():
    drawly.set_color("black")
    drawly.text(200, 150, "Jonny's Snowman", 30)
    drawly.draw()

def ground():
    drawly.set_color("white")
    drawly.ellipse(-150, 650, 1500, 200)
    drawly.draw()
    drawly.set_color("darkgreen")
    drawly.ellipse(0, 675, 1280, 100)
    drawly.draw()

def tree():
    drawly.set_color("black")
    drawly.rectangle(948, 398, 104, 702)
    drawly.set_color("saddlebrown")
    drawly.rectangle(950, 400, 100, 700)
    drawly.draw()
    drawly.set_color("forestgreen")
    drawly.circle(1000, 300, 202)
    drawly.draw()
    drawly.set_color("limegreen")
    drawly.circle(1000, 300, 200)
    drawly.draw()

def snowman_body():
    drawly.set_color("black")
    drawly.circle(650, 600, 155)
    drawly.draw()
    drawly.set_color("white")
    drawly.circle(650, 600, 150)
    drawly.draw()
    drawly.set_color("black")
    drawly.circle(650, 400, 105)
    drawly.draw()
    drawly.set_color("white")
    drawly.circle(650, 400, 100)
    drawly.draw()
    drawly.set_color("black")
    drawly.circle(650, 270, 70)
    drawly.draw()
    drawly.set_color("white")
    drawly.circle(650, 270, 65)
    drawly.draw()

def hat():
    drawly.set_color("black")
    drawly.rectangle(580, 150, 140, 60)
    drawly.draw()
    drawly.set_color("darkred")
    drawly.rectangle(582, 152, 136, 58)
    drawly.draw()
    drawly.set_color("black")
    drawly.rectangle(550, 195, 200, 25)
    drawly.draw()
    drawly.set_color("darkred")
    drawly.rectangle(552, 197, 196, 23)
    drawly.draw()

def face():
    drawly.set_color("black")
    drawly.circle(635, 250, 6)
    drawly.circle(665, 250, 6)
    drawly.draw()
    drawly.circle(610, 275, 4)
    drawly.circle(690, 275, 4)
    drawly.draw()
    drawly.circle(630, 290, 4)
    drawly.circle(670, 290, 4)
    drawly.draw()
    drawly.circle(650, 295, 4)
    drawly.draw()

def arms():
    drawly.set_color("sienna")
    drawly.line(550, 400, 400, 300, 20)
    drawly.line(750, 400, 900, 300, 20)
    drawly.draw()

    #left fingers
    drawly.line(400, 300, 350, 250, 10)
    drawly.line(400, 300, 400, 250, 10)
    drawly.line(400, 300, 370, 350, 10)
    drawly.draw()
    #right fingers
    drawly.line(900, 300, 950, 250, 10)
    drawly.line(900, 300, 900, 250, 10)
    drawly.line(900, 300, 925, 350, 10)
    drawly.draw()

def buttons():
    drawly.set_color("orange")
    drawly.circle(650, 375, 10)
    drawly.draw()
    drawly.circle(650, 425, 10)
    drawly.draw()
    drawly.circle(650, 475, 10)
    drawly.draw()

def sun():
    drawly.set_color("yellow")
    drawly.circle(100, 100, 80)
    drawly.draw()

    drawly.set_color("gold")
    drawly.circle(100, 100, 75)
    drawly.draw()

    # sun rays
    drawly.set_color("yellow")
    drawly.line(100, 20, 100, -20, 10)
    drawly.line(20, 100, -20, 100, 10)
    drawly.draw()
    drawly.line(180, 100, 220, 100, 10)
    drawly.line(100, 180, 100, 220, 10)
    drawly.draw()

# Animate the drawing process
ground()
tree()
snowman_body()
hat()
face()
arms()
buttons()
sun()
title()

drawly.done()
