class Node:
    state=""
    parent=None
    action=[]
    def __init__(self,state,parent,action,totalcost):
        self.state=state
        self.parent=parent
        self.action=action
        self.totalcost=totalcost
def BFS():
        initialState="1"
        goalState="15"
        graph={
    "1":Node('1',None,["2"],None),
    "2":Node('2',None,['3'],None),
    "3":Node("3",None, ['4'], None),
    "4":Node("4",None,['5','26'],None),
    "5":Node("5",None,['8','6'],None),
    "6":Node("6",None,['7','5'],None),
    "7":Node('7',None,['8','9'],None),
    "8":Node("8",None,['5','7'],None),
    "9":Node("9",None,['10'],None),
    "10":Node("10",None,['11','12'],None),
    "11":Node("11",None,['10'],None),
    "12":Node("12",None,['13'],None),
    "13":Node("13",None,['14'],None),
    "14":Node("14",None,['15','16'],None),
    "15":Node("15",None,['14'],None),
    "16":Node("16",None,['17'],None),
    "17":Node("17",None,['18'],None),
    "18":Node("18",None,['19'],None),
    "19":Node("19",None,['20'],None),
    "20":Node("20",None,['21'],None),
    "21":Node("21",None,['22'],None),
    "22":Node("22",None,['23'],None),
    "23":Node("23",None,['24'],None),
    "24":Node("24",None,['25'],None),
    "25":Node("25",None,['26'],None),
    "26":Node("26",None,['4'],None),
    }
        
        frontier=[initialState]
        explored=[]
        while len(frontier)!=0:
            currentNode=frontier.pop(0)
            explored.append(currentNode)
            for child in graph[currentNode].action:
                if child not in frontier and child not in explored:
                    graph[child].parent=currentNode
                    if graph[child].state==goalState:
                        return actionSequence(graph,initialState,goalState)
                    frontier.append(child)
def actionSequence(graph,initialState,goalState):
    solution=[goalState]
    currentParent=graph[goalState].parent
    while currentParent!=None:
        solution.append(currentParent)
        currentParent=graph[currentParent].parent
    solution.reverse()
    return solution                    
solution=BFS()
print(solution)