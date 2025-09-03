'''
Classes - 
    CubeSide Class(Stores matrices, center element(string) 4th element) 
    6 CubeSide elements for each face
Class Movement - 
    12 (Cube Side, Column/Row - Binary, Position - Binary, Movement(Up/Down) 
    Binary, Roate Side, Array of Sides path, Temp side(Maybe0))
'''
#Might be removed, but starter class definitions for CubeSide and Movement
class CubeSide:
    facevalue = [[0,0,0],[0,0,0],[0,0,0]]
    centercolor = ""
    centervalue = facevalue[1][1] + centercolor

class Cube:
    def __init__(self):
        self.Front = CubeSide.centercolor("Y")
        self.Back = CubeSide.centercolor("P")
        self.Left = CubeSide.centercolor("B")
        self.Right = CubeSide.centercolor("G")
        self.Up = CubeSide.centercolor("O")
        self.Down = CubeSide.centercolor("R")

# class Movement:



def initializefunction():
    Cube.Front.facevalue = [ [9,5,2], [3,8,1], [6,7,4] ]
    Cube.Back.facevalue = [ [9,5,2], [3,8,1], [6,7,4] ]
    Cube.Left.facevalue = [ [7,1,8], [2,4,6], [9,3,5] ]
    Cube.Right.facevalue = [ [4,6,3], [7,5,9], [1,2,8] ]
    Cube.Up.facevalue = [ [8,1,3], [4,6,7], [2,9,5] ]
    Cube.Down.facevalue = [ [1,2,8], [5,3,9], [7,4,6] ]

    return Cube.Down.centervalue



