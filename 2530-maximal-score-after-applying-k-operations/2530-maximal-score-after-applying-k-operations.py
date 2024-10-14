class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_score = 0
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        
        while k !=0:
            n = -heapq.heappop(max_heap)
            max_score += n
            k -= 1
            heapq.heappush(max_heap, -math.ceil(n / 3))
        return max_score



        # # Time Limit Exceeded - Time complexity O(k*nlogn)
        # while k != 0:
        #     nums.sort()
        #     max_score += nums[-1]
        #     nums[-1] = ceil(nums[-1]/3)
        #     k -= 1
        
        # return max_score


