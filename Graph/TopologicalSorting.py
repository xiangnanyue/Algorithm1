"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        # a non-recursive version of topological sorting
        stack = []
        visitStack = []
        labelDict = {}  #visit dictionary
        for g in graph:
            if len(stack) == 0 and labelDict.get(g.label) is None:
                stack.append(g)
            while len(stack) > 0:
                #print([s.label for s in stack])
                visit = stack[-1]
                # check if node visited ? visited then delete from stack
                if labelDict.get(visit.label):
                    stack.pop()
                    continue
                # check the neighbors of node: if not visited, add to stack
                flag = 0
                for node in visit.neighbors:
                    if labelDict.get(node.label) is None:
                        stack.append(node)
                        flag = 1
                # check if neighbors unvisited not found, then pop out, and mark it 
                # as visited.
                if len(visit.neighbors) == 0 or flag == 0:
                    stack.pop()
                    visitStack.append(visit)
                    labelDict[visit.label] = True
                    
        return visitStack[::-1]


    def topSort2(self, graph):
        # write your code here
        # a recursive version
        visitStack = []
        labelDict = {}  #visit dictionary
        
        for g in graph:
            if labelDict.get(g.label) is None:
                visiting = {}
                self.dfs(g, visitStack, labelDict, visiting)
        return visitStack[::-1]
    
    def dfs(self, g, visitStack, visitDict, visiting):
        if visiting.get(g.label) == True:
            print("cycle found, not DAG")
            return False
        else:
            visiting[g.label] = True

        if len(g.neighbors) == 0:
            visitStack.append(g)
            visitDict[g.label] = True
            return
            
        for node in g.neighbors:
            if visitDict.get(node.label) is None:
                self.dfs(node, visitStack, visitDict, visiting)
        
        visitStack.append(g)
        visitDict[g.label] = True
        visiting[g.label] = False
                
                
            