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
    def __init__(self, cube, colrow, position, direction, path=None, temppath=None):
        self.cube = cube
        self.colRow = colrow
        self.position = position
        self.direction = direction
        self.path = path if path is not None else []
        self.temppath = cube
        


# This is where our Heuristic for how close the cube is to be solved will go

def initializefunction():
    cubeObject = Cube()

    FC00 = Movement(cubeObject.Front, colrow="C", position=0, direction=0)
    FC01 = Movement(cubeObject.Front, colrow="C", position=0, direction=1)
    FC10 = Movement(cubeObject.Front, colrow="C", position=0, direction=1)
    FC11 = Movement(cubeObject.Front, colrow="C", position=0, direction=1)
    FR00 = Movement(cubeObject.Front, colrow="R", position=0, direction=0)
    FR01 = Movement(cubeObject.Front, colrow="R", position=0, direction=1)
    FR10 = Movement(cubeObject.Front, colrow="R", position=0, direction=0)
    FR11 = Movement(cubeObject.Front, colrow="R", position=0, direction=1)

    LC00 = Movement(cubeObject.Left, colrow="C", position=0, direction=0)
    LC01 = Movement(cubeObject.Left, colrow="C", position=0, direction=1)
    LC10 = Movement(cubeObject.Left, colrow="C", position=0, direction=0)
    LC11 = Movement(cubeObject.Left, colrow="C", position=0, direction=1)

    applyMovement(FC00)
    applyMovement(LC00)

    printCube(cubeObject)
    
def applyMovement(movement: Movement):
    cube = movement.cube

    if movement.colRow == "C":  # column move
        applyColumnMove(cube, movement.position, movement.direction)
    elif movement.colRow == "R":  # row move
        applyRowMove(cube, movement.position, movement.direction)


def applyColumnMove(cube, col, direction):
    tempcol = [cube.facevalue[i][col] for i in range(3)]
    
    if (cube.centervalue == "8Y"):
        print("Front")
    else:
        print("Left")

    print(tempcol)
    print("Testing Column Move")
    print("Cube is ", cube.centervalue)
    print("col is ", col)
    print("direction is ", direction)

def applyRowMove(cube, row, direction):
    temprow = [cube.facevalue[row][i] for i in range(3)]

    print("Testing Row Move")
    print("Cube is ", cube)
    print("col is ", row)
    print("direction is ", direction)


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