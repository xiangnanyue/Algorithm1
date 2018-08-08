class ConnectingGraph3:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.lis = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]
        self.num = n
        
    def root(self, a):
        node = a
        while self.lis[node] != node:
            self.lis[node] = self.lis[self.lis[node]]
            node = self.lis[node]
        return node

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        if a == b:
            return 
        rootb = self.root(b)
        roota = self.root(a)
        
        if roota == rootb:
            return 
        
        if self.size[rootb] < self.size[roota]:
            self.lis[rootb] = roota 
            self.size[roota] += self.size[rootb]
        else:
            self.lis[roota] = rootb
            self.size[rootb] += self.size[roota]
        self.num -= 1
        
    """
    @return: An integer
    """
    def query(self):
        # write your code here
        #print(self.lis)
        return self.num
            
