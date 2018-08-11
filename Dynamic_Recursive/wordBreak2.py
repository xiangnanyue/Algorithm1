class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    import copy
    
    def wordBreak(self, s, wordDict):
        # write your code here
        if len(wordDict) == 0:
            return []
        self.wdic = {w: True for w in wordDict}
        self.L = max([len(w) for w in wordDict])
        # use dynamic programming(word break) to decide whether we can divide
        if not self.canBreak(s):
            return []
        sols = []
        current = ""
        rest = s
        self.traverse_(current, rest, sols)
        return sols
    
    def canBreak(self, s):
        length = len(s)
        lis = [0]*(length+1)
        lis[0] = 1
        for i in range(1, length+1):
            for j in range(1, min(i, self.L)+1):
                # (i-1) - j + 1 ~ i-1
                if self.wdic.get(s[i-j:i]) is not None and lis[i-j]==1:
                    lis[i] = 1
                    break
        return lis[length]
        
    def traverse_(self, current, rest, sols):
        #print(current, rest)
        length = len(rest)
        if length == 0:
            sols.append(current.strip())
            return 
        
        for i in range(1, min(length,self.L)+1):
            string = rest[:i]
            if self.wdic.get(string) is not None:
                newcurrent = current + " " + string
                newrest = rest[i:]
                self.traverse_(newcurrent, newrest, sols)
        