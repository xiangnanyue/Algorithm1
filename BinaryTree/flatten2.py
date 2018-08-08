"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if root is None:
            return
        self.flag = None
        self.flatten_(root)
        
    
    
    def flatten_(self, node):
        if node is None:
            return
        if self.flag is not None:
            self.flag.right = node
            self.flag.left = None

        self.flag = node
        temp = node.right
        self.flatten_(node.left)
        self.flatten_(temp)
        
        
        
            
            
        