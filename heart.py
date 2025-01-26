import turtle
import math

def hearta(K):
    return 15 *math.sin(K)**3
def heartb(K):
    return 12 *math.cos(K) - 5*math.cos(2*K) - 2*math.cos(3*K) - math.cos(4*K)
window=turtle.Screen()
window.setup(width=800,height=600)
# window.title("Heart shape")
window.bgcolor("black")

pen=turtle.Turtle()
pen.speed(0)
pen.hideturtle()

for i in range(6000):
    x = hearta(i) * 20
    y = heartb(i) * 20
    pen.goto(x, y)
    
    r = abs(math.sin(i/300))
    g = abs(math.sin(i/200))
    b = abs(math.sin(i/100))
    pen.pencolor(r, g, b)
    pen.pendown()
pen.penup()
pen.goto(0,-50)
pen.color("white")
pen.write("Happy Valentine's Day",align="center",font=("Arial",24,"normal"))
# window.mainloop()
turtle.done()