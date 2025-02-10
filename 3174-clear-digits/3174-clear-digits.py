class Solution:
    def clearDigits(self, s: str) -> str:
        res = ""
        for c in s:
            if c.isdigit() and res:
                res = res[:-1]
            else:
                res += c
            

        return res

            

