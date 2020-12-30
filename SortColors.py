class Solution:
    def sortColors_trev_original(self, nums):
        lo, i, hi = 0, -1, len(nums) - 1
        while i <= hi:
            _lo, _hi = lo, hi
            while nums[lo] == 0 and lo < hi: lo += 1; i = lo
            while nums[hi] == 2 and lo < hi: hi -= 1; i = lo
            if _lo == lo and _hi == hi: i += 1
            i = max(i, lo)
            if i > hi: break

            if   nums[lo] > nums[i]: nums[lo], nums[i] = nums[i], nums[lo]
            elif nums[i] != nums[hi]: nums[i], nums[hi] = nums[hi], nums[i]

        return nums

    def sortColors(self, nums):
        beg, mid, end = 0, 0, len(nums) - 1
        while mid <= end:
            if nums[mid] == 0:
                nums[beg], nums[mid] = nums[mid], nums[beg]
                mid += 1
                beg += 1
            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
            else:  #nums[mid] == 1:
                mid += 1
        return nums

s = Solution()
print(s.sortColors([2,0,2,1,1,0]))
print(s.sortColors([2,0,2,1,1,2,1,0,0,2,0,2,1,2,1,0,0,0]))
print(s.sortColors([0]))
print(s.sortColors([0,1,1]))
print(s.sortColors([2,1,0]))
print(s.sortColors([0,1,2]))
print(s.sortColors([1,1,0]))
print(s.sortColors([1,2,2,2,2,0,0,0,1,1]))
