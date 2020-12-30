import itertools

class Solution:
    def combine2(self, n, k):
        return list(itertools.combinations(range(1, n+1), k))

    def combine(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack: return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1

s = Solution()
print(s.combine(4, 2))
