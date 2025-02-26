class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur_sum = 0
        pre_min = 0
        pre_max = 0
        res = 0
        for n in nums:
            cur_sum += n
            res = max(res, abs(cur_sum - pre_max), abs(cur_sum - pre_min))
            pre_min = min(cur_sum, pre_min)
            pre_max = max(cur_sum, pre_max)
        return res