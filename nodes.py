class Nodes:
    """
    state: katastasti tou node (thesi ston pinaka)
    fathernode: patrikos kombos (thesi ston pinaka)
    cost: kostos gia na ftasoume se aytin tin katastasi (int)
    depth: bathos tis katastasis (int)
    value: timi tis katastasis (str)
    """

    def __init__(self,state=[-1, -1], fathernode=[-1, -1], cost=-1, depth=-1, value="null",Hvalue=-1):
        self.state = state
        self.fathernode = fathernode
        self.cost = cost
        self.depth = depth
        self.value = value
        self.Hvalue = Hvalue

    def printclass(self):
        print("State:", self.state,
              "Fathernode:", self.fathernode.state,
              "Cost:", self.cost,
              "Depth:", self.depth,
              "Value:", self.value,
              "Hvalue:", self.Hvalue)




