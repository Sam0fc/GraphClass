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
        print("Unsolvable.")

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
        neighbours = set()
        while not done:
            for vertex in self.Vertices:
                if vertex not in G.Vertices:
                    neighbours.add(vertex)
                if not neighbours:
                    done = True
            if not done:
                neighbour_edges = set()
                for vertex in neighbours:
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





a = Vertex("a")
b = Vertex("b")
c = Vertex("c")
e1 = Edge(a, b, 3)
e2 = Edge(a, c, 0.5)
V = {a, b, c} # the vertex set
E = {e1, e2}
G = Graph(V, E)
print(G.PrimMST())
print(G)
