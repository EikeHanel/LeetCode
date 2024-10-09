class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        closed = 0
        ans = 0
        for c in s:
            if c == "(":
                closed -= 1
            else:
                closed += 1
            if closed > 0:
                ans += 1
                closed = 0
        
        return ans if closed == 0 else abs(closed) + ans