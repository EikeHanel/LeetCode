class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        check_letter = []
        

        for word in words:
            check_letter.append([(letter in allowed)*1 for letter in word])
        
        ans = sum(all(x) for x in check_letter)
        return ans
