def printQueueState(queue):
    print("Size of queue: ", len(queue))
    for i in queue:
        print(i.state, end='')
    print('\n')
