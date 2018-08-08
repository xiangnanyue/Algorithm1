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
        node_ = root_
        lis = [0]
        pip = [root]
        pip_ = [root_]
        
        while len(pip) > 0:
            node = pip.pop()
            node_ = pip_.pop()
            
            if node is None:
                lis.append(None)
                continue
            lis.append(node.val)
            
            if node.right is None and node.left is None:
                continue
            if node.right is not None:
                pip.append(node.right)
                node_.right = TreeNode(node.right.val)
                pip_.append(node_.right)
            if node.left is not None:
                pip.append(node.left)
                node_.left = TreeNode(node.left.val)
                pip_.append(node_.left)
        print(lis)
            
        return root_
                