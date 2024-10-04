class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        s = 0
        while s < len(word1) or s < len(word2):
            if s < len(word1):
                ans += word1[s]
            if s < len(word2):
                ans += word2[s]
            s += 1
        return ans
