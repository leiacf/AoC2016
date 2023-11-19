#Advent of Code 2016 Day 13

from tools import points
from tools import graph

def calculate(x, y, fav):

    sum = x*x + 3*x + 2*x*y + y + y*y
    sum += fav

    binary = bin(sum)
    counter = 0

    for digit in binary:
        if digit == "1":
            counter += 1

    if counter % 2 == 0:
        return "."

    return "#"

def show(grid):

    print()

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            print(grid[y][x], end="")
        print()

    print()


def createGrid(width, height, input):

    grid = []

    for y in range(0, height):
        row = []
        for x in range(0, width):
            point = points.Point(x, y, (calculate(x, y, input)))
            row.append(point)
        grid.append(row)

    return grid

input = 1352
#input = 10

# Part 1

start = points.Point(1, 1, "O")
grid = createGrid(100, 100, input)
graph.djikstra(grid, start)

answer = grid[39][31].cost

print("Part 1: The shortest path to 39, 31 is: {}".format(answer))

# Part 2

counter = 0

for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        if grid[y][x].cost <= 50:
            counter += 1

print("Part 2: The amount of locations that can be reached in at most 50 steps are {}".format(counter))