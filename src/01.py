# Advent of Code 2016 Day 1

def open_input(filename):

    f = open(filename, "r")

    return f.read()

def calculate_manhattan(p, q):
    """ Calculating and returning the manhattan distance between two points, p and q. The function expects two points in 2D space, as lists"""

    return ( abs(p[0]-q[0]) + abs(p[1]-q[1]) )

def turn(direction, facing):
    """ This fuction turns 90 degrees left or right, and returns the new direction you're facing."""

    match direction:
            case "L":
                match facing:
                    case "N":
                        facing = "W"
                    case "W":
                        facing = "S"
                    case "S":
                        facing = "E"
                    case "E":
                        facing = "N"
                    case _: 
                        exit(1)

            case "R":
                match facing:
                    case "N":
                        facing = "E"
                    case "E":
                        facing = "S"
                    case "S":
                        facing = "W"
                    case "W":
                        facing = "N"
                    case _: 
                        exit(2)

            case _: 
               exit(3)

    return facing

def parse_input_part1(input, p):
    """Parsing the input, moving along in 2d space from the origin, returning the result of the movement"""

    q = p.copy()

    movement = input.split(", ")

    for instruction in movement:

        direction = instruction[0]
        distance = int(instruction[1:])
        facing = q[2]

        q[2] = turn(direction, facing)

        match q[2]:
            case "N":
                q[1] += distance
            case "E":
                q[0] += distance
            case "S":
                q[1] -= distance
            case "W":
                q[0] -= distance

            case _: 
               exit(4)

    return q

def parse_input_part2(input, p):
    """ This function checks if we've been to a point before - Not just where we stop, but ANY point. """

    visited = set()
    q = p.copy()

    movement = input.split(", ")

    for instruction in movement:

        direction = instruction[0]
        distance = int(instruction[1:])
        facing = q[2]

        q[2] = turn(direction, facing)

        match q[2]:
            
            case "N":
                
                for x in range(q[1]+1, q[1]+distance+1):
                    check = (q[0], x)
                
                    if check in visited:
                        q[1] = x
                        return q
                    
                    visited.add(check)
                
                q[1] += distance

            case "E":
            
                for x in range(q[0]+1, q[0]+distance+1):
            
                    check = (x, q[1])
            
                    if check in visited:
                        q[0] = x                
                        return q
                    
                    visited.add(check)
            
                q[0] += distance
            
            case "S":
            
                for x in range(q[1]-1, q[1]-distance-1, -1):
            
                    check = (q[0], x)
            
                    if check in visited:
                        q[1] = x                
                        return q

                    visited.add(check)                                
            
                q[1] -= distance
            
            case "W":
            
                for x in range(q[0]-1, q[0]-distance-1, -1):
            
                    check = (x, q[1])
            
                    if check in visited:
                        q[0] = x                
                        return q

                    visited.add(check)           
            
                q[0] -= distance

            case _: 
               exit(4)

    return q

def test(input, expected):
    """Testing that our part 1 functions gives the expected results. The function takes a string (to parse) as the argument, and the expected result of the manhattan calculation"""

    p = [1, 1, "N"]
    q = [2, 3, "S"]

    if calculate_manhattan(p, q) == 3:
        print("Manhattan works!")

    p = [0, 0, "N"]
    q = parse_input_part1(input, p)

    if calculate_manhattan(p, q) == expected:
        print("Parsing works!")

#test("R2, L3", 5)
#test("R2, R2, R2", 2)
#test("R5, L5, R5, R3", 12)

# Part 1

input = open_input("input/01.txt")
origin = [0, 0, "N"]

q = parse_input_part1(input, origin)

result = calculate_manhattan(origin, q)

print("Part 1: The distance to Bunny HQ is {}".format(result))

# Part 2

#input = "R8, R4, R4, R8"

q = parse_input_part2(input, origin)

result = calculate_manhattan(origin, q)

print("Part 2: The distance to Bunny HQ is {}".format(result))