class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        l = len(s)
        if l == 0:
            return [[]]
        pat = self.isPalindrome(s)
        def f(n):
            if n == 0:
                return [[]]
            sol = []
            for j in range(1,n+1):
                if pat[n][j]:
                    sol += [lis+[s[j-1:n]] for lis in f(j-1)]
            return sol
        return f(l)

    """
    最长回文字串问题的线性解法。
    https://www.felix021.com/blog/read.php?2040 
    """
    def longestPalindrome(self, s):
        # write your code here
        length = len(s)
        if length == 0:
            return s
        pat = [[False]*(length+1) for j in range(length+1)]
        for k in range(1, length+1):
            pat[k][k] = True
        maxl = (1, (1,1))
        for j in range(1, length+1):
            for i in range(1, j):
                if i == j - 1:
                    pat[j][i] = (s[i-1]==s[j-1])
                else:
                    pat[j][i] = (s[i-1]==s[j-1]) and pat[j-1][i+1]
                if pat[j][i] and maxl[0] < j-i+1:
                    maxl = (j-i+1, (i,j))
        return s[maxl[1][0]-1:maxl[1][1]]