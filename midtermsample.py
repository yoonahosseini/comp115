import turtle

def draw_sunbeams(t, num_beams):
  """
  This function makes turtle t draw num_beams beams for a sun.
  Given beam length is 20 pixels long (120 - 140 pixels from the origin)
  """
  angle = 360 / num_beams
  for _ in range(num_beams):
    t.up()
    t.forward(120)
    t.down()
    t.forward(20)
    t.up()
    t.backward(140)
    t.right(angle)

window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(1)

radius = 100

# Draw a sun
pen.up()
pen.goto(0, -radius)
pen.down()
pen.circle(radius)
pen.up()
pen.goto(0, 0)

# Draw sun beams
draw_sunbeams(pen, 12)

pen.shape('blank')

window.exitonclick()
