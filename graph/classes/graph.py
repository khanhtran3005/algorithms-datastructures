from .vertex import Vertex

class Graph():
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        return None

    def __contain__(self, i):
        return i in self.vertices

    def addEdge(self, f, t, cost=0):
        if f not in self.vertices:
            self.addVertex(f)
        if t not in self.vertices:
            self.addVertex(t)

        self.vertices[f].addNeighbor(self.vertices[t], cost)

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def __str__(self):
        return str([x for x in self.vertices])

    def __len__(self):
        return len(self.vertices)

