class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        idx, j = 0, 0
        res = [0] * len(nums)
        while j < len(nums)-1:
            print(nums[j])
            if nums[j] == nums[j+1] and nums[j] != 0:
                res[idx] = nums[j] * 2
                nums[j+1] = 0
                j += 1
                idx += 1
            elif nums[j] != nums[j+1] and nums[j] != 0:
                res[idx] = nums[j]
                j += 1
                idx += 1
            else:
                j += 1
        if nums[-1] != 0:
            res[idx] = nums[-1]
        return res
