class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # this solution will get time limit pass O(2^n)
        self.length = len(triangle)
        if self.length == 0:
            return 0
        self.dic = dict()
        i = 0
        j = 0
        return self.getMinimum(i, j, triangle)
        
    def getMinimum(self, i, j, triangle):
        if i == self.length-1:
            return triangle[i][j]
        if self.dic.get((i,j)) is None:
            left = self.getMinimum(i+1, j, triangle)
            right = self.getMinimum(i+1, j+1,triangle)
            self.dic[(i,j)] = min(left,right) + triangle[i][j]
        
        return self.dic.get((i,j))
        
    def minimumTotal2(self, triangle):
        """
        dynamic programming: traverse / divide and conquer

        自底向上的循环 动态规划
        """
        length = len(triangle)
        if length == 1:
            return triangle[0][0]

        mat = [[0]*length for i in range(length)]
        mat[length-1] = triangle[-1]
        for j in range(length-2, -1, -1):
            for i in range(j+1):
                mat[j][i] = min(mat[j+1][i], mat[j+1][i+1])+triangle[j][i]
        return mat[0][0]


"""
try recursive:
KSum
longest consecutive list
subset
...
try DP:
matrix DP
Sequence 
two sequence dp
backpack

exercises:
https://www.lintcode.com/problem/climbing-stairs/description
https://www.lintcode.com/problem/max-chunks-to-make-sorted/description
https://www.lintcode.com/problem/spiral-matrix/description
https://www.lintcode.com/problem/subsets-ii/description
https://www.lintcode.com/problem/daily-temperatures/description

"""