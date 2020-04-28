def doWork(card,frequencies):
    printStr = ""
    numRequired = 3 - (9-len(card))
    for x in range(len(prizes)):
        for y in range(len(card)):
            if card[y] == prizes[x]:
                frequencies[x] = frequencies[x] + 1
    for x in range(len(frequencies)):
        if frequencies[x] == 3:
            printStr = "$" + str(prizes[x])
            break
        if frequencies[x] >= numRequired:
            printStr = printStr + "$" + str(prizes[x]) + " "
    if printStr != "":
        print(printStr)
    else:
        print("No Prizes Possible")




prizes = [1,2,5,10,50,100,1000,10000,500000,1000000]
file = open("C:\python\ECOOCS_2014\ECOO 2014 Round 2\data\DATA11.txt", "r")
card = []
counter = 1
for x in file:
    frequencies = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x = x.strip("\n")
    x = x.strip("$")
    if x.isnumeric():
        card.append(int(x))
    if counter%9 == 0:
        doWork(card,frequencies)
        frequencies = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        card = []
    counter += 1
