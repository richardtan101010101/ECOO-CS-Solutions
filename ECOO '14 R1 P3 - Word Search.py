


def replace(chr, times):
    str = ""
    for i in range(times):
        str = str + chr
    return str


def isStringInList(words, list1):
    strList = str(list1)
    strList = strList.replace("[", "")
    strList = strList.replace("]", "")
    strList = strList.replace(",", "")
    strList = strList.replace("'", "")
    strList = strList.replace(" ", "")
    for myString in words:
        if myString in strList:
            strList = strList.replace(myString, replace("*", len(myString)))
    strList = strList[::-1]
    for myString in words:
        if myString in strList:
            strList = strList.replace(myString, replace("*", len(myString)))
    strList = strList[::-1]
    return strList


def mainFunc(height, width, board, words, resultBoard1, resultBoard2, diagonalBoard1, diagonalBoard2):

    for x in range(height):
        resultBoard1[x] = isStringInList(words, board[x])
    for x in range(width):
        column = []
        for y in range(height):
            column.append(board[y][x])
        printColumn = ""
        for y in range(height):
            printColumn = printColumn + isStringInList(words, column)[y]
        resultBoard2[x] = printColumn

    leftToRightDiag = ""
    for x in range(height):
        diagonal1 = ""
        i = x
        j = 0
        while i >= 0:
            diagonal1 = diagonal1 + board[i][j]
            i -= 1
            j += 1
        leftToRightDiag = leftToRightDiag + diagonal1
    for x in range(1, width):
        diagonal2 = ""
        i = height - 1
        j = x
        while j <= width - 1:
            diagonal2 = diagonal2 + board[i][j]
            i -= 1
            j += 1
        leftToRightDiag = leftToRightDiag + diagonal2

    leftToRightDiag = isStringInList(words,leftToRightDiag)


    RightToLeftDiag = ""
    for x in range(height-1):
        diagonal3 = ""
        j = width - 1
        i = x
        while i >= 0:
            diagonal3 = diagonal3 + board[i][j]
            j -= 1
            i -= 1

        RightToLeftDiag = RightToLeftDiag + diagonal3

    x = width - 1
    while x >= 0:
        diagonal4 = ""
        j = x
        i = height - 1
        while j >= 0:
            diagonal4 = diagonal4 + board[i][j]
            i -= 1
            j -= 1
        RightToLeftDiag = RightToLeftDiag + diagonal4

        x -= 1
    RightToLeftDiag = isStringInList(words,RightToLeftDiag)


    #create final diagonal boards
    counter = -1
    for x in range(height):
        i = x
        j = 0
        while i >= 0:
            counter += 1
            diagonalBoard1[i][j] = leftToRightDiag[counter]
            i -= 1
            j += 1
    for x in range(1, width):
        i = height - 1
        j = x
        while j <= width - 1:
            counter += 1
            diagonalBoard1[i][j] = leftToRightDiag[counter]
            i -= 1
            j += 1

    counter = -1
    for x in range(height-1):
        j = width - 1
        i = x
        while i >= 0:
            counter += 1
            diagonalBoard2[i][j] = RightToLeftDiag[counter]
            j -= 1
            i -= 1

    x = width - 1
    while x >= 0:
        j = x
        i = height - 1
        while j >= 0:
            counter += 1
            diagonalBoard2[i][j] = RightToLeftDiag[counter]
            i -= 1
            j -= 1
        x -= 1

    for x in range(height):
        board[x] = list(board[x])
        resultBoard1[x] = list(resultBoard1[x])
        resultBoard2[x] = list(resultBoard2[x])
    for x in range(height):
        for y in range(width):
            if resultBoard1[x][y] == "*":
                board[x][y] = "*"
    for x in range(width):
        for y in range(height):
            if resultBoard2[y][x] == "*":
                board[x][y] = "*"

    for x in range(width):
        for y in range(height):
            if diagonalBoard1[x][y] == "*":
                board[x][y] = "*"
    for x in range(width):
        for y in range(height):
            if diagonalBoard2[x][y] == "*":
                board[x][y] = "*"
    printWord = ""
    for x in range(height):
        for y in range(width):
            if board[x][y] != "*":
                printWord = printWord + board[x][y]
    print(printWord)


file = open("C:\python\ECOOCS_2014\ECOO 2014 Round 1\data\DATA30.txt", "r")
counter = 0
width = 0
height = 0
wordNum = 0
board = []
words = []
isWords = False
resultBoard1 = []
resultBoard2 = []
diagonalBoard1 = []
diagonalBoard2 = []
for x in file:
    x = x.strip("\n")
    if x[0].isalpha():
        x = x.replace(" ", "")
        if isWords == False:
            board.append(x)
            resultBoard1.append(x)
            resultBoard2.append(x)
            diagonalBoard1.append(list(x))
            diagonalBoard2.append(list(x))
        else:
            words.append(x)
    else:
        x = x.split(" ")
        if len(x) == 1:
            wordNum == int(x[0])
            wordNum == int(x[0])
            isWords = True
        else:
            if counter != 0:
                mainFunc(height, width, board, words, resultBoard1, resultBoard2, diagonalBoard1, diagonalBoard2)
            height = int(x[1])
            width = int(x[0])
    counter += 1
mainFunc(height, width, board, words, resultBoard1, resultBoard2, diagonalBoard1, diagonalBoard2)
