class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # use a global variable for recursive reason
        self.leftlast = float("-inf")
        return self.helper_(root)
        
    def helper_(self, root):
        if root is None:
            return True
        if not self.helper_(root.left):
            return False
        if root.val <= self.leftlast:
            return False
        self.leftlast = root.val
        if not self.helper_(root.right):
            return False
        return True

