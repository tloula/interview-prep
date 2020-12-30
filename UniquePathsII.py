class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, m): dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
        for i in range(1, n): dp[0][i] = dp[0][i-1] if obstacleGrid[0][i] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0

        return dp[m-1][n-1]

s = Solution()
print(s.uniquePathsWithObstacles([[1,0]]))
