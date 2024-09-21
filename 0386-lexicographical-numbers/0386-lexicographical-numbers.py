class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # Start DFS from each number 1 to 9
        self.ans = []
        for i in range(1, 10):
            self.dfs(i, n)
        return self.ans

    def dfs(self, current, n):
        if current > n:
            return
        # Process the current number (e.g., print or store it)
        self.ans.append(current)
        
        # Try to append digits to current number
        for i in range(10):
            next_number = current * 10 + i
            if next_number > n:
                break
            self.dfs(next_number, n)


