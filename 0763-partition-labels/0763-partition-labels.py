class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        res = []
        cur = set()
        cur_res = 0 
        print(counter)
        for c in s:
            cur.add(c)
            counter[c] -= 1
            cur_res += 1
            print(cur)
            if counter[c] == 0:
                print(c, counter)
                cur.remove(c)
                
            if not cur:
                res.append(cur_res)
                cur_res = 0
        return res
