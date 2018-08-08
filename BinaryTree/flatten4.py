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
        if root == None:
            return
        if root.left is not None:
            current_node = root.left
            while current_node.right is not None:
                current_node = current_node.right
            current_node.right = root.right
            root.right = root.left
            root.left = None
        self.flatten(root.right)
        return