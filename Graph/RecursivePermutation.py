class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
            
        length = len(nums)
        if length == 0:
            return [[]]
        
        permutations = []
        for n in range(length):
            newlis = [l for l in nums]
            self.exchange_(0, n, newlis)
            for lis in self.permute(newlis[1:]):
                permutations.append([newlis[0]] + lis)
        return permutations
        
        
    def exchange_(self, a, b, lis):
            temp = lis[a]
            lis[a] = lis[b]
            lis[b] = temp