class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair [temp, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = (i - stackIdx)
            stack.append([t, i])
        return res
        
        
        # # To slow: O(n^2)
        # t1 = len(temperatures)
        # stack = []
        # def temp(idx):
        #     days = 0
        #     for t in range(idx+1, t1):
        #         days += 1
        #         if temperatures[idx] < temperatures[t]:
        #             stack.append(days)
        #             return 
        #     stack.append(0)
        # for i in range(t1):
        #     temp(i)
        # return stack

