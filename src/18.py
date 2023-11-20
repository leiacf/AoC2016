#Advent of Code 2016 Day 18

from tools import files
import time

def show(grid):

    print()

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            print(grid[y][x], end= "")

        print()

    print()

def check(x):

    if x == ".":
        return "S"
    else:
        return "T"
    
def create(string):

    match string:
        case "SSS":
            return "."
        case "SST":
            return "^"
        case "STT":
            return "^"
        case "TTT":
            return "."
        case "TTS":
            return "^"
        case "TSS":
            return "^"
        case "STS":
            return "."
        case "TST":
            return "."
        case _:
            print("Something went wrong")
            exit(-1)

def calculate(grid):

    index = len(grid)-1
    row = ""

    for x in range(0, len(grid[index])):
        
        if x > 0:
            a = check(grid[index][x-1])
        else:
            a = "S"

        b = check(grid[index][x])
        
        if x < len(grid[index])-1:
            c = check(grid[index][x+1])
        else:
            c = "S"

        row += create(a+b+c)
        
    grid.append(row)

def count(grid):

    counter = 0

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == ".":
                counter += 1

    return counter

def part1(input, amount, part):

    for x in range(0, amount):
        calculate(input)
    
    safe = count(input)

    print("Part {}: The number of safe tiles are {}".format(part, safe))

filename = "input/18.txt"
input = files.input_as_list(filename)

print()

start1 = time.perf_counter()
part1(input, 39, 1)
end1 = time.perf_counter()

input = files.input_as_list(filename)

start2 = time.perf_counter()
part1(input, 399999, 2)
end2 = time.perf_counter()

print()
print("Spent {:>7.2f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.2f} seconds on Part 2".format(end2-start2))