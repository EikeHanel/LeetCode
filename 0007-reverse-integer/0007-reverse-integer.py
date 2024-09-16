class Solution:
    def reverse(self, x: int) -> int:
        # 32-bit integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        ans = 0
        if x < 0:
            x = x*(-1)
            ans = int(str(x)[::-1]) *(-1)
        else:  
            ans = int(str(x)[::-1])

        if ans < INT_MIN or ans > INT_MAX:
            return 0

        return ans