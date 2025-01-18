class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count("1")
        res = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zero += 1
            elif s[i] == "1":
                one -= 1
            if (zero + one) > res:
                res = zero + one
    
        return res

