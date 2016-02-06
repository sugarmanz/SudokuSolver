__author__ = 'Suga'

from turtle import *

class Coordinate():

    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Number():

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.value = " "
        self.possibleVals = [1,2,3,4,5,6,7,8,9]
        self.isDrawn = False

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getVal(self):
        return self.value

    def getPossibleVals(self):
        return self.possibleVals

def boardInit():
    board = []
    i = 0
    while i < 9:
        t = 0
        board.append([])
        while t < 9:
            board[i].append(Number(i,t))
            t = t + 1
        i = i + 1
    return board

def fillInBoard(board):
    givens = dict()
    i = 1
    while i < 10:
        givens[i] = []
        i = i + 1
    file = open("puzzles/puzzleEasy.txt")
    for line in file:
        value = Coordinate(line[1],line[3])
        key = int(line[6])
        givens[key].append(value)
    for key in givens:
        list = givens[key]
        for coor in list:
            board[coor.getY()][coor.getX()].value = key
            board[coor.getY()][coor.getX()].possibleVals = []
    return board

def drawBoard():
    reset()
    ht()
    speed(0)
    up()
    goto(-301.5,301.5)
    down()
    pensize(3)
    drawHorizontal()
    pensize(1)
    drawHorizontal()
    drawHorizontal()
    pensize(3)
    drawHorizontal()
    pensize(1)
    drawHorizontal()
    drawHorizontal()
    pensize(3)
    drawHorizontal()
    pensize(1)
    drawHorizontal()
    drawHorizontal()
    pensize(3)
    drawHorizontal()
    up()
    goto(301.5,301.5)
    down()
    rt(90)
    pensize(3)
    drawHorizontal()
    pensize(1)
    drawHorizontal()
    drawHorizontal()
    pensize(3)
    drawHorizontal()
    pensize(1)
    drawHorizontal()
    drawHorizontal()
    pensize(3)
    drawHorizontal()
    pensize(1)
    drawHorizontal()
    drawHorizontal()
    pensize(3)
    drawHorizontal()
    up()
    pensize(1)
    home()
    back(4*67)
    lt(90)
    fd(4*67)
    rt(90)

def drawHorizontal():
    fd(603)
    back(603)
    rt(90)
    up()
    fd(67)
    lt(90)
    down()

def drawGivens(board):
    pencolor("black")
    for row in board:
        for number in row:
            if number.isDrawn == False and number.value != " ":
                drawNumber(number)
                number.isDrawn = True

def drawNumber(number):
    fd(number.getY()*67)
    rt(90)
    fd(number.getX()*67)
    val = number.value
    if val == 1:
        drawOne()
    elif val == 2:
        drawTwo()
    elif val == 3:
        drawThree()
    elif val == 4:
        drawFour()
    elif val == 5:
        drawFive()
    elif val == 6:
        drawSix()
    elif val == 7:
        drawSeven()
    elif val == 8:
        drawEight()
    elif val == 9:
        drawNine()
    else:
        pass
    home()
    up()
    back(67*4)
    lt(90)
    fd(67*4)
    rt(90)

def drawZero():
    circle(40)

def drawOne():
    down()
    pensize(3)
    back(22)
    rt(40)
    fd(18)
    back(18)
    lt(40)
    fd(45)
    rt(90)
    fd(15)
    back(30)
    up()
    pensize(1)

def drawTwo():
    pensize(3)
    lt(90)
    bk(18)
    rt(90)
    bk(10)
    down()
    circle(14,-180)
    rt(185)
    fd(2)
    rt(5)
    fd(2)
    rt(5)
    fd(2)
    rt(5)
    fd(1)
    rt(5)
    fd(1)
    rt(5)
    rt(5)
    rt(5)
    rt(5)
    fd(1)
    rt(5)
    fd(1)
    rt(5)
    fd(20)
    lt(5)
    fd(3)
    lt(5)
    fd(3)
    lt(5)
    fd(3)
    lt(5)
    fd(3)
    lt(5)
    fd(3)
    rt(60)
    bk(33)
    up()
    pensize(1)

def drawThree():
    down()
    rt(90)
    pensize(3)
    circle(12,-180)
    bk(12)
    fd(12)
    circle(12,180)
    lt(180)
    circle(12,180)
    fd(8)
    up()
    pensize(1)

def drawFour():
    down()
    pensize(3)
    lt(90)
    bk(13)
    left(77)
    fd(25)
    bk(25)
    rt(77)
    fd(33)
    lt(90)
    fd(23)
    bk(50)
    up()
    pensize(1)

def drawFive():
    bk(6)
    rt(90)
    down()
    pensize(3)
    bk(5)
    circle(15,-180)
    bk(17)
    fd(17)
    circle(15,180)
    fd(15)
    rt(90)
    fd(20)
    rt(90)
    fd(30)
    up()
    pensize(1)

def drawSix():
    pensize(3)
    right(90)
    down()
    fd(8)
    bk(8)
    circle(11,-280)
    bk(15)
    lt(-5)
    bk(5)
    lt(-5)
    bk(5)
    lt(-5)
    bk(5)
    lt(-5)
    bk(3)
    up()
    pensize(1)

def drawSeven():
    pensize(3)
    fd(25)
    rt(90)
    fd(5)
    rt(120)
    down()
    fd(45)
    left(30)
    fd(10)
    lt(90)
    fd(30)
    lt(90)
    fd(10)
    up()
    pensize(1)

def drawEight():
    down()
    rt(90)
    bk(4)
    pensize(3)
    circle(12,-180)
    bk(8)
    circle(12,-180)
    bk(8)
    lt(180)
    circle(12,180)
    fd(8)
    circle(12,180)
    fd(8)
    up()
    pensize(1)

def drawNine():
    rt(180)
    pensize(3)
    right(90)
    down()
    fd(8)
    bk(8)
    circle(11,-280)
    bk(15)
    lt(-5)
    bk(5)
    lt(-5)
    bk(5)
    lt(-5)
    bk(5)
    lt(-5)
    bk(3)
    up()
    pensize(1)

def algorithm(board):
    board = examineRows(board)
    board = examineCols(board)
    board = examineSections(board,0,0)
    board = examineSections(board,0,3)
    board = examineSections(board,0,6)
    board = examineSections(board,3,0)
    board = examineSections(board,3,3)
    board = examineSections(board,3,6)
    board = examineSections(board,6,0)
    board = examineSections(board,6,3)
    board = examineSections(board,6,6)
    board = checkForLen(board)
    return board

def examineRows(board):
    for row in board:
        removeVal = []
        singleVal = []
        for number in row:
            if number.value != " ":
                removeVal.append(number.value)
        for number in row:
            for el in removeVal:
                try:
                    number.possibleVals.remove(el)
                    print("Remove " + str(el) + " from " + str(number.getX()) + str(number.getY()))
                except ValueError:
                    pass
            for el in number.possibleVals:
                singleVal.append(el)
        c = 1
        while c < 10:
            if singleVal.count(c) == 1:
                for number in row:
                    try:
                        number.possibleVals.remove(c)
                        number.value = c
                    except ValueError:
                        pass
            c = c + 1
    return board

def examineCols(board):
    i = 0
    while i < 9:
        t = 0
        removeVal = []
        singleVal = []
        while t < 9:
            if board[t][i].value != " ":
                removeVal.append(board[t][i].value)
            t = t + 1
        t = 0
        while t < 9:
            for el in removeVal:
                try:
                    board[t][i].possibleVals.remove(el)
                    print("Remove " + str(el) + " from " + str(board[t][i].getX()) + str(board[t][i].getY()))
                except ValueError:
                    pass
            for el in board[t][i].possibleVals:
                singleVal.append(el)
            t = t + 1
        c = 1
        while c < 10:
            if singleVal.count(c) == 1:
                t = 0
                while t < 9:
                    try:
                        board[t][i].possibleVals.remove(c)
                        board[t][i].value = c
                    except ValueError:
                        pass
                    t = t + 1
            c = c + 1
        i = i + 1
    return board

def examineSections(board,x,y):
    xstart = x
    ystart = y
    i = 0
    removeVal = []
    singleVal = []
    while i < 3:
        t = 0
        y = ystart
        while t < 3:
            if board[y][x].value != " ":
                removeVal.append(board[y][x].value)
            y = y + 1
            t = t + 1
        x = x + 1
        i = i + 1
    x = xstart
    y = ystart
    i = 0
    while i < 3:
        t = 0
        y = ystart
        while t < 3:
            for el in removeVal:
                try:
                    board[y][x].possibleVals.remove(el)
                    print("Remove " + str(el) + " from " + str(board[y][x].getX()) + str(board[y][x].getY()))
                except ValueError:
                    pass
            for el in board[y][x].possibleVals:
                singleVal.append(el)
            y = y + 1
            t = t + 1
        x = x + 1
        i = i + 1
    c = 1
    while c < 10:
        if singleVal.count(c) == 1:
            x = xstart
            y = ystart
            i = 0
            while i < 3:
                t = 0
                y = ystart
                while t < 3:
                    try:
                        board[y][x].possibleVals.remove(c)
                        board[y][x].value = c
                    except ValueError:
                        pass
                    y = y + 1
                    t = t + 1
                x = x + 1
                i = i + 1
        c = c + 1

    #Pointing Pairs
    """
    i = 1
    possiblesRows = dict()
    while i < 10:
        possiblesRows[i] = []
        i = i + 1
    i = 0
    while i < 3:
        t = 0
        y = ystart
        while t < 3:
            if board[y][x].value == " ":
                for el in board[y][x].possibleVals:
                    possiblesRows[el].append(y)
            y = y + 1
            t = t + 1
        x = x + 1
        i = i + 1
    x = xstart
    y = ystart
    """
    return board

def checkForLen(board):
    for row in board:
        for number in row:
            if len(number.possibleVals) == 1:
                if number.value == " ":
                    number.value = number.possibleVals.pop()
                    print("Value is",number.value,"at",number.getX(),number.getY())
                else:
                    number.possibleVals.pop()
            if number.value != " ":
                number.possibleVals = []
    return board

def pointingPairs(board):
    pass

def isDone(board):
    for row in board:
        for number in row:
            if number.value == " ":
                return False
    return True

def printPossible(board):
    for row in board:
        for number in row:
            print(str(number.value),number.possibleVals,number.getX(),number.getY())

def inputPuzzle(board):
    section = input()
    while section != '':
        if section == '1':
            drawSectionBorder(section,"red")
            board = sectionSelection(section,board)
        elif section == '2':
            drawSectionBorder(section,"red")
            board = sectionSelection(section,board)
        elif section == '3':
            drawSectionBorder(section,"red")
            board = sectionSelection(section,board)
        elif section == '4':
            drawSectionBorder(section,"red")
            board = sectionSelection(section,board)
        elif section == '5':
            drawSectionBorder(section,"red")
            board = sectionSelection(section,board)
        elif section == '6':
            drawSectionBorder(section,"red")
            board = sectionSelection(section,board)
        elif section == '7':
            drawSectionBorder(section,"red")
            board = sectionSelection(section,board)
        elif section == '8':
            drawSectionBorder(section,"red")
            board = sectionSelection(section,board)
        elif section == '9':
            drawSectionBorder(section,"red")
            board = sectionSelection(section,board)
        else:
            print("Invalid input.")
        home()
        back(4*67)
        lt(90)
        fd(4*67)
        rt(90)
        try:
            if int(section) < 10 and int(section) > 0:
                drawSectionBorder(section,"black")
        except ValueError:
            pass
        home()
        back(4*67)
        lt(90)
        fd(4*67)
        rt(90)
        drawGivens(board)
        section = input()
    return board

def drawSectionBorder(section,color):
    fd(67)
    rt(90)
    fd(67)
    lt(90)
    if section == '1':
        rt(90)
        fd(6*67)
        drawBorder(color)
    elif section == '2':
        rt(90)
        fd(6*67)
        lt(90)
        fd(3*67)
        rt(90)
        drawBorder(color)
    elif section == '3':
        rt(90)
        fd(6*67)
        lt(90)
        fd(6*67)
        rt(90)
        drawBorder(color)
    elif section == '4':
        rt(90)
        fd(3*67)
        drawBorder(color)
    elif section == '5':
        rt(90)
        fd(3*67)
        lt(90)
        fd(3*67)
        rt(90)
        drawBorder(color)
    elif section == '6':
        rt(90)
        fd(3*67)
        lt(90)
        fd(6*67)
        rt(90)
        drawBorder(color)
    elif section == '7':
        rt(90)
        drawBorder(color)
    elif section == '8':
        fd(3*67)
        rt(90)
        drawBorder(color)
    elif section == '9':
        fd(6*67)
        rt(90)
        drawBorder(color)

def drawBorder(color):
    fd(3*67/2)
    rt(90)
    pencolor(color)
    down()
    fd(3*67/2)
    rt(90)
    fd(3*67)
    rt(90)
    fd(3*67)
    rt(90)
    fd(3*67)
    rt(90)
    fd(3*67/2)
    lt(90)
    up()
    bk(3*67/2)
    pencolor("black")

def sectionSelection(sect,board):
    section = input()
    while section != '':
        if section == '1':
            drawSmallSectionBorder(section,"red")
            board = makeNumber(input(),board,sect,section)
            home()
            back(4*67)
            lt(90)
            fd(4*67)
            rt(90)
            drawSectionBorder(sect,"black")
            drawSmallSectionBorder(section,"black")
            return board
        elif section == '2':
            drawSmallSectionBorder(section,"red")
            board = makeNumber(input(),board,sect,section)
            home()
            back(4*67)
            lt(90)
            fd(4*67)
            rt(90)
            drawSectionBorder(sect,"black")
            drawSmallSectionBorder(section,"black")
            return board
        elif section == '3':
            drawSmallSectionBorder(section,"red")
            board = makeNumber(input(),board,sect,section)
            home()
            back(4*67)
            lt(90)
            fd(4*67)
            rt(90)
            drawSectionBorder(sect,"black")
            drawSmallSectionBorder(section,"black")
            return board
        elif section == '4':
            drawSmallSectionBorder(section,"red")
            board = makeNumber(input(),board,sect,section)
            home()
            back(4*67)
            lt(90)
            fd(4*67)
            rt(90)
            drawSectionBorder(sect,"black")
            drawSmallSectionBorder(section,"black")
            return board
        elif section == '5':
            drawSmallSectionBorder(section,"red")
            board = makeNumber(input(),board,sect,section)
            home()
            back(4*67)
            lt(90)
            fd(4*67)
            rt(90)
            drawSectionBorder(sect,"black")
            drawSmallSectionBorder(section,"black")
            return board
        elif section == '6':
            drawSmallSectionBorder(section,"red")
            board = makeNumber(input(),board,sect,section)
            home()
            back(4*67)
            lt(90)
            fd(4*67)
            rt(90)
            drawSectionBorder(sect,"black")
            drawSmallSectionBorder(section,"black")
            return board
        elif section == '7':
            drawSmallSectionBorder(section,"red")
            board = makeNumber(input(),board,sect,section)
            home()
            back(4*67)
            lt(90)
            fd(4*67)
            rt(90)
            drawSectionBorder(sect,"black")
            drawSmallSectionBorder(section,"black")
            return board
        elif section == '8':
            drawSmallSectionBorder(section,"red")
            board = makeNumber(input(),board,sect,section)
            home()
            back(4*67)
            lt(90)
            fd(4*67)
            rt(90)
            drawSectionBorder(sect,"black")
            drawSmallSectionBorder(section,"black")
            return board
        elif section == '9':
            drawSmallSectionBorder(section,"red")
            board = makeNumber(input(),board,sect,section)
            home()
            back(4*67)
            lt(90)
            fd(4*67)
            rt(90)
            drawSectionBorder(sect,"black")
            drawSmallSectionBorder(section,"black")
            return board
        else:
            print("Invalid input.")
        section = input()
    return board

def makeNumber(number,board,sect,section):
    if number == '':
        return board
    try:
        int(number)
    except ValueError:
        if number != " ":
            number = input("Invalid input.")
            return board
    coor = getXY(sect,section)
    if board[coor.getX()][coor.getY()].value != " ":
        pencolor("white")
        val = board[coor.getX()][coor.getY()].value
        rt(90)
        if val == 1:
            drawOne()
        elif val == 2:
            drawTwo()
        elif val == 3:
            drawThree()
        elif val == 4:
            drawFour()
        elif val == 5:
            drawFive()
        elif val == 6:
            drawSix()
        elif val == 7:
            drawSeven()
        elif val == 8:
            drawEight()
        elif val == 9:
            drawNine()
        else:
            pass
    if number == " ":
        board[coor.getX()][coor.getY()].possibleVals =[1,2,3,4,5,6,7,8,9]
    else:
        board[coor.getX()][coor.getY()].possibleVals =[]
    if number == " ":
        board[coor.getX()][coor.getY()].value = number
    else:
        board[coor.getX()][coor.getY()].value = int(number)
    board[coor.getX()][coor.getY()].isDrawn = False
    return board

def getXY(sect,minisection):
    if sect == '1':
        if minisection == '1':
            return Coordinate(8,0)
        elif minisection == '2':
            return Coordinate(8,1)
        elif minisection == '3':
            return Coordinate(8,2)
        elif minisection == '4':
            return Coordinate(7,0)
        elif minisection == '5':
            return Coordinate(7,1)
        elif minisection == '6':
            return Coordinate(7,2)
        elif minisection == '7':
            return Coordinate(6,0)
        elif minisection == '8':
            return Coordinate(6,1)
        elif minisection == '9':
            return Coordinate(6,2)
        else:
            raise ValueError
    elif sect == '2':
        if minisection == '1':
            return Coordinate(8,3)
        elif minisection == '2':
            return Coordinate(8,4)
        elif minisection == '3':
            return Coordinate(8,5)
        elif minisection == '4':
            return Coordinate(7,3)
        elif minisection == '5':
            return Coordinate(7,4)
        elif minisection == '6':
            return Coordinate(7,5)
        elif minisection == '7':
            return Coordinate(6,3)
        elif minisection == '8':
            return Coordinate(6,4)
        elif minisection == '9':
            return Coordinate(6,5)
        else:
            raise ValueError
    elif sect == '3':
        if minisection == '1':
            return Coordinate(8,6)
        elif minisection == '2':
            return Coordinate(8,7)
        elif minisection == '3':
            return Coordinate(8,8)
        elif minisection == '4':
            return Coordinate(7,6)
        elif minisection == '5':
            return Coordinate(7,7)
        elif minisection == '6':
            return Coordinate(7,8)
        elif minisection == '7':
            return Coordinate(6,6)
        elif minisection == '8':
            return Coordinate(6,7)
        elif minisection == '9':
            return Coordinate(6,8)
        else:
            raise ValueError
    elif sect == '4':
        if minisection == '1':
            return Coordinate(5,0)
        elif minisection == '2':
            return Coordinate(5,1)
        elif minisection == '3':
            return Coordinate(5,2)
        elif minisection == '4':
            return Coordinate(4,0)
        elif minisection == '5':
            return Coordinate(4,1)
        elif minisection == '6':
            return Coordinate(4,2)
        elif minisection == '7':
            return Coordinate(3,0)
        elif minisection == '8':
            return Coordinate(3,1)
        elif minisection == '9':
            return Coordinate(3,2)
        else:
            raise ValueError
    elif sect == '5':
        if minisection == '1':
            return Coordinate(5,3)
        elif minisection == '2':
            return Coordinate(5,4)
        elif minisection == '3':
            return Coordinate(5,5)
        elif minisection == '4':
            return Coordinate(4,3)
        elif minisection == '5':
            return Coordinate(4,4)
        elif minisection == '6':
            return Coordinate(4,5)
        elif minisection == '7':
            return Coordinate(3,3)
        elif minisection == '8':
            return Coordinate(3,4)
        elif minisection == '9':
            return Coordinate(3,5)
        else:
            raise ValueError
    elif sect == '6':
        if minisection == '1':
            return Coordinate(5,6)
        elif minisection == '2':
            return Coordinate(5,7)
        elif minisection == '3':
            return Coordinate(5,8)
        elif minisection == '4':
            return Coordinate(4,6)
        elif minisection == '5':
            return Coordinate(4,7)
        elif minisection == '6':
            return Coordinate(4,8)
        elif minisection == '7':
            return Coordinate(3,6)
        elif minisection == '8':
            return Coordinate(3,7)
        elif minisection == '9':
            return Coordinate(3,8)
        else:
            raise ValueError
    elif sect == '7':
        if minisection == '1':
            return Coordinate(2,0)
        elif minisection == '2':
            return Coordinate(2,1)
        elif minisection == '3':
            return Coordinate(2,2)
        elif minisection == '4':
            return Coordinate(1,0)
        elif minisection == '5':
            return Coordinate(1,1)
        elif minisection == '6':
            return Coordinate(1,2)
        elif minisection == '7':
            return Coordinate(0,0)
        elif minisection == '8':
            return Coordinate(0,1)
        elif minisection == '9':
            return Coordinate(0,2)
        else:
            raise ValueError
    elif sect == '8':
        if minisection == '1':
            return Coordinate(2,3)
        elif minisection == '2':
            return Coordinate(2,4)
        elif minisection == '3':
            return Coordinate(2,5)
        elif minisection == '4':
            return Coordinate(1,3)
        elif minisection == '5':
            return Coordinate(1,4)
        elif minisection == '6':
            return Coordinate(1,5)
        elif minisection == '7':
            return Coordinate(0,3)
        elif minisection == '8':
            return Coordinate(0,4)
        elif minisection == '9':
            return Coordinate(0,5)
        else:
            raise ValueError
    elif sect == '9':
        if minisection == '1':
            return Coordinate(2,6)
        elif minisection == '2':
            return Coordinate(2,7)
        elif minisection == '3':
            return Coordinate(2,8)
        elif minisection == '4':
            return Coordinate(1,6)
        elif minisection == '5':
            return Coordinate(1,7)
        elif minisection == '6':
            return Coordinate(1,8)
        elif minisection == '7':
            return Coordinate(0,6)
        elif minisection == '8':
            return Coordinate(0,7)
        elif minisection == '9':
            return Coordinate(0,8)
        else:
            raise ValueError


def drawSmallSectionBorder(section,color):
    lt(90)
    if section == '1':
        bk(67)
        rt(90)
        fd(67)
        lt(90)
        drawSmallBorder(color)
    elif section == '2':
        rt(90)
        fd(67)
        lt(90)
        drawSmallBorder(color)
    elif section == '3':
        fd(67)
        rt(90)
        fd(67)
        lt(90)
        drawSmallBorder(color)
    elif section == '4':
        bk(67)
        drawSmallBorder(color)
    elif section == '5':
        drawSmallBorder(color)
    elif section == '6':
        fd(67)
        drawSmallBorder(color)
    elif section == '7':
        bk(67)
        lt(90)
        fd(67)
        rt(90)
        drawSmallBorder(color)
    elif section == '8':
        lt(90)
        fd(67)
        rt(90)
        drawSmallBorder(color)
    elif section == '9':
        fd(67)
        lt(90)
        fd(67)
        rt(90)
        drawSmallBorder(color)

def drawSmallBorder(color):
    fd(67/2)
    rt(90)
    pencolor(color)
    down()
    fd(67/2)
    rt(90)
    fd(67)
    rt(90)
    fd(67)
    rt(90)
    fd(67)
    rt(90)
    fd(67/2)
    lt(90)
    up()
    bk(67/2)
    pencolor("black")

def saveBoard(board):
    name = input("Name: ")
    count = 0
    if name == '':
        for file in open("/puzzles"):
            count = count + 1
        name = str(count)+".txt"
    file = open("puzzles/"+name,'w')
    for row in board:
        for number in row:
            if number.value != " ":
                file.write("("+str(number.getY())+","+str(number.getX())+") "+str(number.value)+"\n")


def main():
    input("Solve Puzzle?")
    board = fillInBoard(boardInit())
    input("Board created.")
    drawBoard()
    drawGivens(board)
    board = inputPuzzle(board)
    if input("Board drawn.")  == "save":
        saveBoard(board)
    count = 0
    while isDone(board) == False:
        print(count)
        #if input("Loop algorithm.") == 'print':
        #    printPossible(board)
        board = algorithm(board)
        drawGivens(board)
        count = count + 1
        if count > 2000:
            if input("Puzzle not solvable") != "done":
                board = inputPuzzle(board)
                count = 0
            else:
                break
    input("Algorithm completed in "+str(count)+" loops.")



main()
