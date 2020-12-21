import NodeGraph

class Graph:
    nodes = set()

    def __init__(self, nodes):
        for node in nodes:
            self.nodes.add(node)

    def add_node(self,node):
        assert node is NodeGraph
        self.nodes.add(node)