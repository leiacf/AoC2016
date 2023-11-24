#Advent of Code 2016 Day 21

from tools import files
import time


def swap(rule, scramble):

    scrambled = ""

    if "position" in rule:

        rule = rule.replace("swap position ", "")
        rule = rule.replace(" with position", "")

        x, y = [int(a) for a in(rule.split(" "))]

    elif "letter" in rule:

        rule = rule.replace("swap letter ", "")
        rule = rule.replace(" with letter", "")

        a, b = rule.split(" ")

        x = scramble.index(a)
        y = scramble.index(b)

    if x > y:
        c = x
        x = y
        y = c

    if x > 0:
        scrambled += scramble[0:x]
    scrambled += scramble[y]
    scrambled += scramble[x+1: y]
    scrambled += scramble[x]
    if y < len(scramble)-1:
        scrambled += scramble[y+1:]

    return scrambled

def rot(string, dir):

    rotated = ""

    if dir == "l":

        rotated += string[1:]
        rotated += string[0]

    elif dir == "r":

        rotated += string[-1]
        rotated += string[0:-1]
        

    return rotated

def rotate(rule, scramble):

    scrambled = scramble
    x = 0
    dir = "r"
    
    if "based on" in rule:
        
        dir = "r"
    
        a = rule[-1]
        x = scramble.index(a)

        if (x >= 4):
            x += 1

        x = x+1

    elif "step" in rule:

        if "left" in rule:
            rule = rule.replace("rotate left ", "")
            dir = "l"
    
        elif "right" in rule:
            rule = rule.replace("rotate right ", "")
            dir = "r"
    
        rule = rule.replace(" steps", "")
        rule = rule.replace(" step", "")
        x = int(rule)

    for i in range(0, x):
        scrambled = rot(scrambled, dir)

    return scrambled

def rotate_back(rule, scramble):

    scrambled = scramble
    
    if "based on" in rule:
        
        dir = "l"

        for i in range(0, len(scrambled)+2):
            scrambled = rot(scrambled, dir)
            test = rotate(rule, scrambled)
        
            if scramble == test:
                return scrambled

    elif "step" in rule:

        if "left" in rule:
            rule = rule.replace("rotate left ", "")
            dir = "r"
    
        elif "right" in rule:
            rule = rule.replace("rotate right ", "")
            dir = "l"
    
        rule = rule.replace(" steps", "")
        rule = rule.replace(" step", "")
        x = int(rule)

        for i in range(0, x):
            scrambled = rot(scrambled, dir)

    return scrambled

def reverse(rule, scramble):

    rule = rule.replace("reverse positions ", "")
    rule = rule.replace(" through", "")

    x, y = [int(a) for a in(rule.split(" "))]

    scrambled = ""

    scrambled += scramble[0:x]

    for i in range(y, x-1, -1):
        scrambled += scramble[i]

    scrambled += scramble[y+1:]

    return scrambled

def move(rule, scramble, two=False):

    scrambled = ""

    rule = rule.replace("move position ", "")
    rule = rule.replace("to position ", "")

    x, y = [int (a) for a in rule.split(" ")]

    if two:
        z = x
        x = y
        y = z

    if (x > y):
        
        scrambled += scramble[0:y]
        scrambled += scramble[x]
        scrambled += scramble[y:x]
        scrambled += scramble[x+1:]

    else: 

        scrambled += scramble[0:x]
        scrambled += scramble[x+1:y+1]
        scrambled += scramble[x]
        scrambled += scramble[y+1:]

    return scrambled

def test():

    input = [
            "swap position 4 with position 0",
            "swap letter d with letter b",
            "reverse positions 0 through 4",
            "rotate left 1 step",
            "move position 1 to position 4",
            "move position 3 to position 0",
            "rotate based on position of letter b",
            "rotate based on position of letter d"
    ]

    scramble = "abcde"

    return input, scramble

def part1(input, scramble):

    input, scramble = test()
    result = scramble

    for line in input:
        
        word = line.split(" ")[0]
        
        match word:
            case "swap":
                result = swap(line, result)
            case "rotate":
                result = rotate(line, result)
            case "move":
                result = move(line, result)
            case "reverse":
                result = reverse(line, result)
            case _:
                exit("Something went wrong")  

    print("Part 1: {}".format(result))

def part2(input):

    #input, scramble = test()
    #scramble = "decab"

    input.reverse()
    result = scramble

    for line in input:
        
        word = line.split(" ")[0]
        
        match word:
            case "swap":
                result = swap(line, result)
            case "rotate":
                result = rotate_back(line, result)
            case "move":
                result = move(line, result, True)
            case "reverse":
                result = reverse(line, result)
            case _:
                exit("Something went wrong")  

    print("Part 2: {}".format(result))    

filename = "input/21.txt"
input = files.input_as_list(filename)
scramble = "abcdefgh"

print()

start1 = time.perf_counter()
part1(input, scramble)
end1 = time.perf_counter()

scramble = "fbgdceah"

start2 = time.perf_counter()
part2(input)
end2 = time.perf_counter()

print()
print("Spent {:>7.2f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.2f} seconds on Part 2".format(end2-start2))