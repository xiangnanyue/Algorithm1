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
        self.leftlast = None
        self.tree_last(root)
    
    def tree_last(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        if root.left is None and root.right is not None:
            return self.tree_last(root.right)
        if root.right is None and root.left is not None:
            root.right = root.left
            return self.tree_last(root.left)
        self.leftlast = self.tree_last(root.left)
        self.rightlast = self.tree_last(root.right)
        self.leftlast.right = root.right
        root.right = root.left
        return self.rightlast
        
        
        
        
            
            
        