class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        l_map ={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                ans.append(curStr)
                return
            for char in l_map[digits[i]]:
                backtrack(i + 1, curStr + char)

        if digits:
            backtrack(0, "")
        
        return ans

        

    