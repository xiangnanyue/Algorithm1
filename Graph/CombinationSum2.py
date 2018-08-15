class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum2(self, candidates, target):
        # write your code here
        # cosntruct a 3d array
        # use broad first search
        self.target = target
        current = []
        curSum = 0
        rest = sorted(candidates)
        
        sols =[]
        self.traverse_(current, curSum, rest, sols)
        return sols
        
        
    def traverse_(self, current, curSum, rest, sols):
        
        if curSum == self.target:
            sols.append(current)
            return 
        if len(rest) == 0:
            return 
        
        previous = None
        for k, res in enumerate(rest):
            if res == previous:
                continue
            else:
                previous = res
                
            if curSum + res > self.target:
                return
            else:
                newCurrent = current + [res]
                newCurSum = curSum + res
                self.traverse_(newCurrent, newCurSum, rest[k+1:], sols)
                
                
                
                