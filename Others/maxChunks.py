class Solution:
    """
    @param arr: a permutation of N
    @return: the most number of chunks
    """
    def maxChunksToSorted(self, arr):
        # write your code here
        maxr = -1
        chunks = 0
        for i,a in enumerate(arr):
            if a > maxr:
                maxr = a
            if i == maxr:
                chunks += 1
        return chunks
        
            