def repeatingdecimals(input:float) ->str:
    stringInput = str(input)
    stringList = stringInput.split(".")

    integerPart = int(stringList[0])

    power = 10 ** len(stringList[1])
    denom = power - 1

    num = int(stringList[1]) + (integerPart * denom)

    return str(num) + "/" + str(denom)

print(repeatingdecimals(2.98))