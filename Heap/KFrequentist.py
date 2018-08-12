class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # write your code here
        
        def exch_(a, b, lis):
            temp = lis[a]
            lis[a] = lis[b]
            lis[b] = temp
            
        def lessthan_(leftchild, rightchild, lis):
            if lis[leftchild][1] < lis[rightchild][1]:
                return True
            elif lis[leftchild][1] > lis[rightchild][1]:
                return False
            elif lis[leftchild][1] == lis[rightchild][1]:
                if lis[leftchild][0] > lis[rightchild][0]:
                    return True
                else:
                    return False
            else:
                return False
                
            
        dic = {}
        for word in words:
            if dic.get(word) is None:
                dic[word] = 1
            else:
                dic[word] += 1
                
        lis = [(None, 0)]
        for word, value in dic.items():
            l = len(lis)
            lis.append((word, value))
            parent = int(l/2)
            while parent > 0 and lessthan_(parent, l, lis):
                exch_(parent, l, lis)
                l = parent
                parent = int(parent/2)
        print(lis)
        
        #lis.pop(0)
        stack = []
        for i in range(k):
            exch_(1, len(lis)-1, lis)
            stack.append(lis.pop()[0])
            # sink
            current = 1
            leftchild = 2*current
            rightchild = 2*current + 1
            while leftchild < len(lis):
                if rightchild <len(lis) and lessthan_(leftchild,rightchild,lis):
                    larger = rightchild
                else:
                    larger = leftchild
                if lessthan_(current, larger, lis):
                    exch_(larger, current, lis)
                    
                current = larger
                leftchild = 2*current
                rightchild = 2*current + 1
        return stack 


if __name__ == "__main__":
    inputlist = ["yes","lint","code","yes","code","baby","you","baby","chrome","safari","lint","code","body","lint","code"]
    k = 3
    sol = Solution()
    words = sol.topKFrequentWords(inputlist, 3)
    print(words)