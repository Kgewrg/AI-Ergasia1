""" Main Αρχείο 
    Εργασία 1 από τους:
    1451 Γεωργίτσαρος Κωνστατνίνος
    1530 Κωνσταντινος Παλεγκας 
    1495 Χαρίσης Κύρινας 
    1481 Καραγκιώτης Αθανάσιος 
    ta sxolia kai merika prints einai sta ellinika 
    Υλποιήθηκε σε Python 3.9 - 3.10"""
import printing
from nodes import Nodes
import random

# global τιμές
counter = 0
heuristicTable = []
labyrinth = []
totalLines = 0
totalColumns = 0

def sameValueMoves(queue):
    cost = queue[0].cost
    sameCostCounter = 0
    i = 0
    print("selected cost:", cost)
    while(queue[i].cost == cost and len(queue)-1 > i):
        sameCostCounter += 1
        i += 1

    print("states with same cost counter", sameCostCounter)
    if(sameCostCounter > 0):
        randomChoice = random.randrange(0, sameCostCounter)
        print("randomly choosed:", randomChoice)
        print("before switching")
        printing.printQueueState(queue)
        printing.printQueueCost(queue)
        queue[0], queue[randomChoice] = queue[randomChoice], queue[0]
        printing.printQueueState(queue)
    return queue




def heuristic():
    """
    Συνάρτηση να βρίσκει το heuristic σε μέγεθος του αρχικού πίνακα
    Αλλάζει global τιμές
    """
    global heuristicTable, labyrinth, totalLines, totalColumns
    # Για να ξέρει η συνάρτηση οτι η μεταβλητή Heurustic είναι global
    heuristicTable = [[] for i in range(totalLines)]
    # Φτιάχνουμε εναν 2d πίνακα με totalLines συνολικές γραμμές
    # Οι γραμμές περιέχουν άδειους πίνακες

    for i in range(totalLines):
        for j in range(totalColumns):
            heuristicTable[i].append(0)
            # Σε κάθε υπο-πίνακα προσάρτονται totalColums συνολικά μηδενικά
    gi = -1
    gj = -1
    # gi, gj Θέση στον πίνακα που βρήσκεται το G
    for i in range(totalLines):
        for j in range(totalColumns):
            if (labyrinth[i][j] != 'G'):
                continue
                # Αν σε αυτήν την θέση δεν ειναι το G, την προσπερνάμε
            else:
                gi = i
                gj = j
                # Αλλίως αποθυκεύουμε την θέση (συντεταγμένες)

    # Υλοποίηση της απόσταστης Manhattan
    for i in range(totalLines):
        for j in range(totalColumns):
            dy = abs(i - gi)
            # για κάθε στοιχείο του πίνακα μετράμε πόσα βήματα πρέπει να κάνουμε κάθετα
            dx = abs(j - gj)
            # και πόσα οριζόντια
            heuristicTable[i][j] = dx + dy
            # Στο τέλος έχουμε έναν δελυτέρο πίνακα, ίδιων διαστάσεων με τον πίνακα του λαβύρινθου
            # που περιέχει την απόσταση manhattan για κάθε κελί μέχρι το κελί του G


def makeQueue(node):
    """ Συνάρτηση που βρίσκει τις διαθέσιμες ενέργειες και τις επεκτήνει
    :param: node: αντικείμενο τύπου nodes, κομβος τον οποίο θα επεκτείνει

    :returns: πίανας με τα παιδία του κόμβου που πήρε σαν είσωδο """
    tmpQ = []  # Εδώ θα αποθυκευτούν τα παιδία του κόμβου που θα επεκταθεί
    i = node.state[0]
    j = node.state[1]
    # print("i=", i, "j=", j)

    # Για κάθε κατεύθηνση (ενέργεια) έχουμε και ξεχωριστό if
    if (i + 1 < totalLines and labyrinth[i + 1][j] != "X" and node.fathernode.state != [i + 1, j]):
        # Στο οποίο μπορούμε να μπούμε μέσα μόνο αν η ενέργεια (μετακίνηση) που πάμε να κάνουμε δεν είναι:
        #   Εκτώς ορίων του πίνακα (i + 1 < totalLines)
        #   Το κελί που θα πάμε δεν είναι αδιέξωδος (labyrinth[i + 1][j] != "X")
        #   Και η ενέργεια που θα κάνουμε δεν είναι προς τα πίσω κίνηση, δεν μας στέλνει στον πατέρα του
        #       κόμβου που επεκτείνουμε

        # Δημιουργούμε ενα προσωρινό αντικείμενο (κόμβος)
        tmpNode = Nodes([i + 1, j], node, node.cost, node.depth, labyrinth[i + 1][j], 0)  # προς τα κάτω
        # του θέτουμε το κόστος και το βάθος
        tmpNode.depth += 1
        tmpNode.cost += 1
        # Αρχικά το κοστος και το βάθος του προσωρινού κόμβου έχουν τις τιμές του κόμου-πατέρα
        #   και αυξάνονται κατα 1

        # Αυξάνουμε το πλήθος των κόμβων που επεκτάθηκαν
        nodecounter()

        # Αν ο κόμβος που πάμε να επεκτείνουμε είναι πόρτα
        if (tmpNode.value == 'D'):
            # ξανα αυξάνουμε το κόστος κατα 1 (συνολικά αυξάνεται κατα 2)
            tmpNode.cost += 1

        # Θέτουμε την heuristic τιμή για αυτόν τον κόμβο (χρησιμοποιείται μόνο στον Astar)
        tmpNode.Hvalue = heuristicTable[i + 1][j] + tmpNode.cost

        # Βάζουμε τον προσωρινό κόμβο στον πίνακα που θα επιστραφεί
        tmpQ.append(tmpNode)

        # Διαγράφουμε τον προσωρινό κόμβο
        del tmpNode

    # το μόνο που αλλάζει στα υπόλοιπα if είναι σε πια τιμή γίνεται η πράξη (i+1, j+1, κτλ)
    if (j + 1 < totalColumns and labyrinth[i][j + 1] != "X" and node.fathernode.state != [i, j + 1]):
        tmpNode = Nodes([i, j + 1], node, node.cost, node.depth, labyrinth[i][j + 1], 0)  # προς τα δεξιά
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpNode.Hvalue = heuristicTable[i][j + 1] + tmpNode.cost
        tmpQ.append(tmpNode)
        del tmpNode

    if (i - 1 >= 0 and labyrinth[i - 1][j] != "X" and node.fathernode.state != [i - 1, j]):
        tmpNode = Nodes([i - 1, j], node, node.cost, node.depth, labyrinth[i - 1][j], 0)  # προς τα πάνω
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpNode.Hvalue = heuristicTable[i - 1][j] + tmpNode.cost
        tmpQ.append(tmpNode)
        del tmpNode

    if (j - 1 >= 0 and labyrinth[i][j - 1] != "X" and node.fathernode.state != [i, j - 1]):
        tmpNode = Nodes([i, j - 1], node, node.cost, node.depth, labyrinth[i][j - 1], 0)  # προς τα αριστερά
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpNode.Hvalue = heuristicTable[i][j - 1] + tmpNode.cost
        tmpQ.append(tmpNode)
        del tmpNode

    # Στο τέλος επιστρέφουμε τον πίνακα με τα παιδία του κόμβου που εισάγαμε στην είσοδο
    return tmpQ


def backTracePath(currentNode):  #
    """
    backTracePath
    Συνάρτηση για να βρίσκουμε το μονοπάτι απο τον κόμβο στόχου πρως την αρχή
    :param currentNode: Ο τορινός κόμβος (κόμβος λύση)
    :return: ένα string με τις καταστάσεις που οδηγούν στην αρχή (μονοπάτι)
    """
    btNode = currentNode  # backTraceNode
    path = ''
    # Εκμεταλευεται το fathernode, ξεκινάμε απο τον G και πάμε στον father του (προς τα πίσω κίνηση)
    while (btNode.value != 'S'):
        path = path + str(btNode.state) + ' -> '  # κρατάμε την κατάσταση στο string αυτο
        btNode = btNode.fathernode
        # fathernode απο τον τορινο
        # ο επόμενος γίνεαι ο πατέρας του τορινού
    path = path + str(btNode.state)
    del btNode
    return path


def nodecounter():
    """
    Συνάρτηση για να μετράει τους συνολικούς κόμβους που δημιουργήθηκαν
    Αλλάζει global τιμές
    Κάθε φορά που καλείτε, αυξάνει το counter κατα 1
    """
    global counter
    counter += 1


def ucs(queue):
    """ Υλοποιήση του UCS, Επιλέγει τον κόμβο με το μικρότερο κόστος
        :param: queue, Ουρα στην οποία θα επεκτείνει (global Πινακας),
                με πρώτο στοιχείο ο κόμβος απο τον οποίο θα ξεκινήσει η επέκταση"""
    previouslyVisited = []  # Σε αυτόν τον πίνακα κρατάμε τους κόμβους που επεκτείναμε
    repeats = 1  # οι επαναληψεις που θα κάνει η while θα είναι και το πλήθος των κόμβων που επέκτεινε
    tmpNode = queue[0]  # πέρνουμε το πρώτο στοιχείου της ουρας
    #   οταν πρωτο-καλείτε είναι το start noteς

    while (tmpNode.value != 'G'):
        # Εκτύπωση πέριπου κάθε 1000 επεκτάσεις, μονο στον UCS γιατι μόνο αυτος πέρνει αισθητή ώρα εκτέλεσης
        #   περίπου γιατι σε κάθε makeQueue μπορεί να επεκταθούν απο 0 εώς και 4 κόμβοι
        if (repeats % 1000 == 0):
            print("Expanded", counter, "nodes and still searching, current node:")
            tmpNode.printclass()
        # Η while είναι αυτή που ελέγχει αν είμαστε σε κόμβο στόχου
        queue = queue + makeQueue(tmpNode)
        # Βάζουμε τα στοιχεία του πίνακα που επιστρέφει η makeQueue μετά τα στοιχεία που ήδη περιέχει ο πίνακας Queue
        previouslyVisited.append(queue.pop(0))
        # Αφαιρούμε απο την queue το στοιχείο που μόλις επεκτήναμε και ταυτόχρονα το βάζουμε στην previuslyVisited
        queue = sorted(queue, key=lambda Nodes: Nodes.cost)
        # sort της queue με βάση το κοστος των κομβων
        tmpNode = queue[0]
        # ο επόμενος κόμβος που θα επεκταθεί είναι τωρα ο επόμενος στην σειρα (2ος πριν την αφαίρεση)
        repeats += 1

    # Στο τέλος του while, το tmpNode είναι ο κόμβος στόχου, και η previuslyVisited είναι η ουρά
    previouslyVisited.append(tmpNode)
    # Μια τελευταία πρόσθαιση στην previouslyVisited, για να μπεί και ο κόβος στόχου

    print("Done, goal node data:")
    tmpNode.printclass()
    print("Total nodes created:", counter)
    print("Total nodes expaned:", repeats)
    print("Path to the GoalNode", backTracePath(tmpNode))


def ids(queue):
    """ Υλοποιήση του IDS, Επιλέγει τον κόμβο με το μικρότερο κόστος
        :param: queue, Ουρα στην οποία θα επεκτείνει (global Πινακας),
                με πρώτο στοιχείο ο κόμβος απο τον οποίο θα ξεκινήσει η επέκταση"""
    # Αρχικοποίηση μερικών τιμών
    tmpNode = queue[0]
    # Στην ουρά υπάρχει ο Star node
    maxdepth = 1
    previouslyVisited = []
    startNode = Nodes([0, 0], Nodes([-1, -1], [-1, -1], -1, -1, "null"), 0, 0, "S")
    # το startNode συγκεκριμένα χρειάζεται για να κάνουμε "Επανεκίνσηση μέσα στην while"
    repeats = 0

    while (tmpNode.value != 'G'):
        # Αφαιρούμε τον κόμβο που πάει να επεκταθεί απο την ουρά
        previouslyVisited.append(queue.pop(0))
        # Ο κόμβος που πάει να επεκταθεί ειναι στην tmpNode, οπότε μπορούμε  να τον βγάλουμε απο την ουρα
        #   πριν "ολοκληρωθεί" η επέκταση

        # Επεκτίνουμε κανονικά με DFS μεχρι να φτάσουμε στο όριο βάθους depthLimit
        while (tmpNode.depth == maxdepth):
            # Όσο οι κόμβοι που πάμε να επετκείνουμε ειναι στο οριο βάθους, τους επιλέγουμε για έλεγχο αλλά δεν
            #   επεκτείνουμε
            if (len(queue) == 0):
                # Και άμα καταλήξει η ουρά μας να μην έχει άλλους κόμβους
                previouslyVisited = []  # Αδίαζουμε την previouslyVisitided
                tmpNode = startNode  # επιλέγουμε πάλι τον start node για επέκταση (επαννεκίνηση)
                previouslyVisited.append(tmpNode)  # προσθέτουμε τον start node στην previuslyVisited
                #   μιας και μετα το break, θα επεκταθεί ο startNode και θα επιλεχθεί ο επόμενος στην ουρα
                maxdepth += 1  # και αυξάνουμε το όριο βάθους κατα ένα
                repeats = 1
                break  # Βγαινουμε απο την εσωτερική while


            tmpNode = queue[0]
            # Εφόσων δεν έχει αδείαση η ουρά, επιλέγουμε για επέκταση τον επόμενο κόμβο στην ουρα
            previouslyVisited.append(queue.pop(0))
            # Αφαιρούμε απο την ουρα τον κόμβο που επιλέξαμε και τον προσθέτουμε στην priviulyVisited

        # Για να υλοποιηθεί ο DFS βάζουμε τα παιδία μπροστά απο τους υπόλοιπους κόμβους που είχε η queue
        queue = makeQueue(tmpNode) + queue

        # Επιλέγουμε τον επόμενο κόμβο για επέκταση
        tmpNode = queue[0]
        repeats += 1

    print("Done, goal node data:")
    tmpNode.printclass()
    print("Total nodes created:", counter, "and to max depth:", maxdepth)
    print("Total nodes expanded:(in the last search)", repeats)
    print("Path to the GoalNode:", backTracePath(tmpNode))


def Astar(queue):
    """ Υλοποιήση του A*, Επιλέγει τον κόμβο με το μικρότερο κόστος
        :param: queue, Ουρα στην οποία θα επεκτείνει (global Πινακας),
                με πρώτο στοιχείο ο κόμβος απο τον οποίο θα ξεκινήσει η επέκταση"""
    # Ο A* είναι ακριβώς όπως ο UCS αλλά κάνει sort με βάση την heuristic τιμή

    previouslyvisited = []
    repeats = 0
    tmpNode = queue[0]
    while (tmpNode.value != 'G'):
        queue.extend(makeQueue(tmpNode))
        previouslyvisited.append(queue.pop(0))
        queue = sorted(queue, key=lambda Nodes: Nodes.Hvalue)
        # Η μόνη αλλαγή που κάνουμε για τον Astart είναι να ταξινομούμε κατα την heuristic τιμή
        printing.printQueueCost(queue)
        queue = sameValueMoves(queue)
        tmpNode = queue[0]
        repeats += 1
    # Στο τέλος του while, το tmpNode είναι ο κόμβος στόχου
    previouslyvisited.append(tmpNode)

    print("Done, goal node data:")
    tmpNode.printclass()
    print("Total nodes created:", counter)
    print("Total nodes expanded:", repeats)
    print("Path to the GoalNode:", backTracePath(tmpNode))


def main():
    """Main"""

    global totalColumns, totalLines, labyrinth, counter
    # (Parsing) Ανάγνωση του αρχείου με τον λαβύρινθο
    file1 = open('labyrinth.txt', 'r') # πρέπει να είναι στον ίδιο φάκελο με το αρχείο main.py
    # Δίαβασμα του αρχείου
    lst = []
    for i in file1:
        for j in i:
            if (j == '\n'):  # αγνούμε τον κρυφό \n χαρακτήρα
                continue
            lst.append(j)  # Προσωρινός πίνακας που κρατάει τα στοιχεία της κάθε γραμμής
        labyrinth.append(lst)  # Ο προσωρινος πίνακας, γίνεται γραμμή στον τελικό
        lst = []
        # εν τέλει έχουμε εναν 2d πίνακα

    totalLines = len(labyrinth)
    # Βλέπουμε πόσες γραμμές εχει ο πίνακας (πλήθος των υπο-πινάκων)
    totalColumns = len(labyrinth[0])
    # Και για να δούμε πόσες στήλες έχει ο πίνακας,
    # βλέπουμε το μήκος κάποιου υπο-πίνακα

    # ένα πρόβλημα που μπορεί να υπάρξει εδώ είναι τα κενά μετα απο κάποιο χαρακτήρα
    # πχ:(γραμμή 4)[  DX DX  D   ] κάποιοι text editors, δεν θα κρατήσουν τα κενά μετα το D
    # το notepad όμως τα κρατάει

    # Εκτύπωση του τελικού πίνακα
    print("Ο λαβύρινθος σε μορφή πίνακα")
    for i in labyrinth:
        print(i)
        # Εκτυπώνουμε τον κάθε υπο-πίνακα ξεχωριστά


    # Υπολογισμός των heuristic τιμών
    heuristic()

    # Εκτύπωση των heuristic τιμών
    print()  # Κενή γραμμή
    print("Οι τιμές των hueristic τιμών για κάθε θέση του πίνακα")
    for i in heuristicTable:
        print(i)

    queue = []
    startNode = Nodes([0, 0],
                      Nodes([-1, -1], [-1, -1], -1, -1, "null", -1),
                      # για fathernode στον startnode θέτουμε ενα άλλο αντικείμενο τύπου Nodes
                      0, 0, "S", -1)  # Είχε 15 στο hvalue ο παλ
    queue.append(startNode)

    # print()  # Κενή γραμμή
    # print("Running UCS")
    # ucs(queue)
    # counter = 0
    # queue = []
    # queue.append(startNode)
    # # Αρχικοίηση των τιμών μετά απο κάθε εκτέλεση των αλγωρίθμων

    print("Running A*")
    Astar(queue)
    counter = 0
    queue = []
    queue.append(startNode)

    # print()
    # print("Running IDS")
    # ids(queue)


if (__name__ == '__main__'):
    main()
