class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            curr = nums[i] % 2
            prev = nums[i-1] % 2
            if curr == prev:
                return False
        return True
            