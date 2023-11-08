# Advent of Code 2016 Day 3

from tools import files

def is_invalid(a, b, c):
    return (a + b <= c) or (a + c <= b) or (b + c <= a)

filename = "input/03.txt"
input = files.input_as_list(filename)

# Part 1

counter = 0

for line in input:
    a, b, c = [int(i) for i in line.split()]

    if is_invalid(a, b, c):
        counter += 1

print("Part 1 The number of valid triangles are {}".format(len(input) - counter))

# Part 2

counter = 0

for x in range(0, len(input), 3):
    a, d, g = [int(j) for j in input[x+0].split()]
    b, e, h = [int(j) for j in input[x+1].split()]
    c, f, i = [int(j) for j in input[x+2].split()]

    if is_invalid(a, b, c):
        counter += 1

    if is_invalid(d, e, f):
        counter += 1

    if is_invalid(g, h, i):
        counter += 1

print("Part 2: The number of valid triangles are {}".format(len(input) - counter))