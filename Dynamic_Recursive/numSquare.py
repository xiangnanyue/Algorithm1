class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        # example is 32
        lis = [0]*(n+1)
        lis[0] = 0
        lis[1] = 1
        for i in range(2,n+1):
            sqr = int(i**(0.5))
            minnum = i
            for j in range(1, sqr+1):
                minnum = min(minnum, 1+lis[i-j*j])
            lis[i] = minnum
        return lis[n]
