class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        stack = []
        stack.append([start,1])
        dic = {k:True for k in dict}
        ladder = 0
        
        while len(stack) > 0:
            #print(stack)
            cur, ladder = stack.pop()

            if cur == end:
                return ladder
            
            # think: why it cannot pass if I put here:
            # dic[onestep] = False 
            for i in range(len(cur)):
                part1, part2 = cur[:i], cur[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if cur[i] != j:
                        onestep = part1+j+part2
                        if dic.get(onestep) == True:
                            stack.insert(0, [onestep, ladder+1])
                            dic[onestep] = False
        return 0

    def ladderLength2(self, start, end, dict):
        # write your code here
        dict.add(end)
        dic = {k:True for k in dict}
        
        wordLen = len(start)
        queue = collections.deque([(start, 1)])
        while queue:
            curr = queue.popleft()
            currWord = curr[0]; currLen = curr[1]
            if currWord == end: return currLen
            for i in range(wordLen):
                part1 = currWord[:i]; part2 = currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currWord[i] != j:
                        nextWord = part1 + j + part2
                        if dic.get(nextWord) == True:
                            queue.append((nextWord, currLen + 1))
                            dic[nextWord] = False
                            
        return 0
    
    def ladderLength3(self, start, end, dict):
        # write your code here
        dict.add(end)
        dic = {k:True for k in dict}
        
        wordLen = len(start)
        queue = []
        queue.append([start, 1])
        while queue:
            curr = queue.pop()
            currWord = curr[0]; currLen = curr[1]
            if currWord == end: return currLen
            for i in range(wordLen):
                part1 = currWord[:i]; part2 = currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currWord[i] != j:
                        nextWord = part1 + j + part2
                        if dic.get(nextWord) == True:
                            queue.insert(0,[nextWord, currLen + 1])
                            dic[nextWord] = False
                            
        return 0
                        
                        
                        
                    