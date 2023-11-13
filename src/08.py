#Advent of Code 2016 Day 8

from tools import files
import re

def get_lit(grid):

    lit = 0

    for row in grid:
        for pixel in row:
            if pixel == "#":
                lit += 1
    
    return lit


def show(grid):

    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            
            if grid[y][x] == ".":
                print(" ", end="")
            else: 
                print(grid[y][x], end="")

        print()


def rotate_column(id, amount, grid):
    
    temp = [grid[y][id] for y in range(0, len(grid))]
    
    for y in range(0, len(grid)):

        if y+amount >= len(grid):
            grid[y+amount-len(grid)][id] = temp[y]

        else:
            grid[y+amount][id] = temp[y]

    return grid


def rotate_row(id, amount, grid):

    temp = [grid[id][x] for x in range(0, len(grid[0]))]

    for x in range(0, len(grid[0])):

        if x+amount >= len(grid[0]):
            grid[id][x+amount-len(grid[0])] = temp[x]
        
        else:
            grid[id][x+amount] = temp[x]
    
    return grid


def parse_rect(line, grid):

    instructions = re.split(" |x", line)
    
    for y in range(0, int(instructions[2])):
        for x in range(0, int(instructions[1])):
            grid[y][x] = "#"

    return grid


def parse_rotate(line, grid):

    instructions = re.split(" |=", line)

    direction = instructions[1]
    id = int(instructions[3])
    amount = int(instructions[5])
    
    if direction == "column":
        grid = rotate_column(id, amount, grid)

    elif direction == "row":
        grid = rotate_row(id, amount, grid)

    return grid


def parse_input(input, grid):
    
    for line in input:
        if "rect" in line:
            grid = parse_rect(line, grid)
        elif "rotate" in line:
            grid = parse_rotate(line, grid)

    return grid


filename = "input/08.txt"
input = files.input_as_list(filename)
grid = [["." for x in range(0, 50)] for y in range(0, 6)]

#input = ["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1"]
#grid = [["." for x in range(0, 7)] for y in range(0, 3)]

# Part 1

grid = parse_input(input, grid)
lit = get_lit(grid)

print("Part 1: The amount of lit pixels are {}".format(lit))

# Part 2

print("Part 2: ")
show(grid)