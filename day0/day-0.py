from turtle import*
#house
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#roof
penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
left(120)
forward(200)
left(120)
forward(200)
end_fill()
#door
penup()
goto(30,0)
left(120)
pendown()
forward(20)
left(90)
forward(80)
left(90)
forward(20)
left(90)
forward(80)
#window1
penup()
goto(70,180)
pendown()
forward(50)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
right(-90)
#window2
penup()
goto(130,130)
pendown()
forward(50)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
#exite
exitonclick()