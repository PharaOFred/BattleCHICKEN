class Grid:
    def __init__(self):
        grid = ["water"]*100
        self.grid = grid

    def __getitem__(self, item):
        return self.grid[item]
class Grid:
    def __init__(self):
        grid = ["water"]*100
        self.grid = grid

    def __getitem__(self, item):
        return self.grid[item]

    def __setitem__(self, key, value):
        self.grid[key] = value

class Tile:
    def __init__(self,m,n,gridtile):
        self.m = m
        self.n = n
        self.gridtile = gridtile
    def getvalue(self):
        return self.gridtile[(10*(self.m-1))+(self.n-1)]
    def setvalue(self,value):
        self.gridtile[(10*(self.m-1))+(self.n-1)] = value

class Boat:
    def __init__(self,lenght):
        self.lenght = lenght
    def placeboat_horizontaly(self,init_line,init_col,gridboat1):
        for i in range(self.lenght):
            init_tile = Tile(init_line,init_col+i,gridboat1)
            init_tile.setvalue("boat")
    def placeboat_verticaly(self,init_line,init_col,gridboat1):
        for i in range(self.lenght):
            init_tile = Tile(init_line+i,init_col,gridboat1)
            init_tile.setvalue("boat")