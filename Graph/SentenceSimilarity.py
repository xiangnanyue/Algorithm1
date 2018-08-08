class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        l1 = len(words1)
        l2 = len(words2)
        if l1 != l2:
            return False
            
        dic = {}
        enc_map = {}
        idx = 0
        for i in pairs:
            pword, qword = i[0], i[1]
            if enc_map.get(pword) is None:
                enc_map[pword] = idx
                idx += 1
            if enc_map.get(qword) is None:
                enc_map[qword] = idx
                idx += 1
                
            p, q = enc_map[pword], enc_map[qword]
            
            if dic.get(p) is None:
                dic[p] = {}
            if dic.get(q) is None:
                dic[q] = {}
            dic[p][q] = 1
            dic[q][p] = 1
        
        for j in range(l1):
            word1 = enc_map[words1[j]]
            word2 = enc_map[words2[j]]
            neighbors1 = dic[word1]

            if neighbors1.get(word2) is None:
                return False
            else:
                continue
            
        return True

if __name__ == "__main__":
    w1 = ["great","acting","skills"]
    w2 = ["fine","drama","talent"]
    pairs = [["great","fine"],["drama","acting"],["skills","talent"]]