#Advent of Code 2016 Day 14

import hashlib
import time

def createMd5(salt, number):
    return hashlib.md5((salt+str(number)).encode()).hexdigest()

def check(md5, salt, number):

    found = False
    valid = False
    check = ""

    for letter in range(0, len(md5)-2):
        if md5[letter] == md5[letter+1] == md5[letter+2]:
            found = True
            check = md5[letter]
            break

    if found:
        for x in range(number+1, number + 1 + 1000):
            test = createMd5(salt, x)

            if check*5 in test:
                valid = True
                break
                        
    return valid

def stretch(md5, amount):

    if md5 in stretched:
        return stretched[md5]
    
    new = md5

    for x in range(0, amount):
        new = createMd5(new, "")

    stretched[md5] = new

    return new

def check_stretch(md5, salt, number):

    found = False
    valid = False
    check = ""

    for letter in range(0, len(md5)-2):
        if md5[letter] == md5[letter+1] == md5[letter+2]:
            found = True
            check = md5[letter]
            break

    if found:
        for x in range(number+1, number + 1 + 1000):

            test = createMd5(salt, x)
            test = stretch(test, 2016)

            if check*5 in test:
                valid = True
                break
                        
    return valid

def part1(input):

    i = 0
    counter = 0

    while counter < 65:
        test = createMd5(input, i)
        
        if check(test, input, i):
            counter += 1
        
        if counter == 64:
            break

        i += 1

    print("Part 1: The index that creates the 64th key is {}".format(i))

def part2(input):

    i = 0
    counter = 0
    
    while counter < 65:
        
        test = createMd5(input, i)
        test = stretch(test, 2016)
        
        if check_stretch(test, input, i):
            counter += 1
        
        if counter == 64:
            break

        i += 1

    print("Part 2: The index that creates the 64th key is {}".format(i))

print()

input = "yjdafjpo"
stretched = {}

start1 = time.perf_counter()
part1(input)
end1 = time.perf_counter()

start2 = time.perf_counter()
part2(input)
end2 = time.perf_counter()

print()
print("Spent {:>7.2f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.2f} seconds on Part 2".format(end2-start2))