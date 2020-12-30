class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = [[j, i] for i, row in enumerate(matrix) for j, x in enumerate(row) if x == 0]
        for x, y in zeroes:
            for i in range(len(matrix[y])): matrix[y][i] = 0
            for i in range(len(matrix)): matrix[i][x] = 0
        return matrix

s = Solution()
print(s.setZeroes([[1,1,1,1],[1,1,0,1],[1,1,1,1]]))
