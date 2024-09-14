class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        test = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] in test:
                test = test[test.index(s[i])+1:] + s[i]
            else:
                test += s[i]
            if count < len(test):
                count = len(test)
        return count


        # # First Attempt found easier solution while coding

        # if len(s) == 0:
        #     return 0

        # letters = s[0]
        # count = 1
        # lst = []
        # for i in range(1, len(s)):
        #     # # Debuggin help
        #     print(f"i: {i} letters: {letters}")
        #     print(f"i: {i} current letter is {s[i]}")
        #     print(f"i: {i} lst: {lst}") # a list was used to see the variations of the letters varable before it got reset
            
        #     if s[i] in letters:
        #         lst.append(letters)
        #         letters = letters[letters.index(s[i])+1:] + s[i]
                
        #         if i == len(s)-1:
        #             lst.append(letters)
            
        #     elif s[i] not in letters:
        #         letters += s[i]
        
        #     if count < len(letters):
        #         count = len(letters)
        
        # print(f"final lst {lst}")
        # print(count)

        # return count

        