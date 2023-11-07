def open_input(filename):

    f = open(filename, "r")

    return f.read()

def open_input_several(filename):

    f = open(filename, "r")

    return f.readlines()