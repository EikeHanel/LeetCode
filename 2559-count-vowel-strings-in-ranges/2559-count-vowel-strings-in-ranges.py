class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        vowels = ["a", "e", "i", "o", "u"]
        ans_list = [0]
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                ans_list.append(ans_list[-1] + 1)
            else:
                ans_list.append(ans_list[-1])

        for q in queries:
            res.append(ans_list[q[1] + 1] - ans_list[q[0]])
            
        return res
