import turtle

turtle.colormode(255)
turtle.color(255, 0, 0)
turtle.pensize(2)
def ucgenCiz():
    for x in range(3):
        turtle.forward(100)
        turtle.left(120)
        
turtle.begin_fill()
turtle.fillcolor(165,42,255)
ucgenCiz()
turtle.end_fill()