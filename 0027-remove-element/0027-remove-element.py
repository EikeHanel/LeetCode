class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = []
        count= 0
        
        for n in reversed(range(len(nums))):
            if nums[n] == val:
                nums.pop(n)

        return len(nums)