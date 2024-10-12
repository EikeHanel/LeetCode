class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for l, r in intervals:
            start.append(l)
            end.append(r)
        start.sort()
        end.sort()

        s, e = 0, 0
        res = 0
        groups = 0
        while s < len(intervals):
            if start[s] <= end[e]:
                groups += 1
                s += 1
            else: 
                groups -= 1
                e += 1
            res = max(res, groups)
        return res



