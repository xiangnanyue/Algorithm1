"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Ref: https://en.wikipedia.org/wiki/3SUM 
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        dic = {}
        for i,k in enumerate(nums):
            if dic.get(k) is None:
                dic[k] = []
            dic[k] += [i]
        
        sol = []
        for n in range(l):
            for i in range(n+1,l):
                g = -(nums[i] + nums[n])
                if dic.get(g) is None:
                    continue
                for l in dic.get(g):
                    if l > i:
                        sol.append([nums[n], nums[i], nums[l]])
        return sol

        def threeSum2(self, nums):
            """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        dic = {}
        for i,k in enumerate(nums):
            if dic.get(k) is None:
                dic[k] = 0
            dic[k] += 1
        
        sol = []
        vals = dic.keys()
        lv = len(vals)
        for n in range(lv):
            if dic[vals[n]] == 2 and dic.get(-2*vals[n]) is not None:
                sol.append([vals[n], vals[n], -2*vals[n]])
            for i in range(n+1,lv):
                g = -(vals[i] + vals[n])
                if dic.get(g) is None:
                    continue
                if (vals[n]==g or g==vals[i]):
                    continue
                sol.append([vals[n], vals[i], g])
        return sol