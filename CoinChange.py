import sys

class Solution:
    def coinChange(self, coins, amount):
        dp = [sys.maxsize for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i == c: dp[i] = 1
                elif i - c >= 0: dp[i] = min(dp[i], dp[i-c] + 1)
        return dp[amount]

s = Solution()
print(s.coinChange([1,2,5], 11))
