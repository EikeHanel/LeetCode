class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for num in range(len(nums)):
            for n in range(len(nums)):
                if n != num and num < n:
                    test_target = nums[n] + nums[num]
                    if test_target == target:
                        ans.append(num)
                        ans.append(n)
        return ans        
            