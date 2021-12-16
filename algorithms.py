import parseLabyrinthBasic
from nodes import Nodes
import math


totalnodes = 0
expandCounter = 1
global labyrinth, totalLines, totalColumns

def makeQueue(node):
    """
    Βρισκει τι διαθέσιμες κινήσεις μπορουμε να κάνουμε απο την κατάσταση του node και τις βάζει στην ουρα,
    επίσης χρησιμοποιείται και για επέκταση (all-in-one).
    :param node: nodes, Κόμβος που θα επεκταθεί
    :param tmpQueue: πίνακας, Ουρά οπου θα αποθυκευτούν οι νέοι κομβοι
    """
    global totalnodes
    tmpQ = []
    i = node.state[0]
    j = node.state[1]
    print("expanding node:", node.state, "to")

    if (i + 1 < totalLines and labyrinth[i + 1][j] != "X"):
        tmpNode = Nodes([i + 1, j], node, node.cost, node.depth, labyrinth[i + 1][j])  # moved "down"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "fathernode:",
                  node.state)
        del tmpNode

    if (j + 1 < totalColumns and labyrinth[i][j + 1] != "X"):
        tmpNode = Nodes([i, j + 1], node, node.cost, node.depth, labyrinth[i][j + 1])  # moved "right"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "fathernode:",
                  node.state)
        del tmpNode

    if (i - 1 >= 0 and labyrinth[i - 1][j] != "X"):
        tmpNode = Nodes([i - 1, j], node, node.cost, node.depth, labyrinth[i - 1][j])  # moved "up"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "fathernode:",
                  node.state)
        del tmpNode

    if (j - 1 >= 0 and labyrinth[i][j - 1] != "X"):
        tmpNode = Nodes([i, j - 1], node, node.cost, node.depth, labyrinth[i][j - 1])  # moved "left"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "fathernode:",
                  node.state)
        del tmpNode

    totalnodes += len(tmpQ)
    return tmpQ


def UCS(labyrinthName):
    global totalnodes, labyrinth, totalLines, totalColumns
    [labyrinth, totalLines, totalColumns] = parseLabyrinthBasic.parseLabyrinth(labyrinthName)
    previouslyvisited = []
    startNode = Nodes([0, 0],
                      Nodes([-1, -1], [-1, -1], -1, -1, "null"),  # Για fathernode εχουμε ενα ακομη πιο startnode
                      0, 0, "S")
    queue = makeQueue(startNode)
    totalnodes += 1
    previouslyvisited.append(startNode)
    # quepos = 1
    tmpNode = queue[0]
    repeats = 0  # prosorino, to ebales gia na exeis ligotera prints
    while (tmpNode.value != 'G'):
        queue.extend(makeQueue(tmpNode))  # παίρνει την μια λιστα που που φτιάχνει η makeQueue και την βάζει
        # στο τέλος της queue
        # queue+=makeQueue(tmpNode))
        previouslyvisited.append(queue.pop(0))  # Αφαιρήται απο την ουρα ο κόμβος που αναπτήχθηκε ->
        queue = sorted(queue, key=lambda Nodes: Nodes.cost)
        tmpNode = queue[0]  # -> Και μπαίνει να αναπτήξει τον επόμενο
        # quepos += 1
        repeats += 1

    goalNode = tmpNode
    return goalNode, previouslyvisited, repeats, totalnodes


def IDS(labyrinthName):
    global totalnodes, expandCounter, labyrinth, totalLines, totalColumns
    [labyrinth, totalLines, totalColumns] = parseLabyrinthBasic.parseLabyrinth(labyrinthName)
    previouslyvisited = []
    startNode = Nodes([0, 0],
                      Nodes([-1, -1], [-1, -1], -1, -1, "null"),  # Για fathernode εχουμε ενα ακομη πιο startnode
                      0, 0, "S")
    # Base DFS:
    # tmpNode = startNode
    # repeats = 0  # prosorino, to ebales gia na exeis ligotera prints
    # while (tmpNode.value != 'G' and repeats<10):
    #     queue = makeQueue(tmpNode) + queue  # τα νέα παιδιά μπαινουν στην αρχή της ουρας
    #     tmpNode = queue[0]
    #     previouslyvisited.append(queue.pop(0))
    #     repeats += 1
    """ Κάτι παιχτηκε εδώ, δεν ξέρω με τι λογική το έκανα, αλλά νομίζω δουλεύει, βάλε μικρό οριο repeats στο πρωτο 
        while, και δες πραγματικά αν ειναι IDS, αλλά κατι πολύ λάθος πάει με την previusly και τα total nodes
        
        Το repeats ειναι λάθος εδώ μιας και μετράει την εξωτερική λούπα, ενώ η επέκταση γίνεται στην εσωτερική """
    # ΠΟΛΥ ΣΗΜΑΝΤΙΚΟ: queue=makequeue()+queue
    repeats = 0
    depthLimit = 1
    tmpNode = startNode  # μια φορά εδω μόνο και μόνο για το εξωτερικό while
    while(tmpNode.value != 'G'):
        previouslyvisited = []  # αρχικοποίηση καθέ φορα που αυξάνεται το όριο
        queue = []
        expandCounter = 1
        totalnodes = 0
        tmpNode = startNode
        while(1):  # Το while αυτό τρέχει μεχρι να αδειασει η queue ή βρουμε το G
            queue = makeQueue(tmpNode) + queue  # Επεκτήνω
            if (tmpNode.depth >= depthLimit):
                #queue.pop(0)
                print("popped:", queue.pop(0).state)  # Αν ο επόμενος κόμβος που παει να επιλεχθεί ειναι στο οριο
                # βαθους, τον βγάζουμε απο την ουρά
                if (len(queue) == 0): # redundant (δεν χρειάζεται, γινεται μετά ο ελεγχος)
                    break  # αν η ουρά αδειάσει, τότε βγαίνουμε απο την εσωτερική λουπα
            if (len(queue) == 0 or tmpNode.value == 'G'):
                break # επίσης βγαινουμε αν είμαστε στον G
            tmpNode = queue[0]  # μετά τα if, επιλέγετε κόμβος που δεν ειναι στο όριο
            previouslyvisited.append(queue.pop(0))  # προσθέτουμε τον κομβο που πήραμε να επεκτίνουμε στην previously

        depthLimit += 1
        repeats += 1

    goalNode = tmpNode
    return goalNode, previouslyvisited, repeats, totalnodes


def A_star(labyrinthName):
    global labyrinth, totalLines, totalColumns
    [labyrinth, totalLines, totalColumns] = parseLabyrinthBasic.parseLabyrinth(labyrinthName)


    def heuristic():
        # Δημηουργία 2D πίνακα με -1 για default τιμες
        heursticValues = [[int(-1) for i in range(totalColumns)] for i in range(totalLines)]
        # Εύρεση της θέσης του G
        gx = -1
        gy = -1
        for i in range(totalLines):
            for j in range(totalColumns):

                if (labyrinth[i][j] != 'G'):
                    continue
                else:
                    gx=i
                    gy=j

        # Υπολογισμός απόστασης απο κάθε σημείο εως το σημείο G
        for i in range(totalLines):
            for j in range(totalColumns):
                if (labyrinth[i][j] != 'X'):
                    xDist = (gx-i)**2
                    yDist = (gy-j)**2
                    heursticValues[i][j] = int(math.sqrt(xDist + yDist))
                    #print("x=", i, "xDist=", xDist, "y=", j, "yDist=", yDist, "dist=", heursticValues[i][j])

        # Στο τέλος η heuristic τιμή είναι αποθυκευμένη σε εναν πινακα ίδιου μεγέθους με του χαρτη
        # και μπορει να αξιοποιηθεί ως
        # (tmpNode)cost=node.cost+heuristicValues[tmpNode.state[0]][tmpNode.state[1]]
        parseLabyrinthBasic.buetyPrint(heursticValues)


    heuristic()
