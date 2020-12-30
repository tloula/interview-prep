# 300/300
def mutateTheArray(n, a):
    b = list(a)
    for i in range(len(a)):
        if i > 0: b[i] += a[i-1]
        if i < len(a)-1: b[i] += a[i+1]
    return b

# 300/300
import collections
def alternatingSort(a):
    b = [0 for _ in range(len(a))]
    for i in range(len(a)):
        if i % 2 == 0:  b[i] = a[i//2]
        else:           b[i] = a[len(a)-1-i//2]
    return b == sorted(b) and all(v == 1 for v in collections.Counter(b).values())

# 300/300
def mergeStrings(s1, s2):
    m1, m2, out = list(s1), list(s2), list()
    while m1 or m2:
        if   m1 == []: out.append(m2.pop(0))
        elif m2 == []: out.append(m1.pop(0))
        elif s1.count(m1[0]) >  s2.count(m2[0]):  out.append(m2.pop(0))
        elif s1.count(m1[0]) == s2.count(m2[0]):  out.append(m1.pop(0) if m1[0] <= m2[0] else m2.pop(0))
        elif s1.count(m1[0]) <  s2.count(m2[0]):  out.append(m1.pop(0))
    return "".join(out)

# 300/300
def concatenationsSum(a):
    return sum(a) * (sum(10**len(str(n)) for n in a) + len(a))

# 300/300
def meanGroups(a):
    dic = dict()
    for i in range(len(a)):
        mean = sum(a[i]) / len(a[i])
        dic.setdefault(mean, []).append(i)
    return list(dic.values())

# 300/300
import math
def digitAnagrams(a):
    c = 0
    d = dict()
    for x in a:
        t = str("".join(sorted([x for x in str(x)])))
        if t in d.keys(): d[t] += 1
        else: d[t] = 1
    return sum(math.factorial(v)/(math.factorial(2)*math.factorial(v-2)) if v > 1 else 0 for v in d.values())

# 300/300
def countTinyPairs(a, b, k):
    pairs = 0
    for i in range(len(a)):
        if int(str(a[i]) + str(b[len(b) - 1 - i])) < k: pairs += 1
    return pairs

# 300/300
def hashMap(queryType, query):
    hm, ret = dict(), 0
    key_offset, value_offset = 0, 0
    for i in range(len(query)):
        qt, q = queryType[i], query[i]
        if qt == "insert": hm[q[0] - key_offset] = q[1] - value_offset
        elif qt == "get": ret += hm[q[0] - key_offset] + value_offset
        elif qt == "addToKey": key_offset += q[0]
        elif qt == "addToValue": value_offset += q[0]
        else: print("Invalid Query Type")
    return ret
