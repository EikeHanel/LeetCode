class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum = 0
        odd = 0
        even = 0
        res = 0
        for n in arr:
            cur_sum += n
            if cur_sum % 2 != 0:
                if even != 0:
                    res += even
                odd += 1
                res += 1
            else:
                if odd != 0:
                    res += odd
                even += 1
        return res % (10 ** 9 + 7)