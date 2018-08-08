"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True
        return self.helper_(root)[0]
        
    def helper_(self, root):
        if root.left is None and root.right is None:
            return True, root.val, root.val
        if root.left is None:
            isrightBST, rightmax, rightmin = self.helper_(root.right)
            if isrightBST and root.val < rightmin:
                return True, rightmax, root.val
            else:
                return False, None, None
        if root.right is None:    
            isleftBST, leftmax, leftmin = self.helper_(root.left)
            if isleftBST and root.val > leftmax:
                return True, root.val, leftmin
            else:
                return False, None, None
        isleftBST, leftmax, leftmin = self.helper_(root.left)
        isrightBST, rightmax, rightmin = self.helper_(root.right)    
        
        if isleftBST and isrightBST and leftmax < root.val and root.val < rightmin:
            return True, rightmax, leftmin
        else:
            return False, None, None