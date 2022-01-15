""" Main Αρχείο
    Εργασία 1 από τους:
    1451 Γεωργίτσαρος Κωνστατνίνος
    1530 Κωνσταντινος Παλεγκας
    1495 Χαρίσης Κύρινας
    1481 Καραγκιώτης Αθανάσιος
    Υλποιήθηκε σε Python 3.9 - 3.10"""

from nodes import Nodes
import random

# global τιμές
counter = 0
heuristicTable = []
labyrinth = []
totalLines = 0
totalColumns = 0


def sameValueMoves(queue, value):
    """
    Βρίσκει πόσα στοιχεία στην ουρά εχουν το ίδιο κόστος, επιλέγει ένα τυχαίο απο τα ίδιου κόστους,
    και το αλλάζει θέση με τον πρώτο της ουράς.
    :param queue: (πίνακας) Η ουρά οπου στην οποία θα γίνει η επιλογή (ταξινομημένη απο μικρότερο προς το μεγαλύτερο)
    :param value: (string) cost/hvalue με βάση ποια τιμή κόστους θα γίνει ο έλεγχος
    :return: (πίνακας) την ουρά που ήρθε σας είσοδος αλλά σαν πρώτο στοιχείο το τυχαία επιλεγμένο
    """

    # Δύο ξεχωριστά if για κάθε τιμή
    if value == "cost":
        # Σαν κόστος με το οποίο θα γίνεται η σύγκριση παίρνουμε το κόστος του πρώτου στοιχείου
        cost = queue[0].cost

        sameCostCounter = 0  # πλήθος κόμβων με το ίδιο κόστος
        i = 0
        while(queue[i].cost == cost and len(queue)-1 > i):
            # Το while αυτό μετράει πόσοι κόμβοι έχουν το ίδιο κόστος και σταματάει με το που βρεί κάποιον κόμβο με
            # διαφορετικό κόστος
            sameCostCounter += 1
            i += 1

        # κάνουμε την αλλαγή θέσεων αν υπάρχουν παραπάνω απο 1 κόμβοι με το ίδιο κόστος
        if(sameCostCounter > 1):
            randomChoice = random.randrange(0, sameCostCounter)
            # η randrange(0,sameCostCounter) θα επιστρέψει μια Int τιμή απο το 0 μέχρι το πλήθος των κόμβων με το
            # ίδιο κόστος
            queue[0], queue[randomChoice] = queue[randomChoice], queue[0]
            # Αλλαγή θέσεων

    elif value == "hvalue":
        cost = queue[0].Hvalue
        sameCostCounter = 0
        i = 1
        while (queue[i].Hvalue == cost and len(queue) - 1 > i):
            sameCostCounter += 1
            i += 1

        if (sameCostCounter > 0):
            randomChoice = random.randrange(0, sameCostCounter)
            queue[0], queue[randomChoice] = queue[randomChoice], queue[0]
    return queue


def heuristic():
    """
    Συνάρτηση να βρίσκει το heuristic σε μέγεθος του αρχικού πίνακα
    Αλλάζει global τιμές
    """
    global heuristicTable
    # Για να ξέρει η συνάρτηση ότι η μεταβλητή Heurustic είναι global
    heuristicTable = [[] for i in range(totalLines)]
    # Φτιάχνουμε έναν 2d πίνακα με totalLines συνολικές γραμμές
    # Οι γραμμές περιέχουν άδειους πίνακες

    for i in range(totalLines):
        for j in range(totalColumns):
            heuristicTable[i].append(0)
            # Σε κάθε υπο-πίνακα προσάρτονται totalColumns συνολικά μηδενικά
    gi = -1
    gj = -1
    # gi, gj Θέση στον πίνακα που βρήσκεται το G
    for i in range(totalLines):
        for j in range(totalColumns):
            if (labyrinth[i][j] != 'G'):
                continue
            else:
                gi = i
                gj = j

    # Υλοποίηση της απόσταστης Manhattan
    for i in range(totalLines):
        for j in range(totalColumns):
            dy = abs(i - gi)
            # για κάθε στοιχείο του πίνακα μετράμε πόσα βήματα πρέπει να κάνουμε κάθετα
            dx = abs(j - gj)
            # και πόσα οριζόντια
            heuristicTable[i][j] = dx + dy
            # Στο τέλος έχουμε έναν δελυτέρο πίνακα, ίδιων διαστάσεων με τον πίνακα του λαβύρινθου
            # που περιέχει την απόσταση manhattan για κάθε κελί


def makeQueue(node):
    """ Συνάρτηση που βρίσκει τις διαθέσιμες ενέργειες και τις επεκτήνει
    :param: node: αντικείμενο τύπου nodes, κομβος τον οποίο θα επεκτείνει

    :returns: πίανας<--πινακας με τα παιδία του κόμβου που πήρε σαν είσοδο"""
    tmpQ = []  # Εδώ θα αποθυκευτούν τα παιδία του κόμβου που θα επεκταθεί
    i = node.state[0]
    j = node.state[1]
    # print("i=", i, "j=", j)

    # Για κάθε κατεύθηνση (ενέργεια) έχουμε και ξεχωριστό if
    if (i + 1 < totalLines and labyrinth[i + 1][j] != "X" and node.fathernode.state != [i + 1, j]):
        # Στο οποίο μπορούμε να μπούμε μέσα μόνο αν η ενέργεια (μετακίνηση) που πάμε να κάνουμε δεν είναι:
        #   Εκτός ορίων του πίνακα (i + 1 < totalLines)
        #   Το κελί που θα πάμε δεν είναι αδιέξωδος (labyrinth[i + 1][j] != "X")
        #   Και η ενέργεια που θα κάνουμε δεν μας οδηγεί στον πατέρα κόμβο
        #       κόμβου που επεκτείνουμε

        # Δημιουργούμε ενα προσωρινό αντικείμενο (κόμβος)
        tmpNode = Nodes([i + 1, j], node, node.cost, node.depth, labyrinth[i + 1][j], 0)  # προς τα κάτω
        # του θέτουμε το κόστος και το βάθος
        tmpNode.depth += 1
        tmpNode.cost += 1
        # Αρχικά το κοστος και το βάθος του προσωρινού κόμβου έχουν τις τιμές του κόμου-πατέρα<--κόμβου
        #   και αυξάνονται κατα 1

        # Αυξάνουμε το πλήθος των κόμβων που επεκτάθηκαν
        nodecounter()

        # Αν ο κόμβος που πάμε να επεκτείνουμε είναι πόρτα
        if (tmpNode.value == 'D'):
            # ξανα αυξάνουμε ξανά το κόστος κατα 1 (συνολικά αυξάνεται κατα 2)
            tmpNode.cost += 1

        # Θέτουμε την heuristic τιμή για αυτόν τον κόμβο (χρησιμοποιείται μόνο στον Astar)
        tmpNode.Hvalue = heuristicTable[i + 1][j] + tmpNode.cost

        # Βάζουμε τον προσωρινό κόμβο στον πίνακα που θα επιστραφεί
        tmpQ.append(tmpNode)

        # Διαγράφουμε τον προσωρινό κόμβο
        del tmpNode

    # το μόνο που αλλάζει στα υπόλοιπα if είναι η θέση του πίνακα (i+1, j+1, κτλ)
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


def backTracePath(currentNode):
    """
    backTracePath
    Συνάρτηση για να βρίσκουμε το μονοπάτι απο τον κόμβο στόχου προς την αρχή
    :param currentNode: ο τορινός κόμβος (κόμβος λύση)
    :return: ένα string με τις καταστάσεις που οδηγούν στην αρχή (μονοπάτι)
    """
    btNode = currentNode  # backTraceNode
    path = ''
    # Εκμεταλευεται το fathernode, ξεκινάμε απο τον G και πάμε στον πατέρα του (προς τα πίσω κίνηση)
    while (btNode.value != 'S'):
        path = path + str(btNode.state) + ' -> '  # κρατάμε την κατάσταση στο string
        btNode = btNode.fathernode
        # fathernode απο τον τωρινό
        # ο επόμενος γίνεται ο πατέρας του τωρινού
    path = path + str(btNode.state)
    del btNode
    return path


def nodecounter():
    """
    Συνάρτηση για να μετράει τους συνολικούς κόμβους που δημιουργήθηκαν
    Κάθε φορά που καλείται, αυξάνει το counter κατα 1
    """
    global counter
    counter += 1


def ucs(queue):
    """ Υλοποιήση του UCS, Επιλέγει τον κόμβο με το μικρότερο κόστος
        :param: queue, Ουρά στην οποία θα επεκτείνει (global Πίνακας),
                με πρώτο στοιχείο ο κόμβος απο τον οποίο θα ξεκινήσει η επέκταση"""
    previouslyVisited = []  # Σε αυτόν τον πίνακα κρατάμε τους κόμβους που επεκτείναμε
    repeats = 1
    tmpNode = queue[0]  # πέρνουμε το πρώτο στοιχείο της ουράς
    #   οταν πρωτο-καλείτε είναι το start node

    while (tmpNode.value != 'G'):
        # Εκτύπωση κάθε 1000 επεκτάσεις
        if (repeats % 5000 == 0):
            print("Expanded", counter, "nodes and still searching, current node:")
            tmpNode.printclass()
        # Η while είναι αυτή που ελέγχει αν είμαστε σε κόμβο στόχου
        queue = queue + makeQueue(tmpNode)
        # Βάζουμε τα στοιχεία του πίνακα που επιστρέφει η makeQueue μετά τα στοιχεία που ήδη περιέχει ο πίνακας Queue
        previouslyVisited.append(queue.pop(0))
        # Αφαιρούμε απο την queue το στοιχείο που μόλις επεκτήναμε και ταυτόχρονα το βάζουμε στην previuslyVisited
        queue = sorted(queue, key=lambda Nodes: Nodes.cost)
        # sort της queue με βάση το κόστος των κόμβων

        # τροποποίηση της queue για να επιλέγει τυχαία ισάξια ενέργεια
        queue = sameValueMoves(queue, "cost")
        tmpNode = queue[0]
        repeats += 1

    # Στο τέλος του while, το tmpNode είναι ο κόμβος στόχου, και η previuslyVisited είναι οι κόμβοι που ελέγχθηκαν
    previouslyVisited.append(tmpNode)
    # Μια τελευταία πρόσθεση στην previouslyVisited, για να μπεί ο κόμβος στόχου

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
        # Αφαιρούμε τον κόμβο που θα επεκταθεί απο την ουρά
        previouslyVisited.append(queue.pop(0))
        # Ο κόμβος που θα επεκταθεί είναι στην tmpNode, οπότε μπορούμε να τον βγάλουμε απο την ουρα
        #   πριν "ολοκληρωθεί" η επέκταση

        # Επεκτίνουμε κανονικά με DFS μεχρι να φτάσουμε στο όριο βάθους depthLimit
        while (tmpNode.depth == maxdepth):

            # Έπρεπε να βάλουμε και αυτήν τον έλεγχο
            # # Αν στα φύλλα αυτου το μέγστου βάθους βρίσκεται το G, σταματάμε την αναζήτηση
            # if (tmpNode.value == 'G'):
            #     break

            # Όσο οι κόμβοι που πάμε να επεκτείνουμε είναι στο όριο βάθους,
            # τους επιλέγουμε για έλεγχο αλλά δεν επεκτείνουμε
            if (len(queue) == 0):
                # Όταν το μέγεθος της ουράς μηδενιστεί
                previouslyVisited = []  # Αδειάζουμε την previouslyVisitided
                tmpNode = startNode  # επιλέγουμε πάλι τον start node για επέκταση (επαννεκίνηση)
                previouslyVisited.append(tmpNode)
                # μετα το break, θα επεκταθεί ο startNode και θα επιλεχθεί ο επόμενος στην ουρα
                maxdepth += 1  # αυξάνουμε το όριο βάθους κατα ένα
                repeats = 1
                break  # Βγαινουμε απο την εσωτερική while

            # τροποποίηση της queue για να επιλέγει τυχαία ισάξια ενέργεια
            queue = sameValueMoves(queue, "cost")
            tmpNode = queue[0]
            # Εφόσον δεν έχει αδείασει η ουρά, επιλέγουμε για επέκταση τον επόμενο κόμβο στην ουρα
            previouslyVisited.append(queue.pop(0))
            # Αφαιρούμε απο την ουρα τον κόμβο που επιλέξαμε και τον προσθέτουμε στην previouslyVisited

        # Για να υλοποιηθεί ο DFS βάζουμε τα παιδία μπροστά απο τους υπόλοιπους κόμβους που είχε η queue
        queue = makeQueue(tmpNode) + queue

        # Επιλέγουμε τον επόμενο κόμβο για επέκταση
        # τροποποίηση της queue για να επιλέγει τυχαία ισάξια ενέργεια
        queue = sameValueMoves(queue, "cost")
        tmpNode = queue[0]
        repeats += 1

    print("Done, goal node data:")
    tmpNode.printclass()
    print("Total nodes created:", counter, "Μax depth:", maxdepth)
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
        # Η μόνη αλλαγή που κάνουμε για τον Astar είναι να ταξινομούμε κατα την heuristic τιμή
        # τροποποίηση της queue για να επιλέγει τυχαία ισάξια ενέργεια (αλλά με βάση την heuristic τιμή)
        queue = sameValueMoves(queue, "hvalue")
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
    # (Parsing) Ανάγνωση του αρχείου που περιέχει τον λαβύρινθο
    file1 = open('labyrinth.txt', 'r')
    # Δίαβασμα του αρχείου
    lst = []
    for i in file1:
        for j in i:
            if (j == '\n'):  # αγνούμε τον κρυφό \n χαρακτήρα
                continue
            lst.append(j)  # Προσωρινός πίνακας που κρατάει τα στοιχεία της κάθε γραμμής
        labyrinth.append(lst)  # ο προσωρινος πίνακας, γίνεται γραμμή στον τελικό
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

    # Υπολογισμός των heuristic τιμών
    heuristic()

    # Εκτύπωση των heuristic τιμών
    print("-------")
    print("Οι τιμές των hueristic για κάθε θέση του πίνακα")
    for i in heuristicTable:
        print(i)

    queue = []
    startNode = Nodes([0, 0],
                      Nodes([-1, -1], [-1, -1], -1, -1, "null", -1),
                      # για fathernode στον startnode θέτουμε ενα άλλο αντικείμενο τύπου Nodes
                      0, 0, "S", -1)
    queue.append(startNode)

    print("-------")
    print("Running UCS")
    ucs(queue)
    counter = 0
    queue = []
    queue.append(startNode)
    # Αρχικοίηση των τιμών μετά απο κάθε εκτέλεση των αλγωρίθμων

    print("Running A*")
    Astar(queue)
    counter = 0
    queue = []
    queue.append(startNode)

    print("-------")
    print("Running IDS")
    ids(queue)


if (__name__ == '__main__'):
    main()
