# Advent of Code 2016 - Day 4

from tools import files

def count(words):

    letters = {}

    for word in words:
        for letter in word:

            if letter in letters:
                letters[letter] += 1

            else: 
                letters[letter] = 1

    tuples = sorted(letters.items(), key=lambda item: [-item[1], item[0]])

    checksum = ""

    for key in tuples:
        checksum += key[0]

    return checksum[0:5]

def decrypt(words, rot):

    rot = int(rot) % 26
    rot_words = []

    for word in words:

        ascii = [ord(letter)+rot-26 if ord(letter)+rot > 122 else ord(letter)+rot for letter in word]
        letters = [chr(letter) for letter in ascii]
    
        rot_words.append("".join(letters))

    return " ".join(rot_words)

filename = "input/04.txt"

input = files.input_as_list(filename)

# Part 1

sum = 0

for line in input:

    words = line.split("-")
    id, checksum = words.pop(len(words)-1).split("[")
    checksum = checksum[:-1]

    check = count(words)

    if checksum == check:
        sum += int(id)

print("Part 1: The sum of all sector id's is {}".format(sum))

# Part 2

for line in input:

    words = line.split("-")
    id, checksum = words.pop(len(words)-1).split("[")
    checksum = checksum[:-1]

    check = count(words)

    if checksum == check:
        decrypted = decrypt(words, id)

        if "north" in decrypted:
            print("Part 2: The sector id of the north pole storange is {}".format(id))