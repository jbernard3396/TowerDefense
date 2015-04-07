import cTurtle
from random import *

def turtleDrawCircle(radius,myTurtle):  
    for i in range (radius):
        turnAngle=360/radius
        myTurtle.forward(6.28)
        myTurtle.right(turnAngle)
    myTurtle.forward(6.28)

def turtleDrawHalfCircle(radius,myTurtle):
    for i in range (radius):
         turnAngle=180/radius
         myTurtle.forward(3.14)
         myTurtle.right(turnAngle)
    myTurtle.forward(3.14)

def drawRegularPoly(numSides,sideLength,myTurtle):
    turnAngle=360/numSides
    for i in range (numSides):
        myTurtle.fd(sideLength)
        myTurtle.left(turnAngle)

def drawTowerLocation1():
    import cTurtle
    towerDrawer=cTurtle.Turtle()
    td=towerDrawer
    td.speed(10)
    td.tracer(False)
    td.up()
    td.right(180)
    td.fd(107)
    td.left(90)
    td.fd(120)
    td.down()
    turtleDrawCircle(15,td)
    td.up()
    td.fd(100000)
    td.tracer(True)

def drawTowerLocation2():
    import cTurtle
    towerDrawer=cTurtle.Turtle()
    td=towerDrawer
    td.tracer(False)
    td.up()
    td.left(180)
    td.speed(10)
    td.fd(7)
    td.left(90)
    td.fd(20)
    td.down()
    turtleDrawCircle(15,td)
    td.up()
    td.fd(100000)
    td.tracer(True)

def drawTowerLocation3():
    import cTurtle
    towerDrawer=cTurtle.Turtle()
    td=towerDrawer
    td.speed(10)
    td.tracer(False)
    td.up()
    td.fd(100)
    td.left(90)
    td.fd(70)
    td.down()
    turtleDrawCircle(15,td)
    td.up()
    td.fd(100000)
    td.tracer(True)

def setupForSpawn(t):
    t.tracer(False)           #not actually used
    t.up()
    t.goto(-190,190)
    t.down()
    t.tracer(True)
    
def drawEvilSquare(t):
    t.tracer(False)
    t.down()
    drawRegularPoly(4,30,t)           #not actually used
    t.up()
    t.tracer(True)

def spawnEvilSquare(t,x,y):
##    t.tracer(False)           
    t.up()
    t.right(90)
    t.goto(x,y)
    t.down()
    t.color('red')
    t.fill('red')
    drawRegularPoly(4,30,t)
    t.fill('red')
    t.up()
##    t.fd(10)
    t.tracer(True)
    t.tracer(False)

def moveEvilSquareRight(t,Length,x,y,speed):
    t.right(90)
    for forwardAmmt in range (Length//speed):
        spawnEvilSquare(t,x,y)
        x=x+speed
        t.reset()

def moveEvilSquareLeft(t,Length,x,y,speed):
    t.right(90)
    for forwardAmmt in range (Length//speed):
        spawnEvilSquare(t,x,y)
        x=x-speed
        t.reset()

def moveEvilSquareDown(t,Length,x,y,speed):
    t.right(90)
    for forwardAmmt in range (Length//speed): #change den to speed
        spawnEvilSquare(t,x,y)
        y=y-speed
        t.reset()

def moveEvilSquareUp(t,Length,x,y,speed):
    t.right(90)
    for forwardAmmt in range (Length//speed): #change den to speed
        spawnEvilSquare(t,x,y)
        y=y+speed
        t.reset()

def funcSetDown(t,Length,x,y):
    for forwardAmmt in range (Length//2):
        y=y-2
    return y

def funcSetRight(t,Length,x,y):
    for forwardAmmt in range (Length//2):
        x=x+2
    return x

def funcSetUp(t,Length,x,y):
    for forwardAmmt in range (Length//2):
        y=y+2
    return y

def funcSetLeft(t,Length,x,y):
    for forwardAmmt in range (Length//2):
        x=x-2
    return x

##def setX(Length,x,y):
##    x=funcSetX(t,Length,x,y)  #doesn't work?

##def setY(Length,x,y):
##    y=funcSetY(t,Length,x,y)  #doesn't work?
        
def moveEvilSquareMap1(t):
    x=-190
    y=160
    moveEvilSquareDown(t,320,x,y,10)
    y=funcSetDown(t,320,x,y,)
    moveEvilSquareRight(t,350,x,y,10)
    x=funcSetRight(t,350,x,y)
    moveEvilSquareUp(t,100,x,y,10)
    y=funcSetUp(t,100,x,y)
    moveEvilSquareLeft(t,250,x,y,10)
    x=funcSetLeft(t,250,x,y)
    moveEvilSquareUp(t,250,x,y,10)
    y=funcSetUp(t,250,x,y)
    moveEvilSquareRight(t,100,x,y,10)
    x=funcSetRight(t,100,x,y)
    moveEvilSquareDown(t,150,x,y,10)
    y=funcSetDown(t,150,x,y,)
    moveEvilSquareRight(t,150,x,y,10)
    x=funcSetRight(t,150,x,y)
    moveEvilSquareUp(t,150,x,y,10)
    y=funcSetUp(t,150,x,y)

def spawnSeriesOfEnemies(numEnemies):
    for newName in range (numEnemies):
        import cTurtle                      #still spawns one at a time
        newName=cTurtle.Turtle()
        moveEvilSquareMap1(newName)
        
           
def drawMap1():
    mapDrawer=cTurtle.Turtle()
    mapDrawer2=cTurtle.Turtle()
    md=mapDrawer
    md2=mapDrawer2
    md.tracer(False)
    md2.tracer(False)
    md2.speed(10)
    md.speed(10) 
    md.up()
    md2.up()
    md.goto(-200,200)
    md2.goto(-150,200)
    md.right(90)
    md2.right(90)
    md.down()
    md2.down()
    md.fd(400)
    md2.fd(350)
    md.left(90)
    md2.left(90)
    drawTowerLocation1()
    md.fd(400)
    md2.fd(300)
    md.left(90)
    md2.left(90)
    md.fd(150)
    md2.fd(50)
    md.left(90)
    md2.left(90)
    md.fd(250)
    md2.fd(250)
    md.right(90)
    md2.right(90)
    drawTowerLocation2()
    md.fd(200)
    md2.fd(300)
    md.right(90)
    md2.right(90)
    md.fd(50)
    md2.fd(150)
    md.right(90)
    md2.right(90)
    md.fd(150)
    md2.fd(150)
    md.left(90)
    md2.left(90)
    md.fd(200)
    md2.fd(100)
    md.left(90)
    md2.left(90)
    drawTowerLocation3()
    md.fd(200)
    md2.fd(150)
    md.up()
    md2.up()
    md.fd(1000)
    md2.fd(1000)
    md.tracer(True)
    md2.tracer(True)


    
    
drawMap1()
spawnSeriesOfEnemies(2)




