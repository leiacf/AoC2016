#Advent of Code 2016 Day 11

from tools import files
import re

def extract(line):

    if "nothing relevant" in line:
        return []

    line = line[line.find("contains a ")+len("contains a "):]
    line = line.strip(".")
    line = line.replace(",", "")

    return re.split(" and a | a ", line)

def parse(input):

    floorplan = []

    for line in input:
        floorplan.append(extract(line))

    return floorplan

def show(floorplan):

    for floor in floorplan:
        
        if floor == []:
            print("|")

        for room in floor:
            print("| {} |".format(room), end="")

        print()

filename = "input/11.txt"
input = files.input_as_list(filename)

# Part 1

input = [   
            "The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.",
            "The second floor contains a hydrogen generator.",
            "The third floor contains a lithium generator.",
            "The fourth floor contains nothing relevant."
        ]

floorplan = parse(input)
show(floorplan)


print("Part 1: {}".format(1))

# Part 2


print("Part 2: {}".format(2))