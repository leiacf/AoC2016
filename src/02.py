# Advent of Code 2016 Day 2

from tools import files

def find_spot(start, grid):

    for row in range (0, len(grid)):
        for column in range(0, len(grid[0])):

            if grid[row][column] == start:

                return (row, column)

    return (-1, -1)

def move_part_1(input, start):

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    row, column = find_spot(start, grid)

    for letter in input:

        match letter:

            case "U":
                row = row - 1
                if row < 0: 
                    row = 0

            case "R":
                column = column + 1
                if column >= len(grid[row]):
                    column = len(grid[row]) - 1 

            case "D":
                row = row + 1
                if row >= len(grid): 
                    row = len(grid) - 1

            case "L":
                column = column - 1
                if column < 0: 
                    column = 0

            case _:
                exit(1)

    result = grid[row][column]

    return result

def move_part_2(input, start):

    grid = [["x", "x", 1, "x", "x"], ["x", 2, 3, 4, "x"],[ 5, 6, 7, 8, 9], ["x", "A", "B", "C", "x"], ["x", "x", "D", "x", "x"]]

    row, column = find_spot(start, grid)

    for letter in input:

        match letter:

            case "U":
                row = row - 1
                if row < 0 or grid[row][column] == "x": 
                    row = row + 1

            case "R":
                column = column + 1
                if column >= len(grid[row]) or grid[row][column] == "x":
                    column = column - 1 

            case "D":
                row = row + 1
                if row >= len(grid) or grid[row][column] == "x": 
                    row = row - 1

            case "L":
                column = column - 1
                if column < 0 or grid[row][column] == "x": 
                    column = column + 1

            case _:
                exit(1)

    result = grid[row][column]

    return result

def test(input, start, expected):

    result = move_part_1(input, start)

    return (result == expected)

filename = "input/02.txt"
input = files.input_as_list(filename)

# Part 1

start = 5
code = ""

for line in input:
    start = move_part_1(line, start)
    code += str(start)

print("Part 1: The code is {}".format(code))

# Part 2

start = 5
code = ""

for line in input:
    start = move_part_2(line, start)
    code += str(start)

print("Part 2: The code is {}".format(code))