class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i, j = 0, len(s)-1
        while i<j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i +=1 
            j -= 1
        return "".join(s)
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0
        j = len(s)-1
        dic = {k:1 for k in "AEIOUaeiou"}
        
        while i < j :
            if dic.get(s[i]) is None:
                i += 1
                continue
            if dic.get(s[j]) is None:
                j -= 1
                continue
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
            
        return "".join(s)
    