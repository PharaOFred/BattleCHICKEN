class Grid():

    def __init__(self):

        grid = ["water"]*100

        self.grid = grid
    def __item__(self,key):

        return self.grille[key]
    def __setitem__(self, key, value):

        if key < 0 or key >= 100:
            raise ValueError()

        self.grille[key]=value

class Tile(Grid):

    def __init__(self,m,n):

        self.m = m
        self.n = n
        super(Tile,self).__init__()

    def GetValue(self):

        return self.grid[(10*self.m-1)+self.n]

    def SetValue(self,value):

        self.grid[(10*self.m-1)+self.n] = value

class Ship(Tile):

    def __init__(self,lenght):

        self.lenght = lenght


A = Grid()

for i in A:

    print (i)
