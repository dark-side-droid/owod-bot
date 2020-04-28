import random 


def rolldice(numdice,difficulty):

    result = "You rolled: "
    successes = 0
    tens = 0
    ones = 0
    numdice = int(numdice)
    difficulty = int(difficulty)

    for i in range(numdice):
        roll = random.randrange(1,11)

        if roll >= difficulty:
            successes += 1
        if roll == 1:
            successes -= 1
            ones += 1
        if roll == 10 & difficulty >= 11:
            tens += 1
        if tens == 2:
            successes +=1
            tens = 0
        

        roll=str(roll)
        result += roll 
        if i != numdice-1:
            result += ", "
       
    if successes == 1 :
        successes = str(successes) + " success at difficulty " + str(difficulty)
    elif successes == 0:
        successes = str(successes)
        successes = successes.replace("0", "No successes at difficulty ") + str(difficulty) + ". Sorry"
    else:
        successes = str(successes) + " successes at difficulty " + str(difficulty)
    ones = "ones: " + str(ones)
    return result,successes,ones
    
        

def stringreplacer(text):
    text = text.replace("roll dice ", "")
    text = text.rsplit(",")
    return text

def botcommands():
    part1="""Bot Commands:
    roll dice           | e.g: roll dice 14,3

    get discipline info | e.g: get dominate 1 (up to 5)
    get sphere info     | e.g: get life 1
    auspexclash         | obfuscate and chimerstry clash of wills with auspex

    get blood bond      | details of the blood bond mechanic
    get diablerie       | details on the act of diablerie
    get spellcasting    | spellcasting and paradox modifiers

    get road list       | prints a list of all the roads the bot knows of
    get road info       | e.g get road of bones"""
    return part1

    
    
        



    

        






