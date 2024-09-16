class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Check for zero length string
        if n == 0:
            return ""
        # two for loops to go through all substrings starting from the longest possible
        for length in range(n, 1, -1):
            for k in range(n - length + 1):
                # setting the substring for the current loop
                substring = s[k:k + length]
                # checks if substring is a palindrom
                if substring == substring[::-1]:
                    return substring
        return s[0]
        