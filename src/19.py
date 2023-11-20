#Advent of Code 2016 Day 19

import time

def trick(input):

    #Numberphile super trick

    binary = bin(input)
    
    binary = "0b" + binary[3:] + binary[2]
    result = int(binary, 2)

    return result

def part1(input):

    victor = trick(input)

    print("Part 1: The elf with all the presents is elf number {}".format(victor))

def part2(input):

    print("Part 2: {}".format(1))    

input = 3005290
#input = 5

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