class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] <= nums[r]:
                return (r - l)
        
            if nums[l] > nums[l+1] and l+1 != r:
                l += 1
            else:
                r -=1
        return 0