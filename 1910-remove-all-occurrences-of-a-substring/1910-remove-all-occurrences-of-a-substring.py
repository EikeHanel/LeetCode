class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        N = len(part)
        while part in s:
            index = s.index(part)
            s = s[:index] + s[index + N:]
        return s