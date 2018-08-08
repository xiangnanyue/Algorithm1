"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if root is None:
            return "#"
        getString = lambda x:"#" if x is None else str(x.val)
        pipe = [root]
        string = []
        while len(pipe)>0:
            node = pipe.pop()
            string.append(getString(node))
            print(string)
            if node is None:
                continue
            #if node.left is None and node.right is None and len(pipe)==0:
            #    continue
            pipe.insert(0, node.left)
            pipe.insert(0, node.right)
        
        for s in string[::-1]:
            if s == "#":
                string.pop()
            else:
                break
        return " ".join(string)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        data = data.strip().split()[::-1]
        getValue = lambda s:TreeNode(int(s)) if s!="#" else None
        root = getValue(data.pop())
        pipe = [root]
        """
        while len(data) > 0:
            print(data)
            node = pipe.pop()
            if node is None:
                continue
            node.left = getValue(data.pop())
            # this is bizare, need to be optimised
            if len(data) == 0:
                break
            node.right = getValue(data.pop())
            pipe.insert(0, node.left)
            pipe.insert(0, node.right)
        """
        while len(pipe) > 0:
            node = pipe.pop()
            if node is None:
                continue
            if len(data) > 0:
                node.left = getValue(data.pop())
                pipe.insert(0, node.left)
                if len(data) > 0:
                    node.right = getValue(data.pop())
                    pipe.insert(0, node.right)
            
        return root
        