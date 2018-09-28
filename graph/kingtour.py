from classes.graph import Graph

def knightGraph(boardSize):
    ktGraph = Graph()

    for row in range(boardSize):
        for col in range(boardSize):
            nodeId = posToNodeId(row, col, boardSize)
            moves = legalMoves(row, col, boardSize)
            for move in moves:
                posibleNodeId = posToNodeId(move[0], move[1], boardSize)
                ktGraph.addEdge(nodeId, posibleNodeId)

    return ktGraph

def posToNodeId(row, col, boardSize):
    return boardSize * row + col

def legalMoves(row, col, boardSize):
    newMoves = []
    posibleMoves = [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),( 1,2),(2,-1),(2,1)]

    for move in posibleMoves:
        x = row + move[0]
        y = col + move[1]

        if legalCoord(x, y, boardSize):
            newMoves.append((x, y))
    return newMoves

def legalCoord(row, col, boardSize):
    return row < boardSize and row >= 0 and col < boardSize and col >= 0


def kingTour(graph, n, path, u, limit):
    u.setColor('grey')
    path.append(u)
    if n < limit:
        nbrList = orderByAvail(u)
        i = 0
        done = False

        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = kingTour(graph, n + 1, path, nbrList[i], limit)
            i += 1

        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True

    return done

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))

    resList.sort(key=lambda x: x[0])

    return [y[1] for y in resList]


size = 8
graph = knightGraph(size)

path = []
result = kingTour(graph, 0, path, graph.getVertex(0), size**2 - 1)

print('Result:', result)
strPath = ""
for vertex in path:
    strPath += str(vertex.getId()) + ' => '
strPath = strPath.rstrip(' => ')
print('Path:', strPath)