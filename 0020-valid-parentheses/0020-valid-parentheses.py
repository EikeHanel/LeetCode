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
                # Pop the last element from the list, or use a dummy value if list is empty
                if lst:
                    top_element = lst.pop()
                else:
                    top_element = '#'
                # Check if opening bracket and closing bracket match if not return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push the opening brackets onto the list
                lst.append(char)

            # If the list is empty, all brackets were matched
        return not lst