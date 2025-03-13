class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        res = 0 
        if sum(nums) == 0:
            return res
        for q in queries:
            res += 1
            l, r, val = q
            for i in range(l, r + 1):
                if nums[i] != 0 and nums[i] >= val:
                    nums[i] -= val
                elif nums[i] != 0 and nums[i] < val:
                    nums[i] = 0

            target = sum(nums)
            if target == 0:
                break
        else:
            return -1

        return res
            
            
                