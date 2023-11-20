#Advent of Code 2016 Day 15

from tools import files

def test(slots, time):

    temp = []

    for slot in slots:
        temp.append([slot[0], slot[1], (slot[0]+time+slot[2]) % slot[1]])

    return temp

def parse(input):

    slots = []

    for line in input:

        line = line.replace("Disc #", "")
        line = line.replace(" has", "")
        line = line.replace(" positions; at time=0, it is at position ", " ")
        line = line.replace(".", "")
        slots.append([int(x) for x in line.split(" ")])

    return slots

filename = "input/15.txt"
input = files.input_as_list(filename)

#input = ["Disc #1 has 5 positions; at time=0, it is at position 4.", "Disc #2 has 2 positions; at time=0, it is at position 1."]

# Part 1

slots = parse(input)

counter = 0

for time in range(0, 100000000):

    temp = test(slots, time)

    for slot in temp:
        if slot[2] == 0:
            counter += 1
    
    if counter == len(temp):
        break

    counter = 0

print("Part 1: The starting point is at time {}".format(time))

# Part 2

slots = parse(input)
slots.append([len(input)+1, 11, 0])

counter = 0

for time in range(0, 100000000):

    temp = test(slots, time)

    for slot in temp:
        if slot[2] == 0:
            counter += 1
    
    if counter == len(temp):
        break

    counter = 0

print("Part 2: The starting point is at time {}".format(time))