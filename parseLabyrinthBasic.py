def parseLabyrinth(file):
    """
    :param file: onoma arxeiou (prepei na einai ston fakelo) (string)
    :return: [pinakas[], int sinolikes grammes, int sinolikes stiles]
    """
    inputFile = open(file, "r")

    totalLines = 0
    for i in inputFile:
        totalLines += 1
    inputFile.seek(0)  # to seek xreiazetai giati i loupa pige ton kersora sto telos tou arxeioy
    # (idiaiterotita tis pyhton)
    print("Total lines of the file:", totalLines)

    totalCols = len(inputFile.readline()) - 1
    inputFile.seek(0)
    print("Total columns of the file(line):", totalCols)
    # to -1 eiani giati h len() metraei kai to \n

    labyrinth = [['E' for x in range(totalCols)] for y in range(totalLines)]
    # Auto gemizei ton pinaka me 'E' (E gia empty)

    lineCounter = 0
    for line in inputFile:
        colCounter = 0  # mesa stin for gia na kanei reset kathe grammi
        for char in line:
            if (char == '\n'):  # ta if einai perita, einai gia morfopoihsh
                continue
            elif (char == ''):
                labyrinth[lineCounter][colCounter] = ' '
            else:
                labyrinth[lineCounter][colCounter] = char
            # print(lineCounter,colCounter,c,labyrinth[lineCounter][colCounter])
            colCounter += 1
        lineCounter += 1

    inputFile.close()
    return [labyrinth, totalLines, totalCols]


def buetyPrint(labyrinth):
    """
    :param labyrinth: o pinakas
    :return: print
    """
    # Gia omorgo print
    totalLines = len(labyrinth)
    totalCols = len(labyrinth[0])
    for i in range(totalLines):
        for j in range(totalCols):
            print(labyrinth[i][j], '|' ,end='')
        print('\n', end='')
