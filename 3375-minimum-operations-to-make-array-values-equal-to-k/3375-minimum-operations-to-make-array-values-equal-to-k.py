class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        cur = nums[-1]

        if nums[0] < k:
            return -1
        elif nums[0] != k:
            res += 1
        
        for i in range(len(nums) - 1, -1, -1):
            if cur == nums[i]:
                continue
            else:
                cur = nums[i]
                res += 1
        
        return res