"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """
    def str2tree(self, s):
        # write your code here
        if len(s) == 0:
            return None
        lis = s.replace("(", " ( ").replace(")", " ) ").strip().split()
        root = TreeNode(int(lis.pop(0)))
        nodedic = {1:root}
        i = 1
        node = root
        while len(lis) > 0:
            c = lis.pop(0)
            print(c)
            if c == "(":
                if node.left is None:
                    i = 2*i
                    node.left = TreeNode(None)
                    node = node.left
                else:
                    i = 2*i+1
                    node.right = TreeNode(None)
                    node = node.right
            elif c == ")":
                i = int(i/2)
                node = nodedic[i]   # use the dic to record pointer...
            else:
                node.val = int(c)
                nodedic[i] = node
            
        return root
                
