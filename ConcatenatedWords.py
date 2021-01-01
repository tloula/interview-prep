class Solution():
    def findAllConcatenatedWords(self, words):
        wordsDict = set(words)
        cache = {}
        return [word for word in words if self._canForm(word, wordsDict, cache)]

    def _canForm(self, word, wordDict, cache):
        if word in cache:
            return cache[word]
        for index in range(1, len(word)):
            prefix = word[:index]
            suffix = word[index:]
            if prefix in wordDict:
                if suffix in wordDict or self._canForm(suffix, wordDict, cache):
                    return True
        return False

print(Solution().findAllConcatenatedWords(['cat', 'cats', 'dog', 'catsdog']))