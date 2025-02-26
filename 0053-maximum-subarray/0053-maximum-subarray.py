class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_min, cur, res = 0, 0 ,0

        for n in nums:
            cur += n
            res = max(res, (cur - pre_min))
            pre_min = min(cur, pre_min)

        return res