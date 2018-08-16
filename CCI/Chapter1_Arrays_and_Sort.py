

##
# 1.2 check permutation
#

class Solution1_2(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        sols = []
        curr = []
        res = nums
        
        self.traverse_()

#
# 1.3 URLify
#
class Solution1_3(object):
    def urlify(self, string):
        i = 0
        string = string.strip()
        while i < len(string):
            if string[i] == " ":
                j = i+1
                while j < len(string):
                    if string[j] == " ":
                        j += 1
                    else:
                        break
                string = string[:i]+"%20"+string[j:]
            i += 1
        return string

    @staticmethod
    def test_():
        string = "Mr John Smith   "
        sol = Solution1_2()
        print(sol.urlify(string))

#
# Ex. https://leetcode.com/problems/encode-and-decode-tinyurl/description/
# Sol https://medium.com/@roger35972134/leetcode-535-encode-and-decode-tinyurl-90113d08b1c
class Codec:
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        pass

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        pass

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



#
#1.5 one away distance 
#https://www.lintcode.com/problem/one-edit-distance/description
#
class Solution1_5(object):

    def isOneEditDistance1(self, s, t):
        # write your code here
        # this will get memory limit exceed 
        return self.minDistance(s, t) == 1

    
    def isOneEditDistance2(self, s, t):
        # write your code here
        l1, l2 = len(s), len(t)
        if abs(l1 - l2) > 1:
            return False
            
        for i in range(min(l1, l2)):
            if t[i] == s[i]:
                continue
            #add or substract or replace
            return t[i:] == s[i+1:] or t[i+1:] == s[i:] or t[i+1:] == s[i+1:]
        # exactly the same
        if l1 == l2:
            return False
        elif abs(l1 - l2) == 1:  #else
            return True

    # ex: https://leetcode.com/problems/edit-distance/description/
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        mat = [[0]*(l2+1) for i in range(l1+1)]

        for i in range(l1+1):
            mat[i][0] = i
        for j in range(l2+1):
            mat[0][j] = j 
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                mat[i][j] = mat[i-1][j-1] if word1[i-1]==word2[j-1] else min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1])+1
        return mat[l1][l2]

#
#1.6 string compression
#https://leetcode.com/problems/string-compression/description/

class Solution1_6(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        length = len(chars)
        if length < 1:
            return chars
        
        i = 0
        while i < len(chars):
            j = i+1
            rep = 1
            while j < len(chars):
                if chars[j] == chars[i]:
                    chars.pop(j)
                    rep += 1
                else:
                    break
            if rep > 1:
                for r in str(rep):
                    chars.insert(j, r)
                    j += 1
            i = j
        return len(chars)

# https://www.lintcode.com/problem/encode-and-decode-strings/description
# use a method to encode and then to decode a string
class EncoderDecoder:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        #self.prim = 24319
        def encoding_(string):
            return str(len(string))+"#"+string
        return "".join(list(map(encoding_, strs)))

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        if len(str) == 0:
            return []
        
        str = list(str)
        strings = []
        while len(str) > 0:
            nums = []
            next = str.pop(0)
            while next != "#":
                nums.append(next)
                next = str.pop(0)
            digits = int("".join(nums))
            strings.append("".join(str[:digits]))
            str = str[digits:]
        return strings
    
#
#1.7 rotate matrix
#https://leetcode.com/problems/rotate-image/description/
#

class Solution1_7(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        
        m = len(matrix) - 1
        # if m == 2
        # (0, 1) -> (1, 2-0) -> (2, 2-1) -> (1, 2-2)
        # (i, j) -> (j, m-i) -> (m-i, m-j) -> (m-j, i)

        pass


#
#1.8 set zero matrix
# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution1_8(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        
        r, c = len(matrix), len(matrix[0])
        
        rows = set()
        cols = set()
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for l in range(c):
                matrix[i][l] = 0
        for j in cols:
            for l in range(r):
                matrix[l][j] = 0


#
#1.9 string rotation
#


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution1_9:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        
        node = head
        
        if node is None:
            return node
        if node.next is None:
            return node
            
        num = 1
        lis = [head]
        while node.next is not None:
            node = node.next
            num += 1
            lis.append(node)
        k =k%num
        node.next = head
        lis[num-k-1].next = None  # cannot forget this
        
        return lis[(num-k)%num]   #and the special case k=0




if __name__ == "__main__":
    Solution1_3.test_()