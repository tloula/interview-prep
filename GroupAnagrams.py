def groupAnagrams(strs):
    d = dict()
    for word in strs:
        alpha = "".join(sorted(word))
        d.setdefault(alpha, []).append(word)
    return list(d.values())

inp = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(inp))