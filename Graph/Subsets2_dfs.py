class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        nums = sorted(nums)
        subset = [[]]
        self.traverse_(nums, [], subset)
        return subset
        
    def traverse_(self, rest, lis, subset):
        for i in range(len(rest)):
            if i > 0 and rest[i] == rest[i-1]:
                continue
            newrest = rest[i+1:]
            newlis = lis + [rest[i]]
            subset.append(newlis)
            self.traverse_(newrest, newlis, subset)