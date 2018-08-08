"""
给定一个包含 m x n 个要素的矩阵，（m 行, n 列），按照螺旋顺序，返回该矩阵中的所有要素。

给定如下矩阵：

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
应返回 [1,2,3,6,9,8,7,4,5]

"""

class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        # write your code here
        if len(matrix) == 0:
            return matrix
        m,n = len(matrix), len(matrix[0])
        trace = [[0]*(n+2) for i in range(m+2)]
        for i in range(n+2):
            trace[0][i] = 1
            trace[m+1][i] =1
        for j in range(m+2):
            trace[j][0] =1
            trace[j][n+1] =1
        trace[1][1] = 1
        #print(trace)
        lis = [matrix[0][0]]
        i, j = 0, 0
        d = 0
        flag = 0
        while flag < 2:
            if flag == 1:
                d += 1
                d = d%4
                
            if d == 0:
                i_, j_ = i, j+1
            elif d == 1:
                i_, j_ = i+1, j
            elif d == 2:
                i_, j_ = i, j-1
            else:
                i_, j_ = i-1, j
                
            if trace[i_+1][j_+1]==1:
                flag += 1
                continue
            else:
                i, j = i_, j_
                lis.append(matrix[i][j])
                trace[i_+1][j_+1] = 1
                flag = 0
        return lis
            
            
            
        