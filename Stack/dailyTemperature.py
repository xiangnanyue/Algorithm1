"""
Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
"""

class Solution:
    """
    @param temperatures: a list of daily temperatures
    @return: a list of how many days you would have to wait until a warmer temperature
    """
    def dailyTemperatures(self, temperatures):
        # Write your code here
        
        stack = []
        lis = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append([i,t])
                continue
            while stack[-1][1] < t:
                idx, temp = stack.pop()
                lis[idx] = i - idx
                if len(stack) == 0:
                    break
            stack.append([i, t])
        return lis

        