class Vertex:
    def __init__(self, name,colour = 0):
        self.name = name
        self.colour = colour
    def __repr__(self):
        return("Vertex:"+str(self.name)+" Colour: "+str(self.colour))

class Edge:
    def __init__(self, v1, v2, weight=1):
        self.a = v1
        self.b = v2
        self.weight = weight
    def __repr__(self):
        return("Edge between " + str(self.a) +" " + str(self.b) + " Weight: " + str(self.weight))

class Graph:
    def __init__(self, V, E):
        self.Vertices = V
        self.Edges = E

    def Neighbours(self, v):
        neighbours = set()
        for edge in self.Edges:
            if edge.a == v:
                neighbours.update({edge.b})
            if edge.b == v:
                neighbours.update({edge.a})
        return neighbours

    def MinEdge(self, v):
        current_min = None
        for edge in self.Edges:
            if edge.a == v or edge.b == v:
                if current_min == None or edge.weight < current_min.weight:
                    current_min = edge
        return current_min

    def RemoveEdge(self, e):
        self.Edges.remove(e)

    def RemoveVertex(self, v):
        self.Vertices.remove(v)
        newEdges = {}
        for edge in self.Edges:
            if not (edge.a == v or edge.b == v):
                newEdges.update({edge})
        self.Edges=newEdges


    def __repr__(self):
        return(str(self.Edges) +str(self.Vertices))

    # Optional problems!!
    def FindParentPath(self,vertex,parents):
        out_list = []
        past_state = parents.pop(vertex)
        while past_state != None:
            vertex = past_state
            out_list.insert(0,vertex)
            past_state = parents.pop(vertex)
        return out_list

    def DFS(self, start_vertex, target_vertex):
        frontier = [start_vertex]
        lenFrontier = 1
        discovered = set({start_vertex})
        parents = {start_vertex: None}
        while lenFrontier > 0:
            current_state = frontier.pop(0)
            lenFrontier -= 1
            discovered.add(current_state)
            if current_state == target_vertex:
                return self.FindParentPath(current_state,parents)
            neighbours = self.Neighbours(current_state)
            if neighbours != None:
                for vertex in self.Neighbours(current_state):
                    if vertex not in discovered:
                        frontier.insert(0,vertex)
                        lenFrontier += 1
                        discovered.add(vertex)
                        parents.update({vertex : current_state})
        return None

    def ChromaticNumber(self):
        colourSet = set()
        for vertex in self.Vertices:
            if vertex.colour == 0:
                return None
            elif vertex.colour not in colourSet:
                colourSet.add(vertex.colour)
        return len(colourSet)

    def isValidColouring(self):
        for edge in self.Edges:
            if edge.a.colour == edge.b.colour:
                return False
        return True

    def GreedyColour(self):
        for vertex in self.Vertices:
            if vertex.colour == 0:
                done = False
                neighbourColours = set()
                current_colour = vertex.colour
                for edge in self.Edges:
                    if edge.a == vertex:
                        neighbourColours.add(edge.b.colour)
                    elif edge.b == vertex:
                        neighbourColours.add(edge.a.colour)
                while not done:
                    current_colour += 1
                    if current_colour not in neighbourColours:
                        vertex.colour = current_colour
                        done = True

    def BruteForce(self):
        pass

    def IsTree(self):
        pass

    def IsPlanar(self):
        pass

    def FindEdge(self,vertexA,vertexB):
        for edge in self.Edges:
            if edge.a == vertexA:
                if edge.b == vertexB:
                    return edge
            if edge.b == vertexA:
                if edge.a == vertexB:
                    return edge
        return None

    def SpanningTree(self):
        start_vertex = next(iter(self.Vertices))
        frontier = [start_vertex]
        discovered = set({start_vertex})
        T = set()
        while frontier:
            current_state = frontier.pop(0)
            discovered.add(current_state)
            neighbours = self.Neighbours(current_state)
            if neighbours != None:
                for vertex in self.Neighbours(current_state):
                    if vertex not in discovered:
                        frontier.insert(0,vertex)
                        discovered.add(vertex)
                        T.add(self.FindEdge(current_state,vertex))
        return T

    def PrimMST(self):
        current_vertex = next(iter(self.Vertices))
        G = Graph(set({current_vertex}),set())
        done = False
        while not done:
            neighbours = set()
            for vertex in self.Vertices:
                if vertex not in G.Vertices:
                    neighbours.add(vertex)
            if len(neighbours)<=0:
                done = True
            if not done:
                neighbour_edges = set()
                for vertex in iter(neighbours):
                    for start_vertex in G.Vertices:
                        edge = self.FindEdge(vertex,start_vertex)
                        if edge != None:
                            neighbour_edges.add(edge)
                current_min = next(iter(neighbour_edges))
                for edge in neighbour_edges :
                    if edge.weight<current_min.weight:
                        current_min = edge
                G.Edges.add(current_min)
                G.Vertices.add(current_min.a)
                G.Vertices.add(current_min.b)
        return G.Edges

    def KruskalMST(self):
        F = Graph(self.Vertices,set())
        S = self.Edges
        while len(S) > 0 and not F.IsConnected():
            current_min = next(iter(self.Edges))
            for edge in S:
                if current_min.weight > edge.weight:
                    current_min = edge
            S.remove(current_min)
            if not F.DFS(current_min.a,current_min.b):
                F.Edges.add(current_min)
        return F.Edges

    def IsConnected(self):
        for vertex in self.Vertices:
            for vertex2 in self.Vertices:
                return bool(self.DFS(vertex,vertex2))

    def SamMST(self):
        return self.Edges




v1 = Vertex("a")
v2 = Vertex("b")
v3 = Vertex("c")
v4 = Vertex("d")
v5 = Vertex("e")
v6 = Vertex("f")
v7 = Vertex("g")
v8 = Vertex("h")
v9 = Vertex("i")
v10 = Vertex("j")
e1 = Edge(v1, v2, 3)
e2 = Edge(v1, v3, 4)
e3 = Edge(v1, v5, 10)
e4 = Edge(v1, v6, 18)
e5 = Edge(v2, v3, 1)
e6 = Edge(v2, v4, 5)
e7 = Edge(v2, v5, 9)
e8 = Edge(v3, v4, 4)
e9 = Edge(v4, v5, 7)
e10 = Edge(v4, v7, 9)
e11 = Edge(v4, v10, 9)
e12 = Edge(v5, v6, 8)
e13 = Edge(v5, v7, 8)
e14 = Edge(v5, v8, 9)
e15 = Edge(v6, v8, 9)
e16 = Edge(v6, v9, 9)
e17 = Edge(v7, v8, 2)
e18 = Edge(v7, v9, 2)
e19 = Edge(v8, v9, 4)
e19 = Edge(v8, v10, 3)
e20 = Edge(v9, v10, 6)

V = {v1, v2, v3, v4, v5, v6, v7, v8, v9, v10}
E = {e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20}

G = Graph(V, E)
runningmax =0
MST = G.KruskalMST()
print(MST)
for edge in MST:
    runningmax+=edge.weight
print(runningmax)
