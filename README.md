# Mountains
#1.1.9 Algorithms and Art Project
#   1.1.9 Art Project
import turtle as trtl
painter = trtl.Turtle()
painter.speed(10)
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

# draw sun
painter.penup()
painter.goto(-200,270)
painter.pendown()
painter.pensize(70)
painter.pencolor("#FFFB00")
painter.circle(35)

# set up mountains
mountx = -600
mounty = -450
sidelength = 650
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
  # triangle
  for mountain in range(2):
      painter.forward(sidelength)
      painter.right(130)
  painter.end_fill()
  mountx = mountx + 450
  sidelength = sidelength + 200


painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()
