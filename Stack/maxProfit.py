class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        
        if len(prices) == 0:
            return 0
        stack = []
        maxv = 0
        for p in prices:
            if len(stack) == 0:
                stack.append(p)
                continue
            
            if len(stack) > 0:
                if stack[-1] >= p:
                    stack.append(p)
                else:
                    maxv = max(p-stack[-1], maxv) 
        return maxv