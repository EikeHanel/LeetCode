from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Combine words into a list
        s = s1.split() + s2.split() 
        
        # Use Counter to count frequency of words   
        word_count = Counter(s)
        
        # Return words that appear exactly once
        return [word for word in word_count if word_count[word] == 1]