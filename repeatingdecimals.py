def repeatingdecimals(input:float) ->str:
    stringInput = str(input)
    stringInput = stringInput[2:]

    power = 10 ** len(stringInput)
    denom = str(power - 1)
    num = stringInput
    return num + "/" + denom

print(repeatingdecimals(.98))