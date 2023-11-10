# Advent of Code 2016 Day 5

import hashlib as h

def search(input):

    done = False
    counter = 0
    hash = ""
    password = ""

    while not done:

        test = input + str(counter)
        hash = h.md5(test.encode()).hexdigest()

        if hash.startswith("00000"):
            #print("Found hash: {}".format(hash))
            password += hash[5]

        counter += 1

        if len(password) == 8:
            done = True

    return password

def search_better(input):

    done = False
    counter = 0
    hash = ""
    password = ["", "", "", "", "", "", "", ""]

    while not done:

        test = input + str(counter)
        hash = h.md5(test.encode()).hexdigest()

        if hash.startswith("00000"):
            #print("Found hash: {}".format(hash))
            
            try:
                index = int(hash[5])
                insert = hash[6]
                if index < len(password) and password[index] == "":
                    password[index] = insert
            except ValueError:
                pass
            finally:
                pass

        counter += 1

        if all(element != "" for element in password):        
            done = True

    return "".join(password)

input = "ffykfhsq"
#input = "abc"

# Part 1

password = search(input)
print("Part 1: The password is {}".format(password))


# Part 2

password = search_better(input)
print("Part 1: The password is {}".format(password))
