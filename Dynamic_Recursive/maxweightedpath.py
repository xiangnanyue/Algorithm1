"""
有一个机器人位于一个 m × n 个网格的右上角。
机器人每一时刻只能向下或者向左移动一步。机器人试图达到网格的左下角。每个网格上有一个数字权值，机器人希望它走到左下角的路径权值和最大。
问这个最大路径权值和是多少？

[
[1,2,3,4],
[3,5,6,7],
[9,10,1,2],
[4,4,5,5]
]
，返回45。

解释：
从右上角出发，沿着[4,7,6,5,10,9,4]走到左下角。权值和为45。
"""

class Solution:
    """
    @param nums: 
    @return: nothing
    """
    def maxWeight(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0

        m,n = len(nums), len(nums[0])
        trace = [[0]*n for j in range(m)]
        trace[0][n-1] = nums[0][n-1]
        for j in range(n-2, -1, -1):
            trace[0][j] = trace[0][j+1] + nums[0][j]
        for j in range(1, m):
            trace[j][n-1] = trace[j-1][n-1] + nums[j][n-1]
        for i in range(1, m):
            for j in range(n-2, -1, -1):
                trace[i][j] = max(trace[i-1][j], trace[i][j-1])+nums[i][j]
        return trace[m-1][0]

if __name__ == "__main__":
    nums = [[5,16,8,8,4],[6,0,4,0,5],[16,0,0,7,5],[15,6,5,14,16],[17,9,11,2,4]]
    sol = Solution()
    solution = sol.maxWeight(nums)
    print(solution)