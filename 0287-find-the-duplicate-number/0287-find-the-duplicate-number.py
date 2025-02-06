class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 1
        N = len(nums)
        while True:
            if nums[s] == nums[f]:
                return nums[s]
            s = (s + 1) % N
            f = (f + 2) % N
    
        