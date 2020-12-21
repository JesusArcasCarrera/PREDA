class NodeGraph: 
    edges = set()
    
    # edges is a tuple, (other_node,'u|d|b',weigth)
    #u is undirected, d is directed, b is bidirectional
    def __init__(self,edges):
        for edge in edges:
            self.edges.add(edge)

    def add_edge(self,edge):
        if edge[1] is None or edge[1] not in ['u','d','b']:
            raise ValueError('direction must be "u|d|b"')           
        self.edges.add(edge)

    def remove_edge(self,edge):
        self.edges.discard(edge) 

    def remove_node(self,node):
        self.edges.discard(self.get_edge(node))

    def set_edge(self,node,direction=None,weight=None):
        edge = self.get_edge(node)
        if direction is not None and direction in ['u','d','b']:
            edge[1]=direction
        else:
            raise ValueError('direction must be "u|d|b"')
        if weight is not None:
            edge[2]=weight
    
    def get_edges(self):
        return self.edges
    
    def get_edge(self,node):
        return  [e for e in self.edges if e[0] is node]

    def get_by_direct(self,direction):
        direction.lower()
        return [e for e in self.edges if e[1]==direction]
    
    def get_by_weight(self,weight,op = 'equal'):
        ops = {
            'equal':lambda x:x==weight,
            'gretter':lambda x:x>weight,
            'less':lambda x:x<weight
        }
        return [e for e in self.edges if ops[op](e[2])]

    def filter_edges(self, f):
        return [e for e in self.edges if f(e)]
    
    def stay(self,edge):
        return self.edges.issuperset({edge})

    def stay_node(self,node):
        return self.stay(self.get_edge(node))    