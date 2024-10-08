class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for n in nums:
            if n in num_map:
                num_map[n] += 1
            else:
                num_map[n] = 1

        ans = []
        for i in range(k):
            highest = max(num_map, key=num_map.get)  
            ans.append(highest)
            num_map[highest] = -1

        return ans