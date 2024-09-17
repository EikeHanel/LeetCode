class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""  
        thousand = num // 1000
        hundred = (num % 1000) // 100
        ten = (num % 100) // 10
        one = num % 10
        num = [thousand, hundred, ten, one] 
        for k in range(len(num)):
            # Thousand:
            if k == 0 and num[k] != 0:
                ans += "M" * num[k]
            # Hundred:
            elif k == 1:
                if num[k] == 9:
                    ans += "CM"
                elif 9 > num[k] > 5:
                    ans += "D" + ("C" * (num[k]-5))
                elif num[k] == 5:
                    ans += "D"
                elif num[k] == 4:
                    ans += "CD"
                else: 
                    ans += "C" * num[k]
            # Ten:
            elif k == 2:
                if num[k] == 9:
                    ans += "XC"
                elif 9 > num[k] > 5:
                    ans += "L" + "X" * (num[k]-5)
                elif num[k] == 5:
                    ans += "L"
                elif num[k] == 4:
                    ans += "XL"
                else: 
                    ans += "X" * num[k]
            # One:
            elif k == 3:
                if num[k] == 9:
                    ans += "IX"
                elif 9 > num[k] > 5:
                    ans += "V" + "I" * (num[k]-5)
                elif num[k] == 5:
                    ans += "V"
                elif num[k] == 4:
                    ans += "IV"
                else: 
                    ans += "I" * num[k]
        return ans
