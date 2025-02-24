class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        # Bob Simulation - DFS
        bob_time = {} # node on root path -> time visited
        def dfs(src, prev, time):
            if src == 0:
                bob_time[src] = time
                return True
            for nei in adj[src]:
                if nei == prev:
                    continue
                if dfs(nei, src, time + 1):
                    bob_time[src] = time
                    return True
            return False
        dfs(bob, -1, 0)

        # Alice Simulation - BFS
        q = deque([(0, 0, -1, amount[0])])  # (node, time, parent, total profit)
        res = float("-inf")
        while q:
            node, time, parent, profit = q.popleft()

            for nei in adj[node]:
                if nei == parent:
                    continue
                nei_profit = amount[nei]
                nei_time = time + 1
                if nei in bob_time:
                    if nei_time > bob_time[nei]:
                        nei_profit = 0
                    if nei_time == bob_time[nei]:
                        nei_profit = nei_profit // 2
                
                q.append((nei, nei_time, node, profit + nei_profit))
                if len(adj[nei]) == 1:
                    res = max(res, profit + nei_profit)

        return res