class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        #find union algorithm
        dic = dict()
        trace = dict()
        maxv = 1
        for n in num:
            dic[n] = True
        for i,n in enumerate(num):
            if trace.get(n) is not None:
                continue
            freq = 1
            trace[n] = True
            k = n
            while dic.get(k-1) is not None and trace.get(k-1) is None:
                k = k-1
                trace[k] = True
                freq += 1
            k = n
            while dic.get(k+1) is not None and trace.get(k+1) is None:
                k = k+1
                trace[k] = True
                freq += 1
            maxv = max(maxv, freq)
        return maxv
        
                