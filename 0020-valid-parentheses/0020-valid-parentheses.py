class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        # Mapping of closing to opening brackets
        bracket_map = {
            ')': '(', 
            '}': '{', 
            ']': '['
            }

        for char in s:
            if char in bracket_map:
                if lst and lst[-1] == bracket_map[char]:
                    lst.pop()
                else:
                    return False
            else:
                lst.append(char)
        return True if not lst else False