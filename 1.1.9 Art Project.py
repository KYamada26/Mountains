# 1.1.9 Art Project
import turtle as trtl
painter = trtl.Turtle()
painter.speed(0)

# draw sky
painter.pencolor("#FF9C07")
painter.fillcolor("#FF9C07")
painter.begin_fill()
side_length = 1100
painter.penup()
painter.goto(-550,-550)
painter.pendown()
painter.setheading(90)
for _ in range(4):
    painter.forward(side_length)
    painter.right(90)
painter.end_fill()

# set up mountains
painter.hideturtle()
painter.shape("classic")
painter.pensize(0)
painter.speed(0)
mountx = -600
mounty = -450
sidelength = 600
# draw mountains
for mountainrange in range(2):
  painter.penup()
  painter.pensize(5)
  painter.pencolor("#107C14")
  painter.fillcolor("#107C14")
  painter.goto(mountx,mounty)
  painter.begin_fill()
  painter.pendown()
  painter.setheading(65)
  # triangles
  for mountain in range(2):
      painter.forward(sidelength)
      painter.right(130)
  painter.end_fill()
  mountx = mountx + 450
  sidelength = sidelength + 200

# set up snow
snowx = -388.5
snowy = 3
snowlength = 100
# draw snow
for snow in range(2):
  painter.penup()
  painter.pensize(6.5)
  painter.pencolor("#FFFFFF")
  painter.fillcolor("#FFFFFF")
  painter.goto(snowx,snowy)
  painter.begin_fill()
  painter.pendown()
  painter.setheading(65)
  # triangles
  for snow in range(2):
      painter.forward(snowlength)
      painter.right(130)
  painter.end_fill()
  snowx = snowx + 491.5
  snowy = snowy + 90
  snowlength = snowlength + 100

# create and move sun
painter.penup()
painter.showturtle()
painter.goto(800,-400)
painter.setheading(90)
painter.speed(1)
painter.turtlesize(7)
painter.shape("circle")
painter.pencolor("yellow")
painter.fillcolor("yellow")
painter.circle(800,180)

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()