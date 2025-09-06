'''
Test
Classes - 
    CubeSide Class(Stores matrices, center element(string) 4th element) 
    6 CubeSide elements for each face
Class Movement - 
    12 (Cube Side, Column/Row - Binary, Position - Binary, Movement(Up/Down) 
    Binary, Roate Side, Array of Sides path, Temp side(Maybe0))
Test Hoe
'''
#Might be removed, but starter class definitions for CubeSide and Movement
class CubeSide:
    # self initialization created for CubeSide to fix centervalue variable issues
    def __init__(self, facevalue, centercolor):
        self.facevalue = facevalue
        self.centercolor = centercolor
        self.centervalue = str(facevalue[1][1]) + self.centercolor

#Creates a cube with 6 predetermined sides of a solved cube
class Cube:
    def __init__(self):
        self.Front = CubeSide([[9, 5, 2], [3, 8, 1], [6, 7, 4]], 'Y')
        self.Back = CubeSide([[9, 5, 2], [3, 8, 1], [6, 7, 4]], 'P')
        self.Left = CubeSide([[7, 1, 8], [2, 4, 6], [9, 3, 5]], 'B')
        self.Right = CubeSide([[4, 6, 3], [7, 5, 9], [1, 2, 8]], 'G')
        self.Up = CubeSide([[8, 1, 3], [4, 6, 7], [2, 9, 5]], 'O')
        self.Down = CubeSide([[1, 2, 8], [5, 3, 9], [7, 4, 6]], 'R')

# Class Movement
class Movement:
    '''
    Self initialization takes multiple parameters
    side - Side of the cube to be moved
    colRow - Whether the movement is of a column or row (0: column, 1:row)
    position - 
    movement - 
    rotateSide - 
    array of sides path - 
    '''
    def __init__(self, Cube, movement colrow, position, direction, path, temppath):
        self.movement = movement
        self.movement.side = side
        self.movement.colRow = colrow
        self.movement.position = position
        self.movement.direction = direction
        self.movement.path = path
        self.movement.temppath = temppath
        


# This is where our Heuristic for how close the cube is to be solved will go

def initializefunction():
    cubeObject = Cube()

    FC00 = Movement(Front, Column, Left, Down, {}, Front)


    printCube(cubeObject)
    

def printCube(cubeObject):
    # Takes a looper iterating through the desired values of the sides of the cube and prints them in a readable format
    '''
    for i in [cubeObject.Front, cubeObject.Back, cubeObject.Left, cubeObject.Right, cubeObject.Up, cubeObject.Down]:
        print(f"Face Value:\n{i.facevalue[0]}\n{i.facevalue[1]}\n{i.facevalue[2]}\nCenter Value: {i.centervalue}\n")
    '''
    for i in [cubeObject.Up]:
        print(f"\t {i.facevalue[0]}\n\t {i.facevalue[1]}\n\t {i.facevalue[2]}")
    
    for i in [cubeObject.Left, cubeObject.Front, cubeObject.Right, cubeObject.Back]:
         print(i.facevalue[0], end="")
    print("")
    for i in [cubeObject.Left, cubeObject.Front, cubeObject.Right, cubeObject.Back]:
         print(i.facevalue[1], end="")
    print("")
    for i in [cubeObject.Left, cubeObject.Front, cubeObject.Right, cubeObject.Back]:
         print(i.facevalue[2], end="")
    print("")
    for i in [cubeObject.Down]:
            print(f"\t {i.facevalue[0]}\n\t {i.facevalue[1]}\n\t {i.facevalue[2]}")
    
initializefunction()