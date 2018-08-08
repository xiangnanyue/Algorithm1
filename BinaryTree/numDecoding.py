class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        length = len(s)
        
        mat = [[0]*length for i in range(length)]
        num2letter = lambda x:chr(x+ord("@")) if x>0 and x<27 else None
        def decode(x):
            if x[0]=="0":
                return 0
            return 1 if int(x)>0 and int(x)<27 else 0
            
        if length == 0:
            return 0
        if length == 1:
            return decode(s)
        
        # mat[i][j] = mat[i-1][j]*decode(s[i+j]) + mat[i-2][j]*decode(s[j+i-1:]) 
        # mat[i-1][j+1]*decode(s[j]) + mat[i-2][j+2]*decode(s[j:j+2])
        for j in range(length):
            mat[0][j] = decode(s[j])
        for j in range(length-1):
            mat[1][j] = mat[0][j]*decode(s[j+1]) + decode(s[j:j+2])
        for i in range(2, length):
            for j in range(length-i):
                mat[i][j] = mat[i-1][j]*decode(s[j+i]) + mat[i-2][j]*decode(s[j+i-1:j+i+1]) 
                
        return mat[length-1][0]
            