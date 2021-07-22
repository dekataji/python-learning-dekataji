import turtle

turtle.bgcolor("black")
square = turtle.Turtle()
colors=["red",'blue','green','yellow']

def squared():
    deg = 0
    rotation = 20
    for x in range(int(360/rotation)):
        square.right(rotation)
        for i in range(4):
            square.color(colors[i])
            square.forward(200)
            square.right(90)
        
squared()

