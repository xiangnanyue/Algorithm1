"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        # write your code here
        if root is None:
            return None
        root_ = TreeNode(root.val)
        
        root_.left = self.cloneTree(root.left)
        root_.right = self.cloneTree(root.right)
        return root_