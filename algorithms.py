import parseLabyrinthBasic
from nodes import Nodes

totalnodes = 0
expandCounter=1


def UCS():
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
                print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "granfathernode:",
                      node.fathernode.state)
            del tmpNode

        if (j + 1 < totalColumns and labyrinth[i][j + 1] != "X"):
            tmpNode = Nodes([i, j + 1], node, node.cost, node.depth, labyrinth[i][j + 1])  # moved "right"
            tmpNode.depth += 1
            tmpNode.cost += 1
            if (tmpNode.value == 'D'):
                tmpNode.cost += 1

            if tmpNode.state != node.fathernode.state:
                tmpQ.append(tmpNode)
                print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "granfathernode:",
                      node.fathernode.state)
            del tmpNode

        if (i - 1 >= 0 and labyrinth[i - 1][j] != "X"):
            tmpNode = Nodes([i - 1, j], node, node.cost, node.depth, labyrinth[i - 1][j])  # moved "up"
            tmpNode.depth += 1
            tmpNode.cost += 1
            if (tmpNode.value == 'D'):
                tmpNode.cost += 1

            if tmpNode.state != node.fathernode.state:
                tmpQ.append(tmpNode)
                print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "granfathernode:",
                      node.fathernode.state)
            del tmpNode

        if (j - 1 >= 0 and labyrinth[i][j - 1] != "X"):
            tmpNode = Nodes([i, j - 1], node, node.cost, node.depth, labyrinth[i][j - 1])  # moved "left"
            tmpNode.depth += 1
            tmpNode.cost += 1
            if (tmpNode.value == 'D'):
                tmpNode.cost += 1

            if tmpNode.state != node.fathernode.state:
                tmpQ.append(tmpNode)
                print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "granfathernode:",
                      node.fathernode.state)
            del tmpNode

        totalnodes += len(tmpQ)
        return tmpQ

    global totalnodes
    [labyrinth, totalLines, totalColumns] = parseLabyrinthBasic.parseLabyrinth("labyrinth_small.txt")
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


def IDS():
    def makeQueue(node):
        """
        Βρισκει τι διαθέσιμες κινήσεις μπορουμε να κάνουμε απο την κατάσταση του node και τις βάζει στην ουρα,
        επίσης χρησιμοποιείται και για επέκταση (all-in-one).
        :param node: nodes, Κόμβος που θα επεκταθεί
        :param queue: πίνακας, Ουρά οπου θα αποθυκευτούν οι νέοι κομβοι
        """
        global totalnodes, expandCounter
        tmpQ = []
        i = node.state[0]
        j = node.state[1]
        print(expandCounter,"expanding node:", node.state, "to")

        if (i + 1 < totalLines and labyrinth[i + 1][j] != "X"):
            tmpNode = Nodes([i + 1, j], node, node.cost, node.depth, labyrinth[i + 1][j])  # moved "down"
            tmpNode.depth += 1
            tmpNode.cost += 1
            if (tmpNode.value == 'D'):
                tmpNode.cost += 1

            if tmpNode.state != node.fathernode.state:
                tmpQ.append(tmpNode)
                print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "granfathernode:",
                      node.fathernode.state)
            del tmpNode

        if (j + 1 < totalColumns and labyrinth[i][j + 1] != "X"):
            tmpNode = Nodes([i, j + 1], node, node.cost, node.depth, labyrinth[i][j + 1])  # moved "right"
            tmpNode.depth += 1
            tmpNode.cost += 1
            if (tmpNode.value == 'D'):
                tmpNode.cost += 1

            if tmpNode.state != node.fathernode.state:
                tmpQ.append(tmpNode)
                print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "granfathernode:",
                      node.fathernode.state)
            del tmpNode

        if (i - 1 >= 0 and labyrinth[i - 1][j] != "X"):
            tmpNode = Nodes([i - 1, j], node, node.cost, node.depth, labyrinth[i - 1][j])  # moved "up"
            tmpNode.depth += 1
            tmpNode.cost += 1
            if (tmpNode.value == 'D'):
                tmpNode.cost += 1

            if tmpNode.state != node.fathernode.state:
                tmpQ.append(tmpNode)
                print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "granfathernode:",
                      node.fathernode.state)
            del tmpNode

        if (j - 1 >= 0 and labyrinth[i][j - 1] != "X"):
            tmpNode = Nodes([i, j - 1], node, node.cost, node.depth, labyrinth[i][j - 1])  # moved "left"
            tmpNode.depth += 1
            tmpNode.cost += 1
            if (tmpNode.value == 'D'):
                tmpNode.cost += 1

            if tmpNode.state != node.fathernode.state:
                tmpQ.append(tmpNode)
                print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost, "granfathernode:",
                      node.fathernode.state)
            del tmpNode

        totalnodes += len(tmpQ)
        expandCounter+=1
        return tmpQ

    global totalnodes
    [labyrinth, totalLines, totalColumns] = parseLabyrinthBasic.parseLabyrinth("labyrinth_small.txt")
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
    while (tmpNode.value != 'G' and repeats<10):
        previouslyvisited.append(queue.pop(0))  # αφαιρείται απο την ουρα ο κόμβος που αναπτήχθηκε ->
        # (για καποιο λόγο στον IDS(UCS) πρέπει να μπει πριν προσθεθούν τα παιδιά)
        queue = makeQueue(tmpNode) + queue  # τα νέα παιδιά μπαινουν στην αρχή της ουρας

        tmpNode = queue[0]  # -> Και μπαίνει να αναπτήξει τον επόμενο
        # quepos += 1
        repeats += 1

    goalNode = tmpNode
    return goalNode, previouslyvisited, repeats, totalnodes
