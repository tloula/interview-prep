from collections import Counter

class Solution:
    def permuteUnique_dfs(self, nums):
        res = set()
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, build, res):
        if not nums: return res.add(tuple(build))
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], build+[nums[i]], res)
            
    def permuteUnique(self, nums):        
        def backtrack(comb, counter):
            if len(comb) == len(nums): return res.append(list(comb))
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1

        res = []
        backtrack([], Counter(nums))
        return res

s = Solution()
print(s.permuteUnique([1, 1, 2]))