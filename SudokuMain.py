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
    def __init__(self, cube, colrow, position, direction, name, path=None, temppath=None):
        self.cube = cube
        self.colRow = colrow
        self.position = position
        self.direction = direction
        self.path = path if path is not None else []
        self.temppath = cube
        self.name = name
        


# This is where our Heuristic for how close the cube is to be solved will go

def initializefunction():

    cubeObject = Cube()

    FC00 = Movement(cubeObject.Front, colrow="C", position=0, direction=0, name = "FC00")
    FC01 = Movement(cubeObject.Front, colrow="C", position=0, direction=1, name = "FC01")
    FC10 = Movement(cubeObject.Front, colrow="C", position=2, direction=1, name = "FC10")
    FC11 = Movement(cubeObject.Front, colrow="C", position=2, direction=1, name = "FC11")
    FR00 = Movement(cubeObject.Front, colrow="R", position=0, direction=0, name = "FR00")
    FR01 = Movement(cubeObject.Front, colrow="R", position=0, direction=1, name = "FR01")
    FR10 = Movement(cubeObject.Front, colrow="R", position=2, direction=0, name = "FR10")
    FR11 = Movement(cubeObject.Front, colrow="R", position=2, direction=1, name = "FR11")

    LC00 = Movement(cubeObject.Left, colrow="C", position=0, direction=0, name = "LC00")
    LC01 = Movement(cubeObject.Left, colrow="C", position=0, direction=1, name = "LC01")
    LC10 = Movement(cubeObject.Left, colrow="C", position=2, direction=0, name = "LC10")
    LC11 = Movement(cubeObject.Left, colrow="C", position=2, direction=1, name = "LC11")

    applyMovement(FC00, cubeObject)
    applyMovement(LC00, cubeObject)

    printCube(cubeObject)

    movelist = [FC00, FC01, FC10, FC11, FR00, FR01, FR10, FR11, LC00, LC01, LC10, LC11]

    return movelist, cubeObject
    

def applyMovement(movement: Movement, cubeObject):
    cube = movement.cube
    print("Movement is ")

    if movement.colRow == "C":  # column move
        applyColumnMove(cube, movement.position, movement.direction, movement.name, cubeObject)
    elif movement.colRow == "R":  # row move
        applyRowMove(cube, movement.position, movement.direction, movement.name, cubeObject)



def applyColumnMove(cube, col, direction, name, cubeObject):
    tempcol = [cube.facevalue[i][col] for i in range(3)] # initializing the temp col

    print(tempcol)
    print("Cube is ", cube.centervalue)
    print("col is ", col) # 0 is leftmost column, 2 is rightmost column
    print("direction is ", direction) # 0 is down, 1 is up
    print("Movement is ", name)

    if (direction == 0) and (cube.centervalue == "8Y"): # Down on Front side
        path = [cubeObject.Front, cubeObject.Down, cubeObject.Back, cubeObject.Up]
    elif (direction == 1) and (cube.centervalue == "8Y"): # Up on Front side
        path = [cubeObject.Front, cubeObject.Up, cubeObject.Back, cubeObject.Down]
    elif (direction == 0) and (cube.centervalue == "4B"): # Down on Left side
        path = [cubeObject.Left, cubeObject.Down, cubeObject.Right, cubeObject.Up] 
    elif (direction == 1) and (cube.centervalue == "4B"): # Up on Left side
        path = [cubeObject.Left, cubeObject.Up, cubeObject.Right, cubeObject.Down]
    else:
        print("Invalid Parameters")

    if (cube.centervalue == "8Y" and col == 0): # rotating left column on front side, rotating face is left side
        rotateface = cubeObject.Left
    elif (cube.centervalue == "8Y" and col == 2): # rotating right column on front side, rotating face is right side
        rotateface = cubeObject.Right
    elif (cube.centervalue == "4B" and col == 0): # rotating left column on left side, rotating face is back side
        rotateface = cubeObject.Back
    elif (cube.centervalue == "4B" and col == 2): # rotating right column on left side, rotating face is front side
        rotateface = cubeObject.Front
    else:
        print("Invalid Parameters")




def applyRowMove(cube, row, direction, name, cubeObject):

    temprow = [cube.facevalue[row][i] for i in range(3)] # initializing the temp row
    
    print(temprow)
    print("Cube is ", cube.centervalue)
    print("row is ", row) # 0 is top row, 2 is bottom row
    print("direction is ", direction) # 0 is left, 1 is right
    print("Movement is ", name)

    if (direction == 0) and (cube.centervalue == "8Y"): # Left on Front side
        path = [cubeObject.Front, cubeObject.Left, cubeObject.Back, cubeObject.Right]
    elif (direction == 1) and (cube.centervalue == "8Y"): # Right on Front side
        path = [cubeObject.Front, cubeObject.Right, cubeObject.Back, cubeObject.Left]
    else:
        print("Invalid Parameters")

    if (row == 0):
        rotateface = cubeObject.Up
    elif (row == 2):
        rotateface = cubeObject.Down
    else:
        print("Invalid Parameters")


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
    
import random

movelist,cubeObject = initializefunction()

newmove = 1
previous_var = -1

while(newmove == 1):
    user_input = input("Would you like to complete a move? Y/N:\n")

    match user_input:
        case "Y" | "y":
            print("Alright bruv")

            random_var = random.randint(0, 11)
            while random_var == previous_var:
                print("Same move as last time, rerolling")
                random_var = random.randint(0, 11)

            movechosen = movelist[random_var]
            print("Random Move is ", movechosen.name)
            applyMovement(movechosen, cubeObject)

            printCube(cubeObject)
            previous_var = random_var
        case "N" | "n":
            print("See ya cuh")
            newmove = 0
        case _:
            print("Whachu mean bitch")