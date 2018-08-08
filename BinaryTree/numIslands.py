class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        """
        broad first search
        """
        if len(grid) == 0:
            return 0
        m,n = len(grid), len(grid[0])
        flag = [[0]*n for i in range(m)]
        num = 0
        lists = []
        for ii in range(m):
            for jj in range(n):
                if grid[ii][jj]==0:
                    continue
                if flag[ii][jj]==0:
                    num += 1
                    flag[ii][jj] = num
                    lists.append((ii,jj))
                    while len(lists) > 0:
                        p = lists.pop(0)
                        i, j = p[0], p[1]
                        if j < n-1 and grid[i][j+1] == 1 and flag[i][j+1]==0:
                            flag[i][j+1] = num
                            lists.append((i, j+1))
                        if i < m-1 and grid[i+1][j] == 1 and flag[i+1][j]==0:
                            flag[i+1][j] = num
                            lists.append((i+1, j))
                        if i > 0 and grid[i-1][j] == 1 and flag[i-1][j]==0:
                            flag[i-1][j] = num
                            lists.append((i-1, j))
                        if j > 0 and grid[i][j-1] == 1 and flag[i][j-1]==0:
                            flag[i][j-1] = num
                            lists.append((i, j-1))
        for i in range(len(flag)):
            string = ""
            for j in flag[i]:
                string = string + str(j) + ",    "
            print(string)
        print()
        for i in range(len(grid)):
            string = ""
            for j in grid[i]:
                string = string + str(j) + ",    "
            print(string)
        return num

if __name__ == "__main__":
    grid = [[1,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0],[0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0],[0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1],[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0],[0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1],[0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0],[1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0],[0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0],[1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1],[0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0],[0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0],[1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1],[1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0],[0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0],[0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1],[0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0]]
    sol = Solution()
    num = sol.numIslands(grid)
    print(num)