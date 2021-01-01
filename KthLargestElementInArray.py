class Solution():
    def findKthLargest(self, nums, k):
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivotIndex = self._partition(nums, left, right)
            if pivotIndex == len(nums) - k:
                return nums[pivotIndex]
            elif pivotIndex > len(nums) - k:
                right = pivotIndex - 1
            else:
                left = pivotIndex + 1
        return -1
    
    def _partition(self, arr, low, high):
        pivot = arr[high//2]
        index = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[index], arr[j] = arr[j], arr[index]
                index += 1
        arr[index], arr[high] = arr[high], arr[index]
        return index

print(Solution().findKthLargest([5,7,2,3,4,1,6], 3))
