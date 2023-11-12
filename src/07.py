#Advent of Code 2016 Day 7

from tools import files
import re

def abas(words):

    abas = []

    for word in words:

        for x in range(0, len(word)-2):
            if word[x] == word[x+2] and word[x] != word[x+1]:
                abas.append(word[x:x+3])

    return abas

def babs_as_abas(words):

    abas = []

    for word in words:

        for x in range(0, len(word)-2):
            if word[x] == word[x+2] and word[x] != word[x+1]:
                aba = word[x+1] + word[x] + word[x+1]
                abas.append(aba)

    return abas

def has_pair(words):

    for word in words:
        for x in range(0, len(word)-3):

            if word[x] == word[x+3] and word[x+1] == word[x+2] and word[x] != word[x+1]:
                return True

    return False

def supports_tls(string):

    outside = re.split('\[.*?\]', string)
    inside = [word[1:-1] for word in re.findall('\[.*?\]', string)]
    
    if has_pair(inside):
        return False
    
    if has_pair(outside):
        return True
        
    return False

def supports_ssl(string):

    outside = re.split('\[.*?\]', string)
    inside = [word[1:-1] for word in re.findall('\[.*?\]', string)]
    
    aba = abas(outside)
    bab = babs_as_abas(inside)

    for element in aba:
        if element in bab:
            return True

    return False

filename = "input/07.txt"
input = files.input_as_list(filename)

# Part 1

#input = ["abba[mnop]qrst", "abcd[bddb]xyyx", "aaaa[qwer]tyui", "ioxxoj[asdfgh]zxcvbn"]

counter = 0

for string in input:

    if supports_tls(string):
        counter += 1

print("Part 1: The amount of IPs that support TLS are {}".format(str(counter)))

# Part 2

#input = ["aba[bab]xyz", "xyx[xyx]xyx", "aaa[kek]eke", "zazbz[bzb]cdb"]

counter = 0

for string in input:

    if supports_ssl(string):
        counter += 1

print("Part 2: The amount of IPs that support SSL are {}".format(str(counter)))