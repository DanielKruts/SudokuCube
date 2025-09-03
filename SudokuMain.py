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
    centervalue = str(facevalue[1][1]) + centercolor

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
    print("Front center:", Cube.Front.centervalue)
    print("Front face:", Cube.Front.facevalue)
    print("Back center:", Cube.Back.centervalue)
    print("Left face:", Cube.Left.facevalue)

    return Cube




