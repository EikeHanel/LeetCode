class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        len_max = 0

        while r < len(s):
            if s[l] == s[r]:
                len_max = max(len_max, r - l + 1)
                r += 1
            elif s[l] != s[r] and k:
                k -= 1
                len_max = max(len_max, r - l + 1)
                r += 1
            elif s[l] != s[r] and not k:
                l += 1
                r = l + 1
        return len_max
        
            