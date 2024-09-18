class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # New: using a dictionary  
        num_dict = {}
        for i, num in enumerate(nums):
            missing_num = target-num
            if missing_num in num_dict:
                return [num_dict[missing_num], i]
            else:
                num_dict[num] = i

        # Old: brute force
        # ans = []
        # for num in range(len(nums)):
        #     for n in range(len(nums)):
        #         if n != num and num < n:
        #             test_target = nums[n] + nums[num]
        #             if test_target == target:
        #                 ans.append(num)
        #                 ans.append(n)
        # return ans        
            