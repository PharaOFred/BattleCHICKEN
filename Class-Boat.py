class Grid:                         #This class is to set the game's grid, which will be 10x10


    def __init__(self):             #Constructor operator

        grid = ["water"]*100        #Our grid's - 10x10 -  i.e a list of 100 elements (tiles) "filled" with a string "water".
        self.grid = grid

    def __getitem__(self, item):    #Reading operator

        return self.grid[item]      #Returns the item at the selected tile this, it is of my
                                    #concern that this operator should take a tuple for argument
                                    # as in i,j = item, where the argument would be (i,j)

    def __setitem__(self, key, value):  # Writing operator

        self.grid[key] = value          #This will set a new string to the targeted position, could be "Aaar, how dare "
                                        # ye landlubbers hit my ship!" or "Arrr, ye missed ye scallywag!" or "To Davy Jones wit' ye!"



class Tile:                             # Class

    def __init__(self,m,n,gridtile):    #Constructor for the line position m, the column position n and the grid's tile

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

#Integrated test


Grille = Grid()

print (Grille.grid)
