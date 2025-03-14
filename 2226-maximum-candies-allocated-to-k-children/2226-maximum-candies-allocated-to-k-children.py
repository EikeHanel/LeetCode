class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sum_candies = sum(candies)
        print(sum_candies)
        if sum_candies < k:
            return 0
        
        l, r = 1, (sum_candies // k)
        print(r)
        res = 0
        while l <= r:
            m = (l + r) // 2
            count = 0
            for c in candies:
                print(c)
                if c >= m:
                    count += c // m
                print(count)
            if count >= k:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res 
        