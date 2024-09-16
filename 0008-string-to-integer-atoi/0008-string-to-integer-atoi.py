class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        i = 0 
        n = len(s)
        sign = 1 
        ans = 0

        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Handle the sign if it exists
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. Convert the digits
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Check for overflow and return INT_MIN or INT_MAX if necessary
            if ans > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            ans = ans * 10 + digit
            i += 1

        # 5. Apply the sign to the result
        ans *= sign

        return ans