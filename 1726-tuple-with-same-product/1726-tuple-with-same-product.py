class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pro_map = defaultdict(int)
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                product = nums[a] * nums[b]
                pro_map[product] += 1
        
        res = 0
        pairs = 0
        for n in pro_map.values():
            pairs = (n * (n - 1)) // 2
            res += 8 * pairs
        return res