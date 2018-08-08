"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.current = root
        self.stack = []
        
    """
    @return: True if there has next node, or false
    """
    def hasNext(self,):
        # write your code here
        if self.current is None and len(self.stack) == 0:
            return False
        else:
            return True

    """
    @return: return next node
    """
    def next(self,):
        # write your code here
        while self.current is not None:
            self.stack.append(self.current)
            self.current = self.current.left
            
        node = self.stack.pop()
        self.current = node.right
        return node
