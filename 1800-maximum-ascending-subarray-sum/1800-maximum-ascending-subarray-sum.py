class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0 
        tmp = nums[0]
        increasing = 0

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                tmp += nums[i]
            else:
                tmp = nums[i]
            res = max(res, tmp)

        return res