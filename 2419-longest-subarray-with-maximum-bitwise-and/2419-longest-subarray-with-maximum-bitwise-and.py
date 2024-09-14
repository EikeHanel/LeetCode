class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Answer before hints
        count = 0
        h_count = 1
        h_num = 0
        ans = 0
        for num in nums:
            if ans < num:
                ans = num
                count = 1
                h_count = 1
            elif ans == num:
                count += 1
                h_count = max(h_count, count) 
            else:
                count = 0
        return h_count

        