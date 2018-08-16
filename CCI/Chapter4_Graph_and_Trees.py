
#4.1 route between Nodes
#

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution4_1:
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """

    def hasRoute(self, graph, s, t):
        # write your code here
        if s.label == t.label:
            return True
        visited = {}
        stack = []
        
        stack.append(s)
        visited[s.label] = True
        
        while len(stack) > 0:
            visitingnode = stack.pop()
            for n in visitingnode.neighbors:
                if n.label == t.label:
                    return True
                if visited.get(n.label) is None:
                    stack.append(n)
                    visited[n.label] = True
                
        return False


#4.2 minimal tree
#
#

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution4_2:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        # balanced BST ?
        length = len(A)
        if length == 0:
            return None
        
        mid = int(length/2) if length%2==1 else int(length/2)-1
        node = TreeNode(A[mid])
        node.left = self.sortedArrayToBST(A[:mid])
        node.right = self.sortedArrayToBST(A[mid+1:])
        
        return node


#
#4.3 List of Depths
#

