import sys

class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                grid[i][j] += min(
                    grid[i-1][j] if i > 0 else sys.maxsize,
                    grid[i][j-1] if j > 0 else sys.maxsize)
        return grid[m-1][n-1]

    def minPathSum2(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range(1, m): grid[i][0] += grid[i-1][0]
        for i in range(1, n): grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]

s = Solution()
print(s.minPathSum2([[1,99,1,1,1],[1,99,1,99,1],[1,1,1,99,1],[1,99,1,99,1]]))
