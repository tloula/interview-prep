class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]: merged.append(interval)
            else: merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

s = Solution()
print(s.merge([[0,0],[1,4]]))
print(s.merge([[0,1],[1,4]]))
print(s.merge([[1,4],[0,2],[3,5]]))