class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #return nums.index(target) if target in nums else -1
        if not nums: return -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target: return mid
            elif nums[mid] < nums[hi]:
                if target >= nums[mid] and target <= nums[hi]: lo = mid+1
                else: hi = mid-1
            else:
                if target >= nums[lo] and target <= nums[mid]: hi = mid-1
                else: lo = mid+1
        return -1

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
