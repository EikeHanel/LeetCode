class Solution:
    def check(self, nums: List[int]) -> bool:
        l = nums[0] 
        for r in range(1, len(nums)):
            if l > nums[r] or nums[r-1] > nums[r]:
                m = nums[r]
                for j in range(r, len(nums)):
                    print(nums[j], l)
                    if nums[j] > l or nums[j] < m:
                        return False
                return True
        return True