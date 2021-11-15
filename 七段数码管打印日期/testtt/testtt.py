
from math import *
from random import *
from turtle import *
from datetime import *

def drawGap():
    penup()
    fd(5)

def drawLine(draw):
    drawGap()
    pendown() if draw else penup()
    fd(40)
    drawGap()
    right(90)

def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    left(180)
    penup()
    fd(20)

def drawDate(date):
    pencolor("red")
    for i in date:
        if i=='-':
            write('年',font=("Arial",30,"normal"))
            pencolor("green")
            fd(40)
        elif i=='=':
            write('月',font=("Arial",30,"normal"))
            pencolor("blue")
            fd(40)
        elif i=='+':
            write('日',font=("Arial",30,"normal"))
        else:    
            drawDigit(eval(i))

def main():
    setup(800,350,200,200)
    penup()
    fd(-350)
    pensize(5)
    drawDate(datetime.now().strftime('%Y-%m=%d+'))
    hideturtle()

main()



 