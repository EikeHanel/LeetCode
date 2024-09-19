class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        print(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) -1
            while l < r:
                num_sum = nums[i] + nums[l] + nums[r]
                diff = target - num_sum

                if abs(num_sum - target) < abs(ans - target):
                    ans = num_sum
    
                if num_sum < target:
                    l += 1
                elif num_sum > target:
                    r -=1
                else:
                    return num_sum      
        return ans


        