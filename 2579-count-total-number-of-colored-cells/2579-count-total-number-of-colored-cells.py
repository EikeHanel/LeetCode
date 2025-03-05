class Solution:
    def coloredCells(self, n: int) -> int:
        res = 0
        if n < 2: return 1
        while n > 1:
            res += (n - 1) * 4
            n -= 1
        return res + 1