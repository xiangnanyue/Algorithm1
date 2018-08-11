class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if len(nums) == 0:
            return [[]]
        nums = sorted(nums)
        newNum = nums[-1]
        l = len(nums)-2
        while l>=0:
            if nums[l] == newNum:
                l -= 1
            else:
                break
        l += 1
        newEles = nums[l:]
        left = self.subsetsWithDup(nums[:l])
        #print(left)
        complements = []
        for i in range(len(newEles)):
            complements += [lis+newEles[0:i+1] for lis in left]
        return left + complements