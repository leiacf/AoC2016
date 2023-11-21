#Advent of Code 2016 Day 20

from tools import files
import time

def parse(input):

    all = []

    for x in range(0, len(input)):
        all.append([int(a) for a in input[x].split("-")])
    
    all.sort()

    return all

def calculate(all):
    
    for x in range(0, len(all)-1):

        if x >= len(all)-1:
            break

        start, end = all[x]
        first, last = all[x+1]

        if end < first:
           
            if end+1 == first:

                del all[x+1]
                all[x] = [start, last]

            else: 
                pass

        elif end >= first:

            if end > last:
                del all[x+1]
            
            elif end <= last:
            
                if start > first:
                    del all[x]
                    x -= 1
            
                elif start <= first:
                    del all[x+1]
                    all[x] = [start, last]
                    
    return all

def allowed(all):

    yes = []

    for x in range(0, len(all)-1):

        end = all[x][1]
        last = all[x+1][0]

        for y in range(end+1, last):
            yes.append(y)

    return len(yes)


def lowest(input):

    return input[0][1] + 1

def part1(input):

    all = parse(input)
    last = len(all)
    this = 0
    
    while last != this:
        
        last = len(all)
        all = calculate(all)
        this = len(all)

    low = lowest(all)

    print("Part 1: The lowest number that isn't blocked is {}".format(low))

def part2(input):

    all = parse(input)
    last = len(all)
    this = 0
    
    while last != this:
        
        last = len(all)
        all = calculate(all)
        this = len(all)

    allow = allowed(all)

    print("Part 2: The amount of allowed ip's are {}".format(allow))    

filename = "input/20.txt"
input = files.input_as_list(filename)
#input = [ "5-8", "0-2", "4-7"]
        

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