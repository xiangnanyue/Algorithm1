"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    def __init__(self):
        self.nodes = dict()
        self.edges = dict()
    
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        print(node.label, node.neighbors)
        if node is None:
            return None
        
        stack = [node]
        while len(stack) > 0:
            new = stack.pop()
            if self.nodes.get(new.label) is None:
                self.nodes[new.label] = UndirectedGraphNode(new.label)
                self.edges[new.label] = {}
             
            for n in new.neighbors:
                if self.nodes.get(n.label) is None:
                    self.nodes[n.label] = UndirectedGraphNode(n.label)
                    self.edges[n.label] = {}
                    
                if self.edges[new.label].get(n.label) is None:
                    self.nodes[new.label].neighbors.append(self.nodes[n.label])
                    self.nodes[n.label].neighbors.append(self.nodes[new.label])
                    self.edges[new.label][n.label] = True
                    self.edges[new.label][n.label] = True
                stack.append(n)
        return self.nodes[node.label]