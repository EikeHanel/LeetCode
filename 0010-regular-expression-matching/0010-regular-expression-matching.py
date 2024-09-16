class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        test = False 
        for n in range(len(s)-1):
            if len(s) != len(p):
                break
            elif s[n] == p[n] or p[n] == ".":
                test  = True
            elif n > 0 and p[n] == "*":
                if s[n] == p[n-1]:
                    test = True
        return test
                    