class Solution:
    def combinationSum_backtrack(self, candidates, target):
        def dfs(nums, target, path, res):
            if target < 0: return
            if target == 0: return res.append(path)
            for i in range(len(nums)):
                dfs(nums[i:], target-nums[i], path+[nums[i]], res)
        res = []
        dfs(candidates, target, [], res)
        return res

    def combinationSum(self, candidates, target):
        dp = [[] for _ in range(target+1)]
        for c in candidates:
            for i in range(c, target+1):
                if i == c: dp[i].append([c])
                else:
                    for blist in dp[i-c]:
                        dp[i].append(blist+[c])
        return dp[target]

s = Solution()
print(s.combinationSum([2,3,6,7], 7))
