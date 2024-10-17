class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(n) for n in str(num)]
        ans = ""
        l = 0
        max_num = 0
        idx = 0
        while l < len(nums):
            for r in range(l, len(nums)):
                if nums[l] < nums[r]:
                    if max_num <= nums[r]:
                        idx = r
                    max_num = max(max_num, nums[r])
            if max_num > 0:
                nums[idx] = nums[l]
                nums[l] = max_num
                for n in nums:
                    ans += str(n)
                return int(ans)
            l += 1
        return num      