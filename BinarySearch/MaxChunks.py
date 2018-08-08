"""
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk. After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

寻找波峰波谷
"""


class Solution:
    """
    @param arr: a permutation of N
    @return: the most number of chunks
    """
    def maxChunksToSorted(self, arr):
        # write your code here

        largest = arr[0]
        length = len(arr)
        chunck_dic = {}
        nb_chunks = 1
        for i in range(1, length):
            if arr[i] >= largest:
                nb_chunks += 1
                chunck_dic[i] = nb_chunks
                largest = arr[i]
            else:
                if arr[i] >= arr[i-1]:
                    chunck_dic[i] = chunck_dic[i-1]
                else:
                    chunck_dic[self.find_last_idx(arr[i])]
        return chunck_dic[length-1]
        
    def find_last_idx(self,val):
        pass