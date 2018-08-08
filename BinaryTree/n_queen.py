class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    '回溯法？'
    def solveNQueens(self, n):
        solutions = []
        k = 0
        path = []
        stack = self.checknext(n, k, path)
        while len(stack) > 0:
            node = stack.pop()
            k = node[0]
            path = path[0:k]
            path.append(node)
            stack += self.checknext(n, k+1, path)
            if k == n-1:
                solutions.append(path)
        graph_solutions = [[['.']*n for i in range(n)] for j in range(len(solutions))]
        string_solutions = []
        for k,s in enumerate(solutions):
            for l in s:
                graph_solutions[k][l[0]][l[1]] = 'Q'
            mat = []
            for line in graph_solutions[k]:
                mat.append(''.join(line))
            string_solutions.append(mat)

        return solutions, string_solutions
    
    def checknext(self, n, k, path):
        # the kth row and l col, n*n matrix
        print("k = ", k, "path=", path)
        noconflict = []
        for l in range(n):
            flag = 0
            for p in path:
                i = p[0]
                j = p[1]
                #this step can be optimised
                if abs(abs(k-i)-abs(l-j)) == 0 or l == j: 
                    flag = 1
                    break
            if flag == 0:
                noconflict.append((k,l))
        print(noconflict)
        return noconflict

if __name__ == "__main__":
    sl = Solution()
    mat = sl.solveNQueens(10)
    print(mat)
    print(len(mat[1]))
