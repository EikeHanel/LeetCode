class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        res = []
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for n in graph[i]:
                if not dfs(n):
                    return safe[i]
            safe[i] = True
            return safe[i]
                
        
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res