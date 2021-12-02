def printQueueState(queue):
    print(len(queue))
    for i in queue:
        print(i.state, end='')
    print('\n')
