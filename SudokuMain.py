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
from dis import findlinestarts
from tkinter.filedialog import Directory


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
    cube - the whole Cube object
    face - which face the move applies to ("Front", "Left", "Right", etc.)
    colRow - "C" (column) or "R" (row)
    position - 0 (left/top) or 2 (right/bottom)
    direction - 0 or 1 (clockwise/counterclockwise or down/up/left/right depending on context)
    name - shorthand label like "FC00"
    '''
    def __init__(self, cube, face, colrow, position, direction, name, path=None):
        self.cube = cube
        self.face = face
        self.colRow = colrow
        self.position = position
        self.direction = direction
        self.name = name
        self.path = path if path is not None else []


# This is where our Heuristic for how close the cube is to be solved will go
def heuristic(cube: Cube):
    score = 0
    i = 0
    for side in [cube.Front, cube.Back, cube.Left, cube.Right, cube.Up, cube.Down]:
        currentface = side.facevalue
        missingvalues = 9 - len(np.unique(currentface))
        print(f"Side {side.centervalue} has values {missingvalues}")
    return score

def initializefunction():
    cubeObject = Cube()

    FC00 = Movement(cubeObject, face="Front", colrow="C", position=0, direction=0, name="FC00")
    FC01 = Movement(cubeObject, face="Front", colrow="C", position=0, direction=1, name="FC01")
    FC10 = Movement(cubeObject, face="Front", colrow="C", position=2, direction=0, name="FC10")
    FC11 = Movement(cubeObject, face="Front", colrow="C", position=2, direction=1, name="FC11")

    FR00 = Movement(cubeObject, face="Front", colrow="R", position=0, direction=0, name="FR00")
    FR01 = Movement(cubeObject, face="Front", colrow="R", position=0, direction=1, name="FR01")
    FR10 = Movement(cubeObject, face="Front", colrow="R", position=2, direction=0, name="FR10")
    FR11 = Movement(cubeObject, face="Front", colrow="R", position=2, direction=1, name="FR11")

    LC00 = Movement(cubeObject, face="Left", colrow="C", position=0, direction=0, name="LC00")
    LC01 = Movement(cubeObject, face="Left", colrow="C", position=0, direction=1, name="LC01")
    LC10 = Movement(cubeObject, face="Left", colrow="C", position=2, direction=0, name="LC10")
    LC11 = Movement(cubeObject, face="Left", colrow="C", position=2, direction=1, name="LC11")

    printCube(cubeObject)

    movelist = [FC00, FC01, FC10, FC11,
                FR00, FR01, FR10, FR11,
                LC00, LC01, LC10, LC11]

    return movelist, cubeObject

def applyMovement(movement: Movement):
    cube = movement.cube
    print("Movement is", movement.name)

    if movement.colRow == "C":  # column move
        applyColumnMove(cube, movement.face, movement.position, movement.direction, movement.name)
    elif movement.colRow == "R":  # row move
        applyRowMove(cube, movement.face, movement.position, movement.direction, movement.name)
    else:
        print("Invalid Movement type")
        exit()


def applyColumnMove(cube: Cube, face: str, col: int, direction: int, name: str):
    print("Column move:", name, "| face:", face, "| col:", col, "| direction:", direction)

    if face == "Front":
        if col == 0:  # Left column
            if direction == 0:  # Down
                cube.Left.facevalue = rotate_face_clockwise(cube.Left.facevalue)
            else:  # Up
                cube.Left.facevalue = rotate_face_counterclockwise(cube.Left.facevalue)
        elif col == 2:  # Right column
            if direction == 0:  # Down
                cube.Right.facevalue = rotate_face_counterclockwise(cube.Right.facevalue)
            else:  # Up
                cube.Right.facevalue = rotate_face_clockwise(cube.Right.facevalue)
        else:
            print("Invalid column for Front move")
            exit()

        # TODO: update path shifting for Front col moves
        move(cube, cube.Front, direction, [cube.Front, cube.Down, cube.Back, cube.Up])

    elif face == "Left":
        if col == 0:  # Left column
            if direction == 0:  # Down
                cube.Back.facevalue = rotate_face_clockwise(cube.Back.facevalue)
            else:  # Up
                cube.Back.facevalue = rotate_face_counterclockwise(cube.Back.facevalue)
        elif col == 2:  # Right column
            if direction == 0:  # Down
                cube.Front.facevalue = rotate_face_counterclockwise(cube.Front.facevalue)
            else:  # Up
                cube.Front.facevalue = rotate_face_clockwise(cube.Front.facevalue)
        else:
            print("Invalid column for Left move")
            exit()

        # TODO: update path shifting for Left col moves
        move(cube, cube.Left, direction, [cube.Left, cube.Down, cube.Right, cube.Up])

    else:
        print("Invalid face for column move")
        exit()





def applyRowMove(cube: Cube, face: str, row: int, direction: int, name: str):
    print("Row move:", name, "| face:", face, "| row:", row, "| direction:", direction)

    if face == "Front":
        if row == 0:  # Top row
            if direction == 0:  # Left
                cube.Up.facevalue = rotate_face_clockwise(cube.Up.facevalue)
            else:  # Right
                cube.Up.facevalue = rotate_face_counterclockwise(cube.Up.facevalue)
        elif row == 2:  # Bottom row
            if direction == 0:  # Left
                cube.Down.facevalue = rotate_face_counterclockwise(cube.Down.facevalue)
            else:  # Right
                cube.Down.facevalue = rotate_face_clockwise(cube.Down.facevalue)
        else:
            print("Invalid row for Front move")
            exit()

        # TODO: update path shifting for Front row moves
        move(cube, cube.Front, direction, [cube.Front, cube.Left, cube.Back, cube.Right])

    else:
        print("Invalid face for row move")
        exit()

def get_path_from_movement(movement: Movement):
    """
    Returns the faces and strip orientation for a move.
    face: "Front", "Left", etc.
    colRow: "C" for column, "R" for row
    position: 0 (left/top) or 2 (right/bottom)
    Returns: path_faces [4 CubeSides], path_orientations ["row2", "col0", ...]
    """
    cube = movement.cube
    face = movement.face
    colRow = movement.colRow
    position = movement.position
    direction = movement.direction

    if colRow == "C":  # Column moves
        if face == "Front":
            if position == 0:
                if direction == 0:
                    return  ["col2", "col0", "col0", "col2"]
                elif direction == 1:
                    return  ["col0", "col2", "col2", "col0"]
            elif position == 2:
                if direction == 0:
                    return  ["col2", "col0", "col0", "col2"]
                elif direction == 1:
                    return  ["col0", "col2", "col2", "col0"]
        elif face == "Left":
            if direction == 0:  # Left column
                return ["col0", "col2", "col0", "col0"]
            elif direction == 2:  # Right column
                return [cube.Up, cube.Front, cube.Down, cube.Back], ["col2", "col2", "col2", "col0"]
    elif colRow == "R":  # Row moves
            if direction == 0:  # Top row
                return [cube.Up, cube.Right, cube.Down, cube.Left], ["row2", "row0", "row0", "row2"]
            elif direction == 2:  # Bottom row
                return [cube.Down, cube.Right, cube.Up, cube.Left], ["row2", "row2", "row0", "row0"]
    else:
        print("Invalid Parameters")
        exit()


# Rotates a given facevalue clockwise
def rotate_face_clockwise(face):
    return [list(row) for row in zip(*face[::-1])]

# Rotates a given facevalue counterclockwise
def rotate_face_counterclockwise(face):
    return [list(row) for row in zip(*face)][::-1]

#Moves the front face clockwise or counterclockwise, considering the parameter wise, (0 is clockwise, 1 is counterclockwise)
def move(movement:Movement, path: list[CubeSide]):
    """
    Rotates the edge strips around a given face.
    - cube: full Cube object
    - face: the CubeSide being rotated
    - direction: 0 = clockwise, 1 = counterclockwise
    - path: list of 4 CubeSides in the order they wrap around the face
    """

    if movement.direction == 0:  # Clockwise
            movement.face.facevalue = rotate_face_clockwise(movement.face.facevalue)
    elif movement.direction == 1:  # Counterclockwise
            movement.face.facevalue = rotate_face_counterclockwise(movement.face.facevalue)
    else:
            print("Invalid direction")
            exit()
    if movement.face == "Front":
        if movement.colRow == "R": # Row move
            if movement.position == 0: # Top row
                temp = path[0].facevalue[0][:]
                if movement.direction == 0: # Clockwise
                    path[2].facevalue[0][:] = path[1].facevalue[0][:]
                    path[3].facevalue[0][:] = path[2].facevalue[0][:]
                    path[0].facevalue[0][:] = path[3].facevalue[0][:]
                    path[1].facevalue[0][:] = temp
                elif movement.direction == 1: # Counterclockwise
                    path[2].facevalue[0][:] = path[3].facevalue[0][:]
                    path[1].facevalue[0][:] = path[2].facevalue[0][:]
                    path[0].facevalue[0][:] = path[1].facevalue[0][:]
                    path[3].facevalue[0][:] = temp
            elif movement.position == 2: # Bottom row
                temp = path[0].facevalue[2][:]
                if movement.direction == 0: # Counterclockwise
                    path[2].facevalue[2][:] = path[3].facevalue[2][:]
                    path[1].facevalue[2][:] = path[2].facevalue[2][:]
                    path[0].facevalue[2][:] = path[1].facevalue[2][:]
                    path[3].facevalue[2][:] = temp
                elif movement.direction == 1: # Clockwise
                    path[2].facevalue[2][:] = path[1].facevalue[2][:]
                    path[3].facevalue[2][:] = path[2].facevalue[2][:]
                    path[0].facevalue[2][:] = path[3].facevalue[2][:]
                    path[1].facevalue[2][:] = temp
        elif movement.colRow == "C": # Column move
            if movement.position == 0: # Left column
                temp = path[0].facevalue[:][0]
                if movement.direction == 0: # Down
                    path[2].facevalue[:][0] = path[3].facevalue[:][0]
                    for i in range(3):
                        path[1].facevalue[i][0] = path[2].facevalue[2-i][0]
                    path[0].facevalue[:][0] = path[1].facevalue[:][0]
                    path[3].facevalue[:][0] = temp
                elif movement.direction == 1: #Up
                    for i in range(3):
                        path[2].facevalue[i][0] = path[1].facevalue[2-i][0]
                    path[3].facevalue[:][0] = path[2].facevalue[:][0]
                    for i in range(3):
                        path[0].facevalue[i][0] = path[3].facevalue[2-i][0]
                    path[1].facevaluep[:][0] = temp
            elif movement.position == 2: # Right column
                temp = path[0].facevalue[:][2]
                if movement.direction == 0: # Down
                    for i in range(3):
                        path[2].facevalue[i][0] = path[3].facevalue[2-i][2]
                    for i in range(3):
                        path[1].facevalue[i][2] = path[2].facevalue[2-i][0]
                    path[0].facevalue[:][2] = path[1].facevalue[:][2]
                    path[3].facevalue[:][2] = temp
                elif movement.direction == 1: #Up
                    path[2].facevalue[:][0] = path[3].facevalue[:][2]
                    for i in range(3):
                        path[1].facevalue[i][2] = path[2].facevalue[2-i][0]
                    path[0].facevalue[:][2] = path[1].facevalue[:][2]
                    path[3].facevalue[:][2] = temp
    elif movement.face == "Left":
        exit()
        
    '''
    subsectionarray = []
    for i, side in enumerate(path):
        print(f"Path {i}: Face {side.centervalue}")
        movementalightnment = get_path_from_movement(movement)
        if movementalightnment[i] == "row0":
            print("Orientation: Top Row")
            subsectionarray[i] = path[i].facevalue[0][:]
        elif movementalightnment[i] == "row2":
            print("Orientation: Bottom Row")
            subsectionarray[i] = path[i].facevalue[2][:]
        elif movementalightnment[i] == "col0":
            print("Orientation: Left Column")
            subsectionarray[i] = path[i].facevalue[:][0]
        elif movementalightnment[i] == "col2":
            print("Orientation: Right Column")
            subsectionarray[i] = path[i].facevalue[:][2]
        else:
            print("Invalid orientation")
            exit()
    
    i = 1
    for i, side in enumerate(path):
        if movementalightnment[i][:3] == movementalightnment[i+1][:3]:
            path[i].facevalue[0] = path[i-1].facevalue[0][:]
            
    # Each face contributes a row/column to the cycle
    strips = []

    # Extract strips
    for i, side in enumerate(path):
        if i == 0:   # from bottom row of top/first face
            strips.append(side.facevalue[2][:])
        elif i == 1: # from right column
            strips.append([side.facevalue[j][0] for j in range(3)])
        elif i == 2: # from top row
            strips.append(side.facevalue[0][:])
        elif i == 3: # from left column
            strips.append([side.facevalue[j][2] for j in range(3)])

    # Rotate strips depending on direction
    if direction == 0:  # Clockwise
        new_strips = [strips[-1]] + strips[:-1]
    else:               # Counterclockwise
        new_strips = strips[1:] + [strips[0]]

    # Write back strips
    for i, side in enumerate(path):
        if i == 0:   # bottom row
            side.facevalue[2] = new_strips[i]
        elif i == 1: # left column
            for j in range(3):
                side.facevalue[j][0] = new_strips[i][j]
        elif i == 2: # top row
            side.facevalue[0] = new_strips[i]
        elif i == 3: # right column
            for j in range(3):
                side.facevalue[j][2] = new_strips[i][j]
'''

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
    print("")

import random
import numpy as np

movelist,cubeObject = initializefunction()

heuristic(cubeObject)

'''
move(cubeObject, 1)
printCube(cubeObject)
move(cubeObject, 0)
printCube(cubeObject)
'''
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
            pathprint = get_path_from_movement(movechosen)
            print("Path is", [side.centercolor for side in pathprint[0]], "with orientations", pathprint[1])
            applyMovement(movechosen)

            printCube(cubeObject)
            heuristic(cubeObject)
            previous_var = random_var
        case "N" | "n":
            print("See ya cuh")
            newmove = 0
        case _:
            print("Whachu mean bitch")
