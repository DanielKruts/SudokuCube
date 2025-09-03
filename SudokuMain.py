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
        self.Front = CubeSide
        self.Back = CubeSide
        self.Left = CubeSide
        self.Right = CubeSide
        self.Up = CubeSide
        self.Down = CubeSide

# class Movement:



def initializefunction():
    cubeObject = Cube()
    cubeObject.Front.centercolor = 'Y'
    cubeObject.Front.centercolor = 'P'
    cubeObject.Left.centercolor = 'B'
    cubeObject.Right.centercolor = 'G'
    cubeObject.Up.centercolor = 'O'
    cubeObject.Down.centercolor = 'R'

    
    cubeObject.Front.facevalue = [[9, 5, 2], [3, 8, 1], [6, 7, 4]]
    cubeObject.Back.facevalue = [[9, 5, 2], [3, 8, 1], [6, 7, 4]]
    cubeObject.Left.facevalue = [[7, 1, 8], [2, 4, 6], [9, 3, 5]]
    cubeObject.Right.facevalue = [[4, 6, 3], [7, 5, 9], [1, 2, 8]]
    cubeObject.Up.facevalue = [[8, 1, 3], [4, 6, 7], [2, 9, 5]]
    cubeObject.Down.facevalue = [[1, 2, 8], [5, 3, 9], [7, 4, 6]]

    print("Front center:", cubeObject.Front.centervalue)
    print("Front face:", cubeObject.Front.facevalue)
    print("Back center:", cubeObject.Back.centervalue)
    print("Left face:", cubeObject.Left.facevalue)

    return cubeObject

initializefunction()




