class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        par = []

        def backtrack(open_N, close_N):
            if open_N == close_N == n:
                ans.append("".join(par))
                return
            
            if open_N < n:
                par.append("(")
                backtrack(open_N + 1, close_N)
                par.pop()

            if close_N < open_N:
                par.append(")")
                backtrack(open_N, close_N + 1)
                par.pop()
        
        backtrack(0, 0)
        return ans
            
            


        