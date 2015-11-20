class Grid:

                   #This class is to set the game's grid, which will be 10x10
    def __init__(self):     #Constructor operator

        grid = ["water"]*100    #Our grid's -10x10- i.e a list of 100 elements (tiles)
        self.grid = grid        #"filled" with water.

    def __getitem__(self, item):    #Reading operator

        return self.grid[item]  #Returns the item at the selected tile this, it is of my
                                #concern that this operator should take a tuple for argument
                                # as in i,j = item, where the argument would be (i,j)

    def __setitem__(self, key, value):  # Writing operator

        self.grid[key] = value          #This will set a new string to the targeted position, could be "Aaar, how dare "
                                        # ye landlubbers hit my ship!" or "Arrr, ye missed ye scallywag!"



class Tile:                             #Huuuh this class was supposed to inherit from the Grid class...
                                        #to be continued...

    def __init__(self,m,n,gridtile):    #Constructor for the line position m, the column position n and the grid's tile

        self.m = m                      #Line position of "grid"
        self.n = n                      #column position of "grid"
        self.gridtile = gridtile        #No idea what's this for.


    def getvalue(self):                                 # Returns the value at the coordinate (m,n), because this is a
                                                        # list of 100 elements and not 10 lists of 10 elements
        return self.gridtile[(10*(self.m-1))+(self.n-1)]# we multiply m by 10 to get the appropriate line and only add the column
                                                        # the minus 1 on both m and n is to avoid having to call
                                                        #line 0 instead of line 1


    def setvalue(self,value):                               # Set the

        self.gridtile[(10*(self.m-1))+(self.n-1)] = value


class Boat:

    def __init__(self,lenght):

        self.lenght = lenght


    def PlaceH(self,init_line,init_col,gridboat1):

        if 11-self.lenght >= init_col:

            for i in range(self.lenght):

                init_tile = Tile(init_line,init_col+i,gridboat1)
                init_tile.setvalue("boat")

        else:

            print("ERREUR, MAUVAIS ENDROIT POUR LA LONGUEUR DU BATEAU")


    def PlaceV(self,init_line,init_col,gridboat1):

        if 11-self.lenght >= init_line:

            for i in range(self.lenght):

                init_tile = Tile(init_line+i,init_col,gridboat1)
                init_tile.setvalue("boat")


        else:

            print("ERREUR, MAUVAIS ENDROIT POUR LA LONGUEUR DU BATEAU")

#Integrated test

G = Grid()
Sous_marin = Boat(3)
