class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False
        
        mat = [[False]*(l2+1) for i in range(l1+1)]
        mat[0][0] = True
        for i in range(1,l2+1):
            mat[0][i] = mat[0][i-1] and (s2[i-1] == s3[i-1])
        for i in range(1, l1+1):
            mat[i][0] = mat[i-1][0] and (s1[i-1] == s3[i-1])
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                mat[i][j] = (mat[i-1][j] and s1[i-1] == s3[i+j-1]) or (mat[i][j-1] and s2[j-1] == s3[i+j-1])
        return mat[l1][l2]