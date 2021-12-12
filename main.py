import algorithms

totalnodes = 0


def backTracePath(currentNode):
    """
    backTracePath
    :param currentNode: Ο τορινός κόμβος (κόμβος λύση)
    :return: ένα string με τις καταστάσεις που οδηγούν στην αρχή (μονοπάτι)
    """
    btNode = currentNode #backTraceNode
    path = ''
    # Εκμεταλευεται το fathernode, ξεκινάμε απο τον G και πάμε στον father του (προς τα πίσω κίνηση)
    while (btNode.value != 'S'):
        path = path + str(btNode.state) + ' -> '  # κρατάμε την κατάσταση στο string αυτο
        btNode = btNode.fathernode
        # fathernode απο τον τορινο
        # ο επόμενος γίνεαι ο πατέρας του τορινού
        # Εδώ θα μπορούσε να υπολογιστεί το depth.

    path = path + str(btNode.state)
    return path


def main():
    [goalNode, previuslyVisited, repeats, totalnodes] = algorithms.IDS()

    # Στο tmpNode βρησκεται η κατάσταση στόχου
    print("Finished, Goal State:")
    goalNode.printclass()
    print("length of previusly:", len(previuslyVisited))
    print("Total nodes created", repeats)  # Οι κομβοι που δημιουργιθηκαν ειναι οι επαναλήψεις του while
    print("total nodes expanded:", totalnodes)

    print("Path:(from G to S)")
    print(backTracePath(goalNode))  # Εκτύπωση του μονοπατιού


if (__name__ == '__main__'):
    main()
