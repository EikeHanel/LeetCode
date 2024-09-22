class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit_shortner = 0xffffffff
        while (b & bit_shortner) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        return (a & bit_shortner) if b > 0 else a