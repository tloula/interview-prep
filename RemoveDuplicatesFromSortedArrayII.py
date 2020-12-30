class Solution:
    def removeDuplicates_slow(self, nums):
        i = 2
        while i < len(nums):
            if nums[i-2] == nums[i]: nums.remove(nums[i])
            else: i += 1
        return len(nums)

    def removeDuplicates(self, nums):
        i, j = 2, 2
        while j < len(nums):
            if nums[i-2] != nums[j]:
                nums[i] = nums[j]
                i+= 1
            j += 1
        return i

s = Solution()
s.removeDuplicates([1,1,1,2,2,3])
