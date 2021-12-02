from nodes import Nodes
import parseLabyrinthBasic

counter = 0

#change
#change 2
def test():
    print(totalLines)
    print(totalColumns)


def nodecounter():
    global counter
    counter += 1
    #print("Nodes:", counter)


def makeQueue(node, queue):
    tmpQ = queue
    i = node.state[0]
    j = node.state[1]
    print("i=", i, "j=", j)

    if (i + 1 < totalLines and labyrinth[i + 1][j] != "X"):
        tmpNode = Nodes([i + 1, j], node.state, node.cost, node.depth, labyrinth[i + 1][j])  # moved "down"
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpQ.append(tmpNode)
        del tmpNode

    if (j + 1 < totalColumns and labyrinth[i][j + 1] != "X"):
        tmpNode = Nodes([i, j + 1], node.state, node.cost, node.depth, labyrinth[i][j + 1])  # moved "right"
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpQ.append(tmpNode)
        del tmpNode

    if (i - 1 >= 0 and labyrinth[i - 1][j] != "X"):
        tmpNode = Nodes([i - 1, j], node.state, node.cost, node.depth, labyrinth[i - 1][j])  # moved "up"
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpQ.append(tmpNode)
        del tmpNode

    if (j - 1 >= 0 and labyrinth[i][j - 1] != "X"):
        tmpNode = Nodes([i, j - 1], node.state, node.cost, node.depth, labyrinth[i][j - 1])  # moved "left"
        tmpNode.depth += 1
        tmpNode.cost += 1
        nodecounter()
        if (tmpNode.value == 'D'):
            tmpNode.cost += 1
        tmpQ.append(tmpNode)
        del tmpNode

    return tmpQ


[labyrinth, totalLines, totalColumns] = parseLabyrinthBasic.parseLabyrinth("labyrinth_small_small.txt")

startNode = Nodes([0, 0], [-1,-1], 0, 0, "S")
queue = makeQueue(startNode, [])
nodecounter()
quepos = 1
tmpNode = queue[0]
previouslyvisited = []

repeats=0 # prosorino, to ebales gia na exeis ligotera prints
while (tmpNode.value != 'G' and repeats<3):
    print(quepos, ":", tmpNode.value, ":")
    makeQueue(tmpNode, queue)
    previouslyvisited.append(queue.pop(0)) # afairei ton komvo pou e3etasame prin
    queue = sorted(queue, key=lambda Nodes: Nodes.cost)
    tmpNode = queue[0]
    # for i in previouslyvisited: #kwdikas gia na krataei poious komvous exoume elegjei
    #   if i.state==tmpNode.state:
    #      queue.pop(0)
    #     tmpNode=queue[0]
    quepos += 1
    repeats+=1

print("Finished")
print("Katastasi tis ypoloipis ouras")
for i in queue:
    print("State:", i.state, "Cost:", i.cost, "Depth", i.depth, "Value", i.value)

print("thesi tis katastasi stoxou")
print(quepos, ":", tmpNode.value, ":")
print("Congratulations you found it!! State:", tmpNode.state)

