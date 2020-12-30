class Solution:
    def subsets2(self, nums):    
        def dfs(build, nums):
            ret.append(build)
            for i, num in enumerate(nums):
                dfs(build + [num], nums[i+1:])

        ret = []
        dfs([], nums)
        return ret

    def subsets(self, nums):
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets]
        return subsets


s = Solution()
print(s.subsets([1,2,3]))
