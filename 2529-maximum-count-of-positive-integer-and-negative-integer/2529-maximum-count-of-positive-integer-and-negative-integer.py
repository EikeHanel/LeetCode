class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        N = len(nums) 
        l, r = 0, N - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < 0:
                l = mid + 1
            else: 
                r = mid - 1
        n_nums = l 
        
        l, r = 0, N - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > 0:
                r = mid - 1
            else: 
                l = mid + 1
        p_nums = N - l
        return max(n_nums, p_nums)
        
        