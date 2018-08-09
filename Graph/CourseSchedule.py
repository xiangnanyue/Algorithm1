class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        # out of memory limit problem
        
        self.linklist = {n:[] for n in range(numCourses)}
        for p, q in prerequisites:
            self.linklist[q].append(p)
        
        visited = {}
        for n in range(numCourses):
            if visited.get(n) is None:
                visiting = {}
                if self.hasCycle(n, visited, visiting):
                    return False
        return True
        
    def hasCycle(self, n, visited, visiting):
        #print(n, self.linklist[n])
        if visiting.get(n) == True:
            return True
        else:
            visiting[n] = True
        
        for i in self.linklist[n]:
            if visited.get(i) is None:
                if self.hasCycle(i, visited, visiting):
                    return True
        
        visited[n] = True
        visiting[n] = False
        return False
        
            
            
                    
        
