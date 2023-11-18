#Advent of Code 2016 Day 12

from tools import files

def unwrap(a, regis):

    if a.isnumeric():
        return int(a)
    else:
        return regis[a]

def execute(instruction, regis, x):

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
                x += int(b)
            else:
                x += 1
        case _:
            exit("Something went very wrong")

    return x

def parse(input, regis):

    x = 0

    while x < len(input):
        x = execute(input[x], regis, x)

filename = "input/12.txt"
input = files.input_as_list(filename)

# Part 1

#input = ["cpy 41 a", "inc a", "inc a", "dec a", "jnz a 2", "dec a"]
regis = { "a":0, "b":0, "c":0, "d":0}
parse(input, regis)

print("Part 1: Register a contains: {}".format(regis["a"]))

# Part 2

regis = { "a":0, "b":0, "c":1, "d":0}
parse(input, regis)

print("Part 2: Register a contains: {}".format(regis["a"]))