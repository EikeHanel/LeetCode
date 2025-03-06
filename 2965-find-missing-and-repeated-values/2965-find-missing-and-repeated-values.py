class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid[0]) ** 2
        nums = set()
        res = []
        for row in grid:
            for col in row:
                if col in nums:
                    res.append(col)
                else:
                    nums.add(col)

        for n in range(1, N+1):
            if n not in nums:
                res.append(n)
                break
                
        return res
        