class Solution:
    def longestPalindrome(self, s: str) -> str:
        return max([max(self._palindromeAt(s, i, i), self._palindromeAt(s, i, i+1), key=len) for i in range(len(s))], key=len)

    def _palindromeAt(self, s, l, r):    
        while l >= 0 and r < len(s) and s[l] == s[r]: l -= 1; r += 1
        return s[l+1:r]

print(Solution().longestPalindrome("babad"))
