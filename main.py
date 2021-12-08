from nodes import Nodes
import parseLabyrinthBasic
import printing

totalnodes = 0


def makeQueue(node, queue):
    """
    Βρισκει τι διαθέσιμες κινήσεις μπορουμε να κάνουμε απο την κατάσταση του node και τις επεκτείνει.
    :param node: nodes, Κόμβος που θα επεκταθεί
    :param queue: πίνακας, Ουρά οπου θα αποθυκευτούν οι νέοι κομβοι
    """
    global totalnodes
    tmpQ = queue
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
            print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost,"granfathernode:",node.fathernode.state)
        del tmpNode

    if (j + 1 < totalColumns and labyrinth[i][j + 1] != "X"):
        tmpNode = Nodes([i, j + 1], node, node.cost, node.depth, labyrinth[i][j + 1])  # moved "right"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost,"granfathernode:",node.fathernode.state)
        del tmpNode

    if (i - 1 >= 0 and labyrinth[i - 1][j] != "X"):
        tmpNode = Nodes([i - 1, j], node, node.cost, node.depth, labyrinth[i - 1][j])  # moved "up"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost,"granfathernode:",node.fathernode.state)
        del tmpNode


    if (j - 1 >= 0 and labyrinth[i][j - 1] != "X"):
        tmpNode = Nodes([i, j - 1], node, node.cost, node.depth, labyrinth[i][j - 1])  # moved "left"
        tmpNode.depth += 1
        tmpNode.cost += 1
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1

        if tmpNode.state != node.fathernode.state:
            tmpQ.append(tmpNode)
            print("tmpNode that was appended:", tmpNode.state, "and cost:", tmpNode.cost,"granfathernode:",node.fathernode.state)
        del tmpNode


    totalnodes += len(tmpQ)
    return tmpQ


[labyrinth, totalLines, totalColumns] = parseLabyrinthBasic.parseLabyrinth("labyrinth.txt")
previouslyvisited = []
t=Nodes(-1,[-1,-1],-1,-1,"null")
startNode = Nodes([0, 0], t, 0, 0, "S")
startNode.fathernode.state=[-1,-1]
queue = makeQueue(startNode, [])
quepos = 1
tmpNode = queue[0]
previouslyvisited.append(startNode)

repeats = 0  # prosorino, to ebales gia na exeis ligotera prints
while (tmpNode.value != 'G'):
    # print("start while queue:")
    # printing.printQueueState(queue)
    makeQueue(tmpNode, queue)
    previouslyvisited.append(queue.pop(0))  # afairei ton komvo pou e3etasame prin
    queue = sorted(queue, key=lambda Nodes: Nodes.cost)

    # kwdikas gia na krataei poious komvous exoume elegjei
    # c=0
    # for i in queue:
    #     for j in previouslyvisited:
    #         if i.state == j.state:
    #             print("i.state:", i.state, ",j.state:",j.state)
    #             queue.pop(c)
    #     c+=1

    # printing.printQueueState(queue)
    tmpNode = queue[0]
    quepos += 1
    repeats += 1

# Στο tmpNode βρησκεται η κατάσταση στόχου
print("Finished, Goal State:")
tmpNode.printclass()
print("Total nodes created", repeats)  # Οι κομβοι που δημιουργιθηκαν ειναι οι επαναλήψεις του while
print("total nodes expanded:", totalnodes)

bcNode = tmpNode
print(bcNode.value)
path = ''
# Εκμεταλευεται το fathernode
while (bcNode.value != 'S'):
    path = path + str(bcNode.state) + ' -> '
    # Κάθε επανάληψη ψάχνουμε ποιος κομβός εχει την κατάσταση
    # fathernode απο τον τορινο
    bcNode = bcNode.fathernode
    # Αυτος που έχει την σωστή κατάσταση γίνεται ο επομενος τορινος
path = path + str(bcNode.state)
print(path)
# Με εναν απλο ελεγχο και ευρεση ποιου κομβου εχει την κατάσταση
# του πατερα, η λουπα του backtrace τρεχει για παντα (d^~60K έλεγοι)
input("Enter a key to continue")
