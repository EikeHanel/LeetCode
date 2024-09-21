class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = []
        count= 0
        
        for n in reversed(range(len(nums))):
            if nums[n] == val:
                idx.append(n)
        
        for i in idx:
            nums.pop(i)
        
        return len(nums)