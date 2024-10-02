class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans = []
        order = {}
        tmp = arr.copy()
        tmp.sort()
        i = 0
        
        for n in range(len(tmp)):
            if tmp[n] == tmp[n-1] and n != 0:
                order[tmp[n]] = i
            else:
                i += 1
                order[tmp[n]] = i
        for k in arr:
            rank = order[k]
            ans.append(rank)

        return ans