class Solution:
    def minimumSteps(self, s: str) -> int:
        swaps = 0
        one_count = 0
        
        for char in s:
            if char == "1":
                one_count +=1
            else:
                swaps += one_count
                
        return swaps
                