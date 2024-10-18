class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.max_or = 0
        for n in nums:
            self.max_or |= n
        
        self.res = 0
        def dfs(i, cur_or):
            if i == len(nums):
                self.res += 1 if cur_or == self.max_or else 0
                return
            
            dfs(i + 1, cur_or)

            dfs(i + 1, cur_or | nums[i])
        
        dfs(0, 0)
        return self.res