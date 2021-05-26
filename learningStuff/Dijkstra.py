
infinity = float('inf')
# 数组processed，用来记录已经处理过的节点
processed = []


class Node(object):
    # sons = {}   # key=SonNodeObject, value=costFromSelfToSon
    # parents = {}    # key=parentNodeObject, value=costFromParentToSelf
    name = ""

    # bool processed = False  #这个属性不应该是Node的属性，而是算法的属性

    def __init__(self, name):
        self.name = name

    # def getCostToSon(self, sonName):
    #    return self.sons[sonName]

    def getName(self):
        return self.name


class Edge(object):
    startNode = None
    endNode = None
    cost = 0

    def __init__(self, nodeS, nodeE, cost):
        self.startNode = nodeS
        self.endNode = nodeE
        self.cost = cost

    def displayEdge(self):
        print("%s --> %s : %f " %(self.startNode.getName(), self.endNode.getName(), self.cost))

    def getStartNode(self):
        return self.startNode

    def getEndNode(self):
        return self.endNode

    def getCost(self):
        return self.cost


class Graph(object):
    # 图中所有边的信息，起点，终点，cost
    edges = []

    # 图中节点作为key, value 是一个list ，list中有3个元素[parentNode, CostFromStartToThis, isProcessed]
    # CostFromStartToThis为起点到当前节点的cost
    bestPathDic = {}

    # processed list used to stored the processd node
    processed = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def displayGraph(self):
        for edge in self.edges:
            edge.displayEdge()

    def displayBestPathDic(self):
        print(("%s %s %s")%("parent".ljust(10),"Node".center(10),"Cost".rjust(10)))
        for key in self.bestPathDic:
            print("%s %s %s " % (str(self.bestPathDic[key][0]).ljust(10), key.center(10), str(self.bestPathDic[key][1]).rjust(10)))


    def initBestPathDic(self):
        for edge in self.edges:
            if( edge.getStartNode() not in self.bestPathDic.keys()):

                # 如果当前边的起点是start，更新当前节点的parent为start，cost为当前边的权值
                if(edge.getStartNode().getName() == "start"):
                    self.bestPathDic[edge.getEndNode().getName()] = ["start", edge.getCost(),False]

                # 如果当前边的起点不是start，更新当前节点的parent为未知‘--’，cost为无限大
                elif(edge.getEndNode().getName() not in self.bestPathDic.keys()):
                    self.bestPathDic[edge.getEndNode().getName()] = ["--", infinity,False]
        self.displayBestPathDic()
        print("----initBestPathDic finish-------")

    def findCheapNode(self):
        print("----findCheapNode start-------")
        cheapNode = None
        cheapestCost = infinity
        for key in self.bestPathDic:
            if(self.bestPathDic[key][1] < cheapestCost and key not in processed):
                cheapNode = key
                cheapestCost = self.bestPathDic[key][1]

        print("\t\t\tfindCheapNode %s"%cheapNode)
        if(cheapNode is not None):
            processed.append(cheapNode)
        return cheapNode


    def findBestPath(self):
        print("----findBestPath start-------")


        currentNodeName = self.findCheapNode()
        print("current node is %s" % currentNodeName)

        while currentNodeName is not None:
            # 计算当前节点前往各个邻居的开销

            #处理当前节点，找出最便宜的邻居节点
            for edge in self.edges:
                if(edge.getStartNode().getName() == currentNodeName):
                    print("Edge: %s --> %s" % (currentNodeName, edge.getEndNode().getName()))

                    # costFromStartToEndOfCurrentEdge 是从起点到当前边的End节点这条路径的值
                    # self.bestPathDic[currentNode.getName()][1] 为已经更新好的 起点到当前节点的最短路径的值
                    costFromStartToEndOfCurrentEdge = edge.getCost() + self.bestPathDic[edge.getStartNode().getName()][1]
                    print("     Cost from Start --> %s: %f + %f " % (edge.getEndNode().getName(), edge.getCost(), self.bestPathDic[edge.getStartNode().getName()][1]))
                    # costForNeighborInBestPathDic 是当前边的End节点在bestPathDic表中对应的cost
                    #也就是起点到当前边的路径的cost

                    costForNeighborInBestPathDic = self.bestPathDic[edge.getEndNode().getName()][1]
                    print("     Cost of \'%s\' in bestPathDic: %f " % (edge.getEndNode().getName(), costForNeighborInBestPathDic))
                    if(costFromStartToEndOfCurrentEdge < costForNeighborInBestPathDic ):
                        print("update bestPathDic for %s" %edge.getEndNode().getName())
                        #在bestPathDic表中，对当前节点的邻居的cost项进行更新
                        self.bestPathDic[edge.getEndNode().getName()][1] = costFromStartToEndOfCurrentEdge
                        self.bestPathDic[edge.getEndNode().getName()][0] = edge.getStartNode().getName()
                    self.displayBestPathDic()

            #继续计算最便宜节点前往其各个邻居的开销
            #currentNodeName = None
            currentNodeName = self.findCheapNode()

        #finNode = self.bestPathDic[]






"""
graphStart = {}
graphStart["a"] = 6
graphStart["b"] = 2

graphA = {}
graphA["fin"] = 1

graphB = {}
graphB["fin"] = 5
graphB["a"] = 3

graphFin = {}

graphBig = {}
graphBig["start"] = graphStart
graphBig["fin"] = graphFin
graphBig["a"] = graphA
graphBig["b"] = graphB

print(graphStart)
print(graphFin)
print(graphA)
print(graphB)
print(graphBig)

# COST表 记录start到各个节点的开销，一旦有更低开销就更新

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# PARENT表 记录在查找最短路径过程中各个节点的父节点，一旦查找到更便宜节点，则更新该表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None  # 初始状态终点还没有父节点


"""




nodeA = Node("a")
nodeB = Node("b")
nodeStart = Node("start")
nodeFin = Node("fin")

#edge begin from Node_Start
edgeStartA = Edge(nodeStart, nodeA, 6)
edgeStartB = Edge(nodeStart, nodeB, 2)

#edge begin from Node_A
edgeAFin = Edge(nodeA, nodeFin, 1)

#edge begin from Node_B
edgeBA = Edge(nodeB, nodeA, 3)
edgeBFin = Edge(nodeB, nodeFin, 5)

graph = Graph()
graph.addEdge(edgeStartA)
graph.addEdge(edgeStartB)
graph.addEdge(edgeAFin)
graph.addEdge(edgeBA)
graph.addEdge(edgeBFin)
graph.displayGraph()
graph.initBestPathDic()
graph.findBestPath()
