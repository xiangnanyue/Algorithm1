class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak1(self, s, dict):
        # write your code here
        # memory out of limit
        length = len(s)
        if length == 0:
            return True
        dict = {l:True for l in dict}
        mat = [[0]*length]
        for i in range(length):
            w = s[i]
            if dict.get(w) is not None:
                mat[0][i] = 1
            
        for k in range(1, length):
            for j in range(length-k):
                isword = dict.get(s[j:j+k+1]) is not None
                for i in range(1, k+1):
                    isword = isword or (mat[k-i][j] and mat[i-1][j+k-i+1])
                    if isword == True:
                        break
                mat[k][j] = 1 if isword else 0
        return True if mat[length-1][0] else False

    
    def wordBreak2(self, s, dict):
        # write your code here
        # time out of limit (back up too long)
        length = len(s)
        if length == 0:
            return True
        dict = {l:True for l in dict}
        mat = [False]*length
        mat[0] = dict.get(s[0]) is not None
        for i in range(1, length):
            print(mat)
            if dict.get(s[0:i+1]):
                mat[i] = True
                continue
            for j in range(i-1, -1, -1):
                isword = mat[j] and dict.get(s[j+1:i+1])
                if isword:
                    mat[i] = True
                    break
        return mat[length-1]

    def wordBreak(self, s, dict):
        # write your code here
        # this passed.
        length = len(s)
        if length == 0:
            return True
        dict = {l:True for l in dict}
        mat = [False]*length
        mat[0] = dict.get(s[0]) is not None
        for i in range(1, length):
            isword = False
            for word in dict.keys():
                l = len(word)
                if i-l+1 == 0 and word == s[i-l+1:i+1]:
                    mat[i] = True
                    break
                elif i-l+1 >0 and word == s[i-l+1:i+1] and mat[i-l]:
                    mat[i] = True
                    break
        return mat[length-1]

    