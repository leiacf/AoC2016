#Advent of Code 2016 Day 16

import time

def flip(b):

    flipped = ""

    for letter in b:
        if letter == "0":
            flipped += "1"
        else:
            flipped += "0"

    return flipped

def reverse(b):

    reversed = ""

    for x in range(len(b)-1, -1, -1):
        reversed += b[x]

    return reversed
    
def generate(a):

    b = a
    b = reverse(b)
    b = flip(b)

    return a + "0" + b

def calculate(output):
    
    checksum = ""

    for x in range(0, len(output), 2):
        if output[x] == output[x+1]:
            checksum += "1"
        else:
            checksum += "0"

    return checksum

def part1(input, length, part):

    output = generate(input)

    while len(output) < length:
        output = generate(output)

    output = output[:length]
    checksum = calculate(output)

    while len(checksum) % 2 == 0:
        checksum = calculate(checksum)

    print("Part {}: The checksum is {}".format(part, checksum))

input = "11101000110010100"

print()

start1 = time.perf_counter()
part1(input, 272, 1)
end1 = time.perf_counter()

start2 = time.perf_counter()
part1(input, 35651584, 2)
end2 = time.perf_counter()

print()
print("Spent {:>7.2f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.2f} seconds on Part 2".format(end2-start2))