class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hashset = set()
        res = 0
        idx = 0
        while idx < len(nums):
            for i in range(idx, len(nums)):
                if nums[i] in hashset:
                    hashset.clear()
                    break
                else:
                    hashset.add(nums[i])
            else:
                return res
            idx += 3
            res += 1
        return  int(len(nums) / 3) + (len(nums) % 3 > 0)
