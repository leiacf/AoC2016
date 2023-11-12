#Advent of Code 2016 Day 6

from tools import files

def count_letters_in_string(word):

    letters = {}

    for letter in word:

        if letter in letters:
            letters[letter] += 1

        else: 
            letters[letter] = 1

    return sorted(letters.items(), key=lambda item: [-item[1], item[0]])

def create_columns(input):
    
    strings = []

    for x in range(0, len(input[0])):
        
        letters = [word[x] for word in input]
        strings.append("".join(letters))    

    return strings

def find_message_part1(columns):

    message = ""

    for column in columns:

        letters = count_letters_in_string(column)
        message += str(letters[0][0])

    return message

def find_message_part2(columns):

    message = ""

    for column in columns:

        letters = count_letters_in_string(column)
        message += str(letters[len(letters)-1][0])

    return message

filename = "input/06.txt"
input = files.input_as_list(filename)

#input = ["eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", 
#         "sdttsa", "rasrtv", "nssdts", "ntnada", "svetve", "tesnvt",
#         "vntsnd", "vrdear", "dvrsen", "enarar"]

# Part 1

columns = create_columns(input)

message = find_message_part1(columns)

print("Part 1: The message is: {}".format(message))

# Part 2

columns = create_columns(input)

message = find_message_part2(columns)

print("Part 2: The message is: {}".format(message))