def printQueueState(queue):
    print("Size of queue: ", len(queue))
    for i in queue:
        print(i.state, end='')
    print('\n')


def printQueueCost(queue):
    print("Size of queue: ", len(queue))
    for i in queue:
        print(str(i.cost)+",", end='')
    print('\n')
