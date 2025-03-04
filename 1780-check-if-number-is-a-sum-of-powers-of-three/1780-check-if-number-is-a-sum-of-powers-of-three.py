class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers = [3 ** i for i in range(17)]
        
        for val in reversed(powers):
            if val <= n:
                n -= val
            if n == 0:
                return True
        return False