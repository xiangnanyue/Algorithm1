"""
description of Cartesian tree
https://en.wikipedia.org/wiki/Cartesian_tree

algorithm with stack:
https://www.cnblogs.com/lishiblog/p/4187936.html 
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        if len(nums) == 0:
            return None
        nums.append(float('inf'))
        stack = [TreeNode(nums[0])]
        for n in nums[1:]:
            if n < stack[-1].val:
                stack.append(TreeNode(n))
                continue
            newNode = TreeNode(n)
            subNode = stack.pop()
            while len(stack) > 0: 
                if stack[-1].val < n:
                    stack[-1].right = subNode
                    subNode = stack.pop()
                else:
                    break
            newNode.left = subNode
            stack.append(newNode)
            
        return stack.pop().left   