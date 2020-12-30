class Solution:
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        l = r = self.binarySearch(nums, target)
        while r < len(nums) - 1 and nums[r+1] == target: r += 1
        return [l, r] if r != -1 else [-1, -1]

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if   nums[mid] < target: left = mid + 1
            elif nums[mid] >= target: right = mid
        return left if nums[left] == target else -1

s = Solution()
print(s.binarySearch([5,6,7,7,8,8,8,8,10], 8))