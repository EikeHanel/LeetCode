class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        check = []
        if s1 == s2:
            return True
        for i, c in enumerate(s1):
            if c == s2[i]:
                continue
            else:
                check.append((c, s2[i]))
        if len(check) == 2 and check[0][0] == check[1][1] and check[0][1] == check[1][0]:
            return True
        else:
            return False