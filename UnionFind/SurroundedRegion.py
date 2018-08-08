# -- coding: utf-8 --

"""
Percolation Problem

给出二维矩阵：

X X X X
X O O X
X X O X
X O X X
把被 'X' 围绕的区域填充之后变为：

X X X X
X X X X
X X X X
X O X X
"""
class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        if len(board) == 0:
            return 
        self.length, self.width = len(board), len(board[0])
        l, w = self.length, self.width
        self.lis = [i for i in range(l*w+1)]
        self.dummy = l*w
        
        for j in range(w):
            self.lis[0*w+j] = self.dummy
            self.lis[(l-1)*w+j] = self.dummy
        for i in range(l):
            self.lis[i*w] = self.dummy
            self.lis[i*w+w-1] = self.dummy
        
        for i in range(1,l-1):
            for j in range(1,w-1):
                if board[i][j] == "O":
                    self.checkSurrounded(board,i,j)

        for i in range(l):
            for j in range(l):
                if self.root(i, j) != self.dummy: 
                    board[i] = board[i][:j]+"X"+board[i][j+1:]
        return board

    def checkSurrounded(self, board, i, j):
        for k,l in [(i, j+1), (i, j-1), (i+1, j), (i-1,j)]:
            if board[k][l] == "O":
                self.connect(k,l,i,j)

    def connect(self, k, l, i, j):
        if k == i and l == j:
            return 
        root1 = self.root(k,l)
        root2 = self.root(i,j)
        if root1 == root2:
            return
        if root1 == self.dummy:
            self.lis[root2] = self.dummy
        elif root2 == self.dummy:
            self.lis[root1] = self.dummy
        else:
            self.lis[root1] = root2            

    def root(self, p, q):
        idx = p*self.width+q
        while self.lis[idx] != idx:
            self.lis[idx] = self.lis[self.lis[idx]]
            idx = self.lis[idx]
        return idx


if __name__ == "__main__":
    board = ["XOOXXXOXOO","XOXXXXXXXX","XXXXOXXXXX","XOXXXOXXXO","OXXXOXOXOX","XXOXXOOXXX","OXXOOXOXXO","OXXXXXOXXX","XOOXXOXXOO","XXXOOXOXXO"]
    sol = Solution()
    newboard = sol.surroundedRegions(board)
    print(sol.lis)
    print(newboard)


