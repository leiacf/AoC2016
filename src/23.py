#Advent of Code 2016 Day 23

from tools import files
import time

def unwrap(a, regis):

    try:
       return int(a)
    except ValueError:
       return regis[a]
    
def toggle(input, regis, a, x):

    a = unwrap(a, regis)

    if (a+x <len(input)):
        line = input[a+x]
        split = line.split(" ")

        if len(split) == 3:
            if split[0] != "jnz":
                split[0] = "jnz"
            else:
                split[0] = "cpy"

        elif len(split) == 2:
            if split[0] != "inc":
                split[0] = "inc"
            else:
                split[0] = "dec"

        line = " ".join(split)

        input[a+x] = line

    return input

def execute(instruction, regis, x, input):

    if "cpy" in instruction or "jnz" in instruction:
        ins, a, b = instruction.split(" ")
        a = unwrap(a, regis)

    else:
        ins, a = instruction.split(" ")

    match ins:
        case "cpy":
            regis[b] = a
            x += 1
        case "inc":
            regis[a] += 1
            x += 1
        case "dec":
            regis[a] -= 1
            x += 1
        case "jnz":
            if a != 0:
                x += unwrap(b, regis)
            else:
                x += 1
        case "tgl":
            input = toggle(input, regis, a, x)
            x += 1
        case _:
            exit("Something went very wrong")

    return input, x

def parse(input, regis):

    x = 0

    while x < len(input):
        input, x = execute(input[x], regis, x, input)
                
def test():

    input = [
        "cpy 2 a",
        "tgl a",
        "tgl a", 
        "tgl a", 
        "cpy 1 a",
        "dec a",
        "dec a"
    ]

    return input

def part1(input):

    #input = test()
    regis = {"a": 7, "b": 0, "c": 0, "d": 0, "e": 0}
    parse(input, regis)

    print("Part 1: The value we should send to the safe is {}".format(regis["a"]))

def part2(input):

    input = files.input_as_list(filename)
    regis = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0}
    parse(input, regis)

    print("Part 2: The value we should send to the safe is {}".format(regis["a"]))

filename = "input/23.txt"
input = files.input_as_list(filename)

print()

start1 = time.perf_counter()
part1(input)
end1 = time.perf_counter()

start2 = time.perf_counter()
part2(input)
end2 = time.perf_counter()

print()
print("Spent {:>7.2f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.2f} seconds on Part 2".format(end2-start2))