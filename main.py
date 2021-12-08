from nodes import Nodes
import parseLabyrinthBasic
import printing

totalnodes = 0


def makeQueue(node, queue):
    """
    Βρισκει τι διαθέσιμες κινήσεις μπορουμε να κάνουμε απο την κατάσταση του node και τις βάζει στην ουρα,
    επίσης χρησιμοποιείται και για επέκταση (all-in-one).
    :param node: nodes, Κόμβος που θα επεκταθεί
    :param queue: πίνακας, Ουρά οπου θα αποθυκευτούν οι νέοι κομβοι
    """
    global totalnodes
    tmpQ = queue
    i = node.state[0]
    j = node.state[1]
    # print("expanding node:", node.state, "to")

    if (i + 1 < totalLines and labyrinth[i + 1][j] != "X"):
        tmpNode = Nodes([i + 1, j], node, node.cost, node.depth, labyrinth[i + 1][j])  # moved "down"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            # print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost,"granfathernode:",node.fathernode.state)
        del tmpNode

    if (j + 1 < totalColumns and labyrinth[i][j + 1] != "X"):
        tmpNode = Nodes([i, j + 1], node, node.cost, node.depth, labyrinth[i][j + 1])  # moved "right"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            # print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost,"granfathernode:",node.fathernode.state)
        del tmpNode

    if (i - 1 >= 0 and labyrinth[i - 1][j] != "X"):
        tmpNode = Nodes([i - 1, j], node, node.cost, node.depth, labyrinth[i - 1][j])  # moved "up"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            # print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost,"granfathernode:",node.fathernode.state)
        del tmpNode

    if (j - 1 >= 0 and labyrinth[i][j - 1] != "X"):
        tmpNode = Nodes([i, j - 1], node, node.cost, node.depth, labyrinth[i][j - 1])  # moved "left"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            # print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost,"granfathernode:",node.fathernode.state)
        del tmpNode

    totalnodes += len(tmpQ)
    return tmpQ


[labyrinth, totalLines, totalColumns] = parseLabyrinthBasic.parseLabyrinth("labyrinth.txt")
previouslyvisited = []
startNode = Nodes([0, 0],
                  Nodes(-1, [-1, -1], -1, -1, "null"),  # Για fathernode εχουμε ενα ακομη πιο startnode
                  0, 0, "S")

queue = makeQueue(startNode, [])
totalnodes += 1
previouslyvisited.append(startNode)
# quepos = 1
tmpNode = queue[0]
repeats = 0  # prosorino, to ebales gia na exeis ligotera prints
while (tmpNode.value != 'G'):
    makeQueue(tmpNode, queue)
    previouslyvisited.append(queue.pop(0))  # Αφαιρήται απο την ουρα ο κόμβος που αναπτήχθηκε ->
    queue = sorted(queue, key=lambda Nodes: Nodes.cost)

    # Κώδικας που ελέγχει αν πάμε να εξερευνήσουμε κόμβο που έχουμε εξερευνήσει
    # for i in previouslyvisited:
    #   if i.state==tmpNode.state:
    #      queue.pop(0)
    #     tmpNode=queue[0]

    # printing.printQueueState(queue)
    tmpNode = queue[0]  # -> Και μπαίνει να αναπτήξει τον επόμενο
    # quepos += 1
    repeats += 1

# Στο tmpNode βρησκεται η κατάσταση στόχου
print("Finished, Goal State:")
tmpNode.printclass()
print("Total nodes created", repeats)  # Οι κομβοι που δημιουργιθηκαν ειναι οι επαναλήψεις του while
print("total nodes expanded:", totalnodes)

bcNode = tmpNode
path = ''
# Εκμεταλευεται το fathernode, ξεκινάμε απο τον G και πάμε στον father του (προς τα πίσω κίνηση)
while (bcNode.value != 'S'):
    path = path + str(bcNode.state) + ' -> '  # κρατάμε την κατάσταση στο string αυτο
    # fathernode απο τον τορινο
    bcNode = bcNode.fathernode
    # ο επόμενος γίνεαι ο πατέρας του τορινού
    # Εδώ θα μπορούσε να υπολογιστεί το depth.


path = path + str(bcNode.state)
print("Path:(from G to S)")
print(path)
input("Enter a key to continue")
