class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # write your code here
        A.insert(0, 0)
        
        def exch_(x, y, lis):
            temp = lis[x]
            lis[x] = lis[y]
            lis[y] = temp
        
        for l in range(1, len(A)):
            parentIdx = int(l/2.)
            a = A[l]
            while  parentIdx > 0 and A[parentIdx] > a:
                exch_(parentIdx, l, A)
                l = int(l/2.)
                parentIdx = int(l/2.)
                
        A.pop(0)
        return A