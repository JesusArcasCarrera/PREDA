class NodeGraph: 
    edges = {}
    
    # edges is a tuple, (other_node,'u|d|b',weigth)
    #u is undirected, d is directed, b is bidirectional
    def __init__(self,edges):
        self.edges = edges

    def addEdge(self,edge):
        if edge[1] is None or edge[1] not in ['u','d','b']:
            raise ValueError('direction must be "u|d|b"')           
        self.edges.add(edge)

    def removeEdge(self,edge):
        self.edges.discard(edge) 

    def removeNode(self,node):
        self.edges.discard(self.getEdge(node))

    def setEdge(self,node,direction=None,weight=None):
        edge = self.getEdge(node)
        if direction is not None and direction in ['u','d','b']:
            edge[1]=direction
        else:
            raise ValueError('direction must be "u|d|b"')
        if weight is not None:
            edge[2]=weight
    
    def getEdges(self):
        return self.edges
    
    def getEdge(self,node):
        return  [e for e in self.edges if e[0] is node]

    def getByDirect(self,direction):
        direction.lower()
        return [e for e in self.edges if e[1]==direction]
    
    def getByWeight(self,weight,op = 'equal'):
        ops = {
            'equal':lambda x:x==weight,
            'gretter':lambda x:x>weight,
            'less':lambda x:x<weight
        }
        return [e for e in self.edges if ops[op](e[2])]

    def filterEdges(self, f):
        return [e for e in self.edges if f(e)]
    
    def stay(self,edge):
        return self.edges.issuperset({edge})

    def stayNode(self,node):
        return self.stay(self.getEdge(node))    