# Impor modul yang diperlukan
from turtle import *
from random import randint

# Bentuk asli kura-kura
speed(0)
penup()
goto(-140, 140)
for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

# Detail pemain pertama
plyr1 = Turtle()
plyr1.color('magenta')
plyr1.shape('turtle')

# Proses pemain pertama ke trek balap
plyr1.penup()
plyr1.goto(-160, 100)
plyr1.pendown()
for turn in range(10):
    plyr1.right(36)

# Detail pemain kedua
plyr2 = Turtle()
plyr2.color('red')
plyr2.shape('turtle')

# Proses pemain kedua ke trek balap
plyr2.penup()
plyr2.goto(-160, 70)
plyr2.pendown()
for turn in range(72):
    plyr2.left(5)

# Detail pemain ketiga
plyr3 = Turtle()
plyr3.color('lightgreen')
plyr3.shape('turtle')

# Proses pemain ketiga ke trek balap
plyr3.penup()
plyr3.goto(-160, 40)
plyr3.pendown()
for turn in range(60):
    plyr3.right(6)

# Detail pemain keempat
plyr4 = Turtle()
plyr4.color('blue')
plyr4.shape('turtle')

# Proses pemain keempat ke trek balap
plyr4.penup()
plyr4.goto(-160, 10)
plyr4.pendown()
for turn in range(30):
    plyr4.left(12)

# Kura-kura berlari dengan kecepatan acak
for turn in range(100):
    plyr1.forward(randint(1, 5))
    plyr2.forward(randint(1, 5))
    plyr3.forward(randint(1, 5))
    plyr4.forward(randint(1, 5))

# Menunggu klik pada jendela untuk menutupnya
exitonclick()
