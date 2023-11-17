#Advent of Code 2016 Day 9

from tools import files

def decompress_string(line):

    output = ""
    position = 0
    
    if "(" in line:

        while "(" in line[position:]:

            start = line.find("(", position)
            end = line.find(")", start)

            repeat, times = (int(a) for a in line[start+1:end].split("x"))

            if (position != start):
                output += line[position:start]

            output += line[end+1:end+1+repeat] * times

            position = end+1+repeat
        
    else:

        output += line[position:]
        
    return output

def decompress(input):

    decompressed = []
    
    for line in input:
        
        output = decompress_string(line)
        decompressed.append(output)

    return decompressed        

def calculate(line):

    sum = 0
    position = 0

    if "(" in line:

        while "(" in line[position:]:

            start = line.find("(", position)
            end = line.find(")", start)

            repeat, times = (int(a) for a in line[start+1:end].split("x"))

            if (position != start):
                sum += start - position

            output = line[end+1:end+1+repeat] * times

            sum += calculate(output)

            position = end+1+repeat

        if (position != len(line)):
            sum += len(line[position:])

    else:
        sum = len(line)

    return sum


filename = "input/09.txt"
input = files.input_as_list(filename)

#Part 1

#Testinput
#input = ["ADVENT", "A(1x5)BC", "(3x3)XYZ", "A(2x2)BCD(2x2)EFG", "(6x1)(1x3)A", "X(8x2)(3x3)ABCY"]

decompressed = decompress(input)
length = 0

for line in decompressed:
    length += len(line)

print("Part 1: The decompressed length is {}".format(length))

#Part 2

#Testinput
#input = ["ABCDEFGH"] 
#input = ["(3x3)XYZ"]
#input = ["ABC(1x2)A"]
#input = ["ABC(1x2)AB"]
#input = ["(6x1)(1x1)A"]
#input = ["X(8x2)(3x3)ABCY"] 
#input = ["(27x12)(20x12)(13x14)(7x10)(1x12)A"]
input = ["(3x3)XYZ", "X(8x2)(3x3)ABCY", "(27x12)(20x12)(13x14)(7x10)(1x12)A", "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"]

length = 0

for line in input:
    length += calculate(line)

print("Part 2: The decompressed length is {}".format(length))