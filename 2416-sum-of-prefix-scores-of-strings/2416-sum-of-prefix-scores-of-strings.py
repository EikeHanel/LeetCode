class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_count = {}
        for w in words:
            for i in range(1, len(w) + 1):
                prefix = w[:i]
                if prefix in prefix_count:
                    prefix_count[prefix] += 1
                else:
                    prefix_count[prefix] = 1
        ans = []
        for w in words:
            score = 0
            for i in range(1, len(w) + 1):
                prefix = w[:i]
                score += prefix_count[prefix]
            ans.append(score)
        
        return ans
