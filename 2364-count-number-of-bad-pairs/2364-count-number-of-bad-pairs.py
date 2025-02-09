class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # # Brute Force
        # res = 0 
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         idx_val = j - i
        #         val = nums[j] - nums[i]
        #         if idx_val != val:
        #             res += 1
        
        # return res

        # y = 1 x + b 
        # b = y - x
        # y: value
        # x: index
        b_map = defaultdict(list)
        good_pairs = 0
        total_pairs = 0
        for i, n in enumerate(nums):
            total_pairs += i
            b_map[n-i].append(i)

        for val in b_map.values():
            if len(val) != 1:
                n = len(val) - 1
                good_pairs += int((n * (n + 1)) / 2)

        return total_pairs - good_pairs