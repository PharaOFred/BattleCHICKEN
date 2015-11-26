
import turtle           # This imports the module turtle from TK.
turtle.tracer(0, 0)

class Grid:              #This class is to set the player's grid, which will be 10x10


    def __init__(self): #Constructor operator

        grid = ["water"]*100 #Our grid's - 10x10 -  i.e a list of 100 elements (tiles) "filled" with a string "water".
        self.grid = grid

    def __getitem__(self, item):#Reading operator

        return self.grid[item]  #Returns the item at the selected tile this, it is of my
                                    #concern that this operator should take a tuple for argument
                                    # as in i,j = item, where the argument would be (i,j)

    def __setitem__(self, key, value):# Writing operator

        self.grid[key] = value# This will set a new string to the targeted position, could be "Aaar, how dare
                 # ye landlubbers hit my ship!" or "Arrr, ye missed ye scallywag!" or "To Davy Jones wit' ye!"


class GridEnnemy:       #This class is to set the enemy's grid, which will be 10x10


    def __init__(self):#Constructor operator

        grid = ["unknown"]*100 #Grid 10x10 with every elements set as "unknown water"
        self.grid = grid

    def __getitem__(self, item): #Reading operator, which return the item selected by the argument item.

        return self.grid[item]

    def __setitem__(self, key, value): #Writing operator which sets a value to the targeted(key) area

        self.grid[key] = value

class Tile:                         #Class will be used to set ships on tiles player's grid and either set
                                        #"unknown","water" or "enemy hit" on enemy's grid.


    def __init__(self,m,n,gridtile):

        self.m = m                      #Line position of "grid"
        self.n = n                      #Column position of "grid"
        self.gridtile = gridtile        #This tells to which grid (the opponent's or the player's) belongs to.

    def getvalue(self):                                 # Returns the value at the coordinate (m,n), because this is a
                                                        # list of 100 elements and not 10 lists of 10 elements
        return self.gridtile[(10*(self.m-1))+(self.n-1)]# we multiply m by 10 to get the appropriate line and only add the column
                                                        # the minus 1 on both m and n is to avoid having to call
                                                        #line 0 instead of line 1 am a bit concerned about the uselessness of
                                                        # __getitem__ in class Grid().


    def setValue(self,value):                           # Set the a value in the list coordinate (m,n)

        self.gridtile[(10*(self.m-1))+(self.n-1)] = value



class Boat:                                 #The class to build our ships!

    def __init__(self,lenght):              #Constructor, we set the lenght of our ships.

        self.lenght = lenght                # From within a range of 2 to 5 tiles.


    def placeH(self,init_line,init_col,gridboat1):      #This function calls on the class Tile and it's function
                                                        # SetValue to set the ship's coordinate on the grid
        if 11-self.lenght >= init_col:                  # horizontally.

            for i in range(self.lenght):

                init_tile = Tile(init_line,init_col+i,gridboat1)
                init_tile.SetValue("boat")

        else:

            print("ERREUR, MAUVAIS ENDROIT POUR LA LONGUEUR DU BATEAU") # if boat is placed outside the
                                                                        # grid's range, raises this error


    def placeV(self,init_line,init_col,gridboat1):      # Same as placeH but places the ship vertically.

        if 11-self.lenght >= init_line:

            for i in range(self.lenght):

                init_tile = Tile(init_line+i,init_col,gridboat1)
                init_tile.SetValue("boat")


        else:

            print("ERREUR, MAUVAIS ENDROIT POUR LA LONGUEUR DU BATEAU") # if boat placed outside allowed
                                                                        # range, raise and error


hauteur = 600
largeur = 800

largeur_grille = largeur/2 * 0.8
largeur_poly = largeur_grille * 1/20

def gotoMidRG():

    alex.penup()
    alex.goto(largeur/4,4/5 * hauteur/2 - hauteur/2)
    alex.pendown()

def gotoMidLG():

    alex.penup()
    alex.goto(-largeur/4,4/5 * hauteur/2 - hauteur/2)
    alex.pendown()

def gotoCornerLG():

    gotoMidLG()
    alex.penup()
    alex.left(90)
    alex.forward(largeur_grille/2)
    alex.left(90)
    alex.forward(largeur_grille/2)
    alex.left(90)

def gotoCornerRG():

    gotoMidRG()
    alex.penup()
    alex.left(90)
    alex.forward(largeur_grille/2)
    alex.left(90)
    alex.forward(largeur_grille/2)
    alex.left(90)

def gotoStartLG():

    alex.penup()
    gotoCornerLG()
    alex.forward(largeur_grille/20)
    alex.left(90)
    alex.forward(largeur_grille/20)

def gotoStartRG():

    alex.penup()
    gotoCornerRG()
    alex.forward(largeur_grille/20)
    alex.left(90)
    alex.forward(largeur_grille/20)

def makeRGridData(grid):

    gotoStartRG()

    for i in range(100):

        if grid[i] == "water":
            alex.color("#00ccff")
            alex.stamp()
        elif grid[i] == "boat":
            alex.color("red")
            alex.stamp()
        elif grid[i] == "unknown":
            alex.color("#f84b08")
            alex.stamp()
        if (i+1) % 10 == 0:
            alex.penup()
            alex.setheading(270)
            alex.forward(largeur_grille/10)
            alex.setheading(180)
            alex.forward(largeur_grille/10 *9)
            alex.setheading(0)
        else:
            alex.forward(largeur_grille/10)
    makeBlackGrid()

def makeLGridData(grid):

    gotoStartLG()

    for i in range(100):

        if grid[i] == "water":

            alex.color("#00ccff")
            alex.stamp()

        elif grid[i] == "boat":

            alex.color("#ccffff")
            alex.stamp()

        elif grid[i] == "unknown":

            alex.color("#e60000")
            alex.stamp()

        if (i+1) % 10 == 0:

            alex.penup()
            alex.setheading(270)
            alex.forward(largeur_grille/10)
            alex.setheading(180)
            alex.forward(largeur_grille/10 *9)
            alex.setheading(0)

        else:

            alex.forward(largeur_grille/10)
    makeBlackGrid()

def makeBlackGrid():

    alex.pencolor("black")
    alex.penup()
    alex.goto(0,-hauteur/2)
    alex.pendown()
    alex.goto(0,hauteur/2 - hauteur/5)
    alex.goto(-largeur/2,hauteur/2 - hauteur/5)
    alex.goto(largeur/2,hauteur/2 - hauteur/5)

    gotoMidRG()

    alex.left(90)
    alex.forward(largeur_grille/2)
    alex.left(90)
    alex.forward(largeur_grille/2)
    alex.left(90)



    for x in range(5):

        alex.forward(largeur_grille)
        alex.left(90)
        alex.forward(largeur_grille/10)
        alex.left(90)
        alex.forward(largeur_grille)
        alex.right(90)
        alex.forward(largeur_grille/10)
        alex.right(90)
    alex.forward(largeur_grille)
    alex.right(90)

    for x in range(5):

        alex.forward(largeur_grille)
        alex.right(90)
        alex.forward(largeur_grille/10)
        alex.right(90)
        alex.forward(largeur_grille)
        alex.left(90)
        alex.forward(largeur_grille/10)
        alex.left(90)
    alex.forward(largeur_grille/2)

    gotoMidLG()

    alex.left(90)
    alex.forward(largeur_grille/2)
    alex.left(90)
    alex.forward(largeur_grille/2)
    alex.left(90)



    for x in range(5):

        alex.forward(largeur_grille)
        alex.left(90)
        alex.forward(largeur_grille/10)
        alex.left(90)
        alex.forward(largeur_grille)
        alex.right(90)
        alex.forward(largeur_grille/10)
        alex.right(90)
    alex.forward(largeur_grille)
    alex.right(90)

    for x in range(5):

        alex.forward(largeur_grille)
        alex.right(90)
        alex.forward(largeur_grille/10)
        alex.right(90)
        alex.forward(largeur_grille)
        alex.left(90)
        alex.forward(largeur_grille/10)
        alex.left(90)
    alex.forward(largeur_grille/2)


fen = turtle.Screen()
fen.setup(width=largeur, height=hauteur)
alex = turtle.Turtle()

text = turtle.Turtle()
text.penup()
text.color("#00ccff")
text.setheading(90)
text.forward(220)

ally = turtle.Turtle()
ally.penup()
ally.color("#00ccff") #f84b08
ally.setheading(90)
ally.forward(105)
ally.left(90)
ally.forward(207)

ennemy = turtle.Turtle()
ennemy.penup()
ennemy.color("#f84b08")
ennemy.setheading(90)
ennemy.forward(105)
ennemy.right(90)
ennemy.forward(200)



poly = ((largeur_poly,largeur_poly),(-largeur_poly,largeur_poly),(-largeur_poly,-largeur_poly),(largeur_poly,-largeur_poly))
turtle.addshape('square',poly)
alex.shape('square')
alex.color('blue')
alex.pencolor('black')

alex.penup()
alex.goto(0,-hauteur/2)
alex.pendown()
alex.goto(0,hauteur/2 - hauteur/5)
alex.goto(-largeur/2,hauteur/2 - hauteur/5)
alex.goto(largeur/2,hauteur/2 - hauteur/5)

gotoMidRG()

alex.left(90)
alex.forward(largeur_grille/2)
alex.left(90)
alex.forward(largeur_grille/2)
alex.left(90)



for x in range(5):

    alex.forward(largeur_grille)
    alex.left(90)
    alex.forward(largeur_grille/10)
    alex.left(90)
    alex.forward(largeur_grille)
    alex.right(90)
    alex.forward(largeur_grille/10)
    alex.right(90)
alex.forward(largeur_grille)
alex.right(90)

for x in range(5):

    alex.forward(largeur_grille)
    alex.right(90)
    alex.forward(largeur_grille/10)
    alex.right(90)
    alex.forward(largeur_grille)
    alex.left(90)
    alex.forward(largeur_grille/10)
    alex.left(90)
alex.forward(largeur_grille/2)

gotoMidLG()

largeur_grille = largeur/2 * 0.8

alex.left(90)
alex.forward(largeur_grille/2)
alex.left(90)
alex.forward(largeur_grille/2)
alex.left(90)

for x in range(5):

    alex.forward(largeur_grille)
    alex.left(90)
    alex.forward(largeur_grille/10)
    alex.left(90)
    alex.forward(largeur_grille)
    alex.right(90)
    alex.forward(largeur_grille/10)
    alex.right(90)
alex.forward(largeur_grille)
alex.right(90)

for x in range(5):

    alex.forward(largeur_grille)
    alex.right(90)
    alex.forward(largeur_grille/10)
    alex.right(90)
    alex.forward(largeur_grille)
    alex.left(90)
    alex.forward(largeur_grille/10)
    alex.left(90)
alex.forward(largeur_grille/2)


fen.bgcolor("black")


leftgrid = Grid()
rightgrid = GridEnnemy()

makeLGridData(leftgrid)
makeRGridData(rightgrid)
alex.hideturtle()
text.hideturtle()

def gotoClick(x,y):
    print(x,y)

def getlgindex(x,y):
    if 100 > y > 68:
        line = 1
    elif 68 > y > 36:
        line = 2
    elif 36 > y > 4:
        line = 3
    elif 4 > y > -28:
        line = 4
    elif -28 > y > -60:
        line = 5
    elif -60 > y > -92:
        line = 6
    elif -92 > y > -124:
        line = 7
    elif -124 > y > -156:
        line = 8
    elif -156 > y > -188:
        line = 9
    elif -188 > y > -220:
        line = 10
    else:
        line = -1000
    for i in range(10):
        if (-0.9 * largeur/2 + (i+1) * largeur_grille/10) > x >= (-0.9 * largeur/2 + i * largeur_grille/10):
            column = (i+1)
        elif x == -1000:
            line = x
    return(line,column)

def getRgindex(x,y):
    if 100 > y > 68:
        line = 1
    elif 68 > y > 36:
        line = 2
    elif 36 > y > 4:
        line = 3
    elif 4 > y > -28:
        line = 4
    elif -28 > y > -60:
        line = 5
    elif -60 > y > -92:
        line = 6
    elif -92 > y > -124:
        line = 7
    elif -124 > y > -156:
        line = 8
    elif -156 > y > -188:
        line = 9
    elif -188 > y > -220:
        line = 10
    for i in range(10):
        if (0.1 * largeur/2 + (i) * largeur_grille/10) < x <= (0.1 * largeur/2 + (1+i) * largeur_grille/10):
            column = (i+1)
    print(line,column)
    return (line,column)

def placeBoat5H(x,y):

    coord = getlgindex(x,y)

    rep = (coord[0],coord[1])

    print(rep)

    boat5 = Boat(5)

    boat5.placeboat_horizontaly(coord[0],coord[1],leftgrid)

    makeLGridData(leftgrid)
    makeBlackGrid()



def placeBoat5V(x,y):


    coord = getlgindex(x,y)

    rep = (coord[0],coord[1])

    print(rep)

    boat5 = Boat(5)

    boat5.placeboat_verticaly(coord[0],coord[1],leftgrid)

    makeLGridData(leftgrid)
    makeBlackGrid()

def placeBoat4H(x,y):

    coord = getlgindex(x,y)

    rep = (coord[0],coord[1])

    print(rep)

    boat4 = Boat(4)

    boat4.placeboat_horizontaly(coord[0],coord[1],leftgrid)

    makeLGridData(leftgrid)
    makeBlackGrid()

def placeBoat4V(x,y):

    coord = getlgindex(x,y)

    rep = (coord[0],coord[1])

    print(rep)

    boat4 = Boat(4)

    boat4.placeboat_verticaly(coord[0],coord[1],leftgrid)

    makeLGridData(leftgrid)
    makeBlackGrid()

def placeBoat3V(x,y):

    coord = getlgindex(x,y)

    rep = (coord[0],coord[1])

    print(rep)

    boat3 = Boat(3)

    boat3.placeboat_verticaly(coord[0],coord[1],leftgrid)

    makeLGridData(leftgrid)
    makeBlackGrid()

def placeBoat3H(x,y):

    coord = getlgindex(x,y)

    rep = (coord[0],coord[1])

    print(rep)

    boat3 = Boat(3)

    boat3.placeboat_horizontaly(coord[0],coord[1],leftgrid)

    makeLGridData(leftgrid)
    makeBlackGrid()

def placeBoat2H(x,y):

    coord = getlgindex(x,y)

    rep = (coord[0],coord[1])

    print(rep)

    boat2 = Boat(2)

    boat2.placeboat_horizontaly(coord[0],coord[1],leftgrid)

    makeLGridData(leftgrid)
    makeBlackGrid()

def placeBoat2V(x,y):

    coord = getlgindex(x,y)

    rep = (coord[0],coord[1])

    print(rep)

    boat2 = Boat(2)

    boat2.placeboat_verticaly(coord[0],coord[1],leftgrid)

    makeLGridData(leftgrid)
    makeBlackGrid()



def placeBoat5(x,y):

    direction = fen.textinput("Console","Choose the orientation of your boat : \n"
                                        "«h» for horizontal orientation\n"
                                        "«v» for vertical orientation")

    if direction == "h":
        placeBoat5H(x,y)

    elif direction == "v":

        placeBoat5V(x,y)
    else:
        texte=fen.textinput("Console","Accepted inputs are :\n"
                      "«h» for horizontal orientation\n"
                      "«v» for vertical orientation")
        if texte == "h":

            placeBoat5H(x,y)
        elif texte == "v":

            placeBoat5V(x,y)
        else:
            placeBoat5(x,y)

def placeBoat4(x,y):
    import time

    boat4 = Boat(4)

    direction = fen.textinput("Console","Choose the orientation of your boat : \n"
                                        "«h» for horizontal orientation\n"
                                        "«v» for vertical orientation")
    if direction == "h":

        placeBoat4H(x,y)
    elif direction == "v":

        placeBoat4V(x,y)
    else:
        texte=fen.textinput("Console","Accepted inputs are :\n"
                      "«h» for horizontal orientation\n"
                      "«v» for vertical orientation")
        if texte == "h":

            placeBoat4H(x,y)
        elif texte == "v":

            placeBoat4V(x,y)
        else:
            placeBoat4(x,y)

def placeBoat3(x,y):

    boat3 = Boat(3)

    direction = fen.textinput("Console","Choose the orientation of your boat : \n"
                                        "«h» for horizontal orientation\n"
                                        "«v» for vertical orientation")
    if direction == "h":

        placeBoat3H(x,y)
    elif direction == "v":

        placeBoat3V(x,y)
    else:
        texte=fen.textinput("Console","Accepted inputs are :\n"
                      "«h» for horizontal orientation\n"
                      "«v» for vertical orientation")
        if texte == "h":

            placeBoat3H(x,y)
        elif texte == "v":

            placeBoat3V(x,y)
        else:
            placeBoat3(x,y)

def placeBoat2(x,y):

    boat2 = Boat(2)

    direction = fen.textinput("Console","Choose the orientation of your boat : \n"
                                        "«h» for horizontal orientation\n"
                                        "«v» for vertical orientation")
    if direction == "h":

        placeBoat2H(x,y)
    elif direction == "v":

        placeBoat2V(x,y)
    else:
        texte=fen.textinput("Console","Accepted inputs are :\n"
                      "«h» for horizontal orientation\n"
                      "«v» for vertical orientation")
        if texte == "h":

            placeBoat2H(x,y)
        elif texte == "v":

            placeBoat2V(x,y)
        else:
            placeBoat2(x,y)


class placeBoat:
    def __init__(self):

        self.bot = 0


    def placerBateau(self,x,y):
        if self.bot == 0:
            text.clear()
            text.write("Boat length is 4 ; Choose an appropriate tile",False,align="center",font=("Arial",18,"normal"))
            placeBoat5(x,y)
            self.bot += 1
            print(self.bot)
        elif self.bot == 1:
            text.clear()
            placeBoat4(x,y)
            text.write("Boat length is 3 ; Choose an appropriate tile",False,align="center",font=("Arial",18,"normal"))
            self.bot += 1
        elif self.bot == 2:
            text.clear()
            placeBoat3(x,y)
            text.write("Boat length is 3 ; Choose an appropriate tile",False,align="center",font=("Arial",18,"normal"))
            self.bot += 1
        elif self.bot == 3:
            text.clear()
            placeBoat3(x,y)
            text.write("Boat length is 2 ; Choose an appropriate tile",False,align="center",font=("Arial",18,"normal"))
            self.bot += 1
        elif self.bot == 4:
            text.clear()
            placeBoat2(x,y)
            alex.screen.onclick(None)
            self.destroy()


def getpixel(x,y):
    print(x,y)


#fen.onscreenclick(getpixel,btn=1)
placebateau = placeBoat()
alex.screen.onclick(placebateau.placerBateau)









ennemy.write("Ground Dwelling Scum Ennemy's Grid",False,align="center",font=("Arial",14,"normal"))
ally.write("Supreme Emperor of the Sea's Grid",False,align="center",font=("Arial",14,"normal"))
text.write("Boat length is 5 ; Choose an appropriate tile",False,align="center",font=("Arial",18,"normal"))
alex.screen.mainloop()





















#here














makeRGridData(rightgrid)
makeLGridData(leftgrid)
makeBlackGrid()









turtle.update()
fen.mainloop()
