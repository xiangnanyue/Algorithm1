class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, targer):
        # write your code here
        # broad first better ?
        self.k = k
        self.target = targer
        cSum = 0
        current = []
        rest = A
        sols = []
        self.dfs(current, rest, cSum, sols)
        
        return sols
        
    def dfs(self, current, rest, cSum, sols):
        
        if len(current) == self.k:
            if cSum == self.target:
                sols.append(current)
            return

        for t,i in enumerate(rest):
            newcurrent = current + [i]
            newSum = cSum + i
            self.dfs(newcurrent, rest[t+1:], newSum, sols)