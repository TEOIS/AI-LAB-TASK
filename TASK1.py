

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
        initialState="O"
        goalState="I"
        graph={
    "O":Node('O',None,["Z","S"],None),
    "Z":Node('Z',None,['A'],None),
    "S":Node("S",None, ['F','R'], None),
    "A":Node("A",None,['S','T'],None),
    "T":Node("T",None,['L'],None),
    "L":Node("L",None,['M'],None),
    "M":Node('M',None,['D'],None),
    "D":Node("D",None,['C'],None),
    "F":Node("F",None,['B'],None),
    "C":Node("C",None,['R','P'],None),
    "R":Node("R",None,['P','C'],None),
    "P":Node("P",None,['B'],None),
    "G":Node("G",None,['B'],None),
    "B":Node("B",None,['G','U'],None),
    "U":Node("U",None,['V','H'],None),
    "V":Node("V",None,['I'],None),
    "H":Node("H",None,['E'],None),
    "I":Node("I",None,['N'],None),
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
country={
    "O":"ORODEA",
    "Z":"ZORIND",
    "A":"ARAD",
    "T":"TIMISORIA",
    "L":"LUGOJ",
    "M":"MEHADIA",
    "D":"DROBETA",
    "C":"CRAIOVA",
    "S":"SIBUI",
    "F":"FAGARAS",
    "R":"RIMNICU",
    "P":"PITSETI",
    "B":"BUCHAREST",
    "G":"GUIRGIU",
    "U":"URZICENI",
    "V":"VASLUI",
    "I":"ISAI",
    "N":"NEAMT",
    "H":"HIRSOVA",
    "E":"EFOIRE"
}
for i in range(solution.__len__()):
    print(country[solution[i]],end=',')
    
    