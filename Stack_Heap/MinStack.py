class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.mini = []
        self.idx = 0
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        #print(self.stack, self.mini)
        
        if len(self.stack) == 0:
            self.mini.append(self.idx)
        else:
            if self.stack[self.mini[-1]] > number:
                self.mini.append(self.idx)
            else:
                self.mini.append(self.mini[-1])
        self.idx += 1        
        self.stack.append(number)
        
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.idx -= 1
        self.mini.pop()
        return self.stack.pop()
        
    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.stack[self.mini[-1]]