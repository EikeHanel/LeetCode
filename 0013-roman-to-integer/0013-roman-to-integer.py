class Solution:
    def romanToInt(self, s: str) -> int:
        roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            }
        ans = 0
        length = len(s)
        
        for i in range(length):
            current_value = roman[s[i]]
            next_value = roman[s[i + 1]] if i + 1 < length else 0
            
            # Determine if we need to add or subtract
            if current_value < next_value:
                ans -= current_value
            else:
                ans += current_value
        
        return ans