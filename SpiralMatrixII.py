class Solution:
    def generateMatrix(self, n):
        matrix, i = [[n*n]], n*n - 1
        while i > 0:
            matrix = list(zip(*matrix[::-1]))
            matrix.insert(0, list(range(i - len(matrix[0]) + 1, i+1)))
            i -= len(matrix[0])
        return matrix

s = Solution()
print(s.generateMatrix(2))
