# Advent of Code 2016 Day 1

from tools import files
from tools import points

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

        q[2] = turn(direction, q[2])

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

        q[2] = turn(direction, q[2])

        moving = []

        match q[2]:
            
            case "N":
                moving = [0, distance, 1]

            case "E":
                moving = [distance, 0, 1]
            
            case "S":
                moving = [0, -distance, -1]
                
            case "W":
                moving = [-distance, 0, -1]

            case _: 
               exit(4)

        for x in range (q[0], q[0]+moving[0]+moving[2], moving[2]):
            for y in range(q[1], q[1]+moving[1]+moving[2], moving[2]):
    
                if x == q[0] and y == q[1]:
                    continue

                check = (x, y)

                if check in visited:
                    q[0] = x
                    q[1] = y
                    return q

                visited.add(check)

        q[0] += moving[0]
        q[1] += moving[1]

    return q

# Part 1

input = files.input_as_string("input/01.txt")
origin = [0, 0, "N"]

q = parse_input_part1(input, origin)

result = points.calculate_manhattan(origin, q)

print("Part 1: The distance to Bunny HQ is {}".format(result))

# Part 2

q = parse_input_part2(input, origin)

result = points.calculate_manhattan(origin, q)

print("Part 2: The distance to Bunny HQ is {}".format(result))