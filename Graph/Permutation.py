class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        def copy_(lis):
            return [l for l in lis]
        
        def exchange_(a, b, lis):
            temp = lis[a]
            lis[a] = lis[b]
            lis[b] = temp
            
        length = len(nums)
        if length == 0:
            return [[]]
            
        stack = [Node_(nums, 0)]
        permutations = []
        while len(stack) > 0:
            node = stack.pop()
            if node.divide == length-1:
                permutations.append(node.lis)
                continue
            for i in range(node.divide, length):
                newlis = copy_(node.lis)
                exchange_(i, node.divide, newlis)
                stack.append(Node_(newlis, node.divide+1))
        return permutations
                
            
        
class Node_:
    def __init__(self, lis, div):
        self.divide = div
        self.lis = lis