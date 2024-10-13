class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for c in range(len(position)):
            stack.append((position[c], (target-position[c])/speed[c]))
        stack.sort(reverse=True)

        ans = len(stack)
        for c in range(len(stack)):
            if c+1 < len(stack) and stack[c][1] >= stack[c+1][1]:
                stack[c+1] = (stack[c+1][0], stack[c][1])
                ans -= 1

        return ans
