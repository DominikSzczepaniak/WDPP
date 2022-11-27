import turtle 
from random import randint
turtle.speed("fastest")
turtle.colormode(255)
# turtle.tracer(0, 1)
def kwadrat(bok, kolor):
    id = []
    liczba = ""
    for i in range(1, len(kolor)-1):
        if(kolor[i] == ','):
            id.append(int(liczba))
            liczba = ""
        else:
            liczba += kolor[i] 
    id.append(int(liczba))
    turtle.begin_fill()
    turtle.fillcolor(id)
    for i in range(4):
        turtle.fd(bok)
        turtle.rt(90)
    turtle.end_fill()
    turtle.fd(bok) #zeby przejsc do kolejnego pixela po prawej

linie = []
with open("obraz.txt") as f:
    linie = f.readlines()
obraz = []
for wiersz in linie:
    test = wiersz.strip().rsplit()
    obraz.append(test)
turtle.penup()
turtle.goto(-200,-300)
turtle.pendown()
bok = 10
licznik = 1
uzyte = set()
wszystkie = 0
for i in range(len(obraz)):
    for j in range(len(obraz[i])):
        y = randint(0, len(obraz)-1)
        x = randint(0, len(obraz[0])-1)
        while((y, x) in uzyte):
            y = randint(0, len(obraz)-1)
            x = randint(0, len(obraz[0])-1)
        kwadrat(bok, obraz[y][x])
    turtle.penup()
    turtle.goto(-200, -300+licznik*bok)
    turtle.pendown()
    licznik += 1

input()



    
        