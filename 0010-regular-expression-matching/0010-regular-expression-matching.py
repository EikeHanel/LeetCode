class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Memoization cache to store results of subproblems
        memo = {}

        def dp(i, j):
            # Check if we've already computed this subproblem
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If we've reached the end of the pattern
            if j == len(p):
                if i == len(s):
                    memo[(i, j)] = True  # Store True for a complete match
                else:
                    memo[(i, j)] = False  # Store False if the string still has characters
                return memo[(i, j)]

            # Check if the current character matches
            current_match = False
            if i < len(s) and (p[j] == s[i] or p[j] == '.'):
                current_match = True

            # If the next character in the pattern is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: Skip the "x*" (i.e., match zero occurrences of the character)
                match_zero = dp(i, j + 2)
                
                # Option 2: Use the '*' to match one or more occurrences of the current character
                match_one_or_more = False
                if current_match:
                    match_one_or_more = dp(i + 1, j)
                
                # If either option works, return True
                if match_zero or match_one_or_more:
                    memo[(i, j)] = True  # Store True for a match
                else:
                    memo[(i, j)] = False  # Store False if neither option works
                return memo[(i, j)]
            
            # If there's no '*', check if the first character matches and move forward
            if current_match:
                memo[(i, j)] = dp(i + 1, j + 1)  # Proceed to the next character in both s and p
            else:
                memo[(i, j)] = False  # If no match at the current position, return False

            return memo[(i, j)]

        # Start the recursion from the beginning of both the string and the pattern
        return dp(0, 0)
