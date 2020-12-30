class Solution:
    def combinationSum2(self, candidates, target):
        dp = [set() for _ in range(target+1)]
        dp[0].add(())
        candidates.sort()
        for c in candidates:
            for i in range(target, c-1, -1):
                for prev in dp[i-c]:
                    dp[i].add(prev + (c,))
        return list(dp[target])

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
