#Advent of Code 2016 Day 10

from tools import files
from tools import bot
import re

def parse(input):

    rules = []
    actions = []

    for line in input:
        if line.startswith("bot"):
            rules.append(line)

        elif line.startswith("value"):
            actions.append(line)

    return rules, actions

def createBots(rules):

    bots = []
    outputs = {}

    for rule in rules:
       
       instructions = re.split(" gives low to | and high to ", rule)  
       
       temp = bot.Bot(instructions)
       bots.append(temp)
       
       for element in instructions:
           if "output" in element:
                outputs[element] = 0

    return bots, outputs

def followRules(bot, bots, outputs):

    highdir = int(bot.highdirection.split(" ")[1])
    lowdir = int(bot.lowdirection.split(" ")[1])

    if "bot" in bot.highdirection:
        for b in bots:
            if b.number == highdir:
                b.getChip(bot.high)
                break

    elif "output" in bot.highdirection:
        outputs[bot.highdirection] = bot.high

    if "bot" in bot.lowdirection:
        for b in bots:
            if b.number == lowdir:
                b.getChip(bot.low)
                break

    elif "output" in bot.lowdirection:
        outputs[bot.lowdirection] = bot.low
    
    bot.removeChip(bot.low)
    bot.removeChip(bot.high)

    return outputs

def takeAction(actions, bots, search1, search2, outputs):
    
    for action in actions:
        chip, number = (int(a) for a in re.split(" goes to bot ", action[6:]))

        for bot in bots:

            if bot.number == number:
                bot.getChip(chip)
                if bot.hasChips():
                    if bot.low == search1 and bot.high == search2:
                        return bot.number
                break

    changed = True
    amount = 0

    while changed:

        for bot in bots:
            if bot.hasChips():
                if bot.low == search1 and bot.high == search2:
                    return bot.number
                outputs = followRules(bot, bots, outputs)
                amount += 1

        if amount > 0:
            changed = True
            amount = 0
        else:
            changed = False

    return -1

def multiplyActions(actions, bots, outputs):

    for action in actions:
        chip, number = (int(a) for a in re.split(" goes to bot ", action[6:]))

        for bot in bots:

            if bot.number == number:
                bot.getChip(chip)
                break

    outputs = update(bots, outputs)

    return outputs

def update(bots, outputs):

    changed = True
    amount = 0

    while changed:

        for bot in bots:
            if bot.hasChips():
                outputs = followRules(bot, bots, outputs)
                amount += 1

        if amount > 0:
            changed = True
            amount = 0
        else:
            changed = False

    return outputs


filename = "input/10.txt"
input = files.input_as_list(filename)

# Part 1

#input = ["value 5 goes to bot 2", 
#         "bot 2 gives low to bot 1 and high to bot 0", 
#         "value 3 goes to bot 1", 
#         "bot 1 gives low to output 1 and high to bot 0", 
#         "bot 0 gives low to output 2 and high to output 0", 
#         "value 2 goes to bot 2"]

rules, actions = parse(input)
bots, outputs = createBots(rules)

answer = takeAction(actions, bots, 17, 61, outputs)

print("Part 1: The bot comparing the two numbers is bot {}".format(answer))

# Part 2

rules, actions = parse(input)
bots, outputs = createBots(rules)

outputs = multiplyActions(actions, bots, outputs)

answer = outputs["output 0"] * outputs["output 1"] * outputs["output 2"]

print("Part 2: The values of the multiplied outputs are {}".format(answer))