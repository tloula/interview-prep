class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            x, y = mid % n, mid // n
            if matrix[y][x] < target: lo = mid + 1
            elif matrix[y][x] > target: hi = mid - 1
            else: return True
        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(s.searchMatrix([[0,1,2],[3,4,5],[6,7,8]], 9))
