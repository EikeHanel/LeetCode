class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for n in reversed(range(len(nums))):
            if nums[n] == val:
                nums.pop(n)

        return len(nums)