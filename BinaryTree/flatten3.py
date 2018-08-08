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
        self.flag = root
        # important to understand, assign pointer of right node
        # to right variable. thus save the address in order not to lose it.
        right = root.right
        left = root.left
        
        root.right = root.left
        root.left = None
        
        self.flatten(left)
        self.flag.right = right
        self.flatten(right)
        
        
        
            
            
        