from collections import Counter

class Solution:
    def subsetsWithDup(self, nums):
        def dfs(build, nums):
            ret.append(build)
            for i, num in enumerate(nums):
                if i > 0 and num == nums[i-1]: continue
                dfs(build + [num], nums[i+1:])

        ret = []
        dfs([], sorted(nums))
        return ret

    def subsetsWithDup2(self, nums):
        res = [[]]
        for n, frequency in Counter(nums).items():
            res += [r+[n]*i for r in res for i in range(1, frequency+1)]
        return res

s = Solution()
print(s.subsetsWithDup([1,2,2]))
