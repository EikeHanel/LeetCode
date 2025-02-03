class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        loop_max = 1
        count_up = 1
        count_down = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count_up += 1
                count_down = 1
            elif nums[i-1] > nums[i]:
                count_down += 1
                count_up = 1
            else:
                count_up = 1
                count_down = 1            
            loop_max = max(count_up, count_down)

        return loop_max
