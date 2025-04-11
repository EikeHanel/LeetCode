class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for n in range(low, high + 1):
            num = str(n)
            num_len = len(num)
            if num_len % 2 != 0:
                continue
            mid = num_len // 2
            total = 0
            for i in range(mid):
                total += int(num[i]) - int(num[i + mid])
            if total == 0:
                res += 1
        return res