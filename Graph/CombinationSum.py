class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        # cosntruct a 3d array
        # use broad first search
        self.target = target
        current = []
        curSum = 0
        rest = sorted(list(set(candidates)))
        
        sols =[]
        self.traverse_(current, curSum, rest, sols)
        return sols
        
        
    def traverse_(self, current, curSum, rest, sols):
        
        if curSum == self.target:
            sols.append(current)
            return 
        
        
        for k, res in enumerate(rest):
            if curSum + res > self.target:
                return
            else:
                newCurrent = current + [res]
                newCurSum = curSum + res
                self.traverse_(newCurrent, newCurSum, rest[k:], sols)