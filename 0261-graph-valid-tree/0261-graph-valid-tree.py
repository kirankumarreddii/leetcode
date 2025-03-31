class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        graph=defaultdict(list)
        visited=set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for v in graph[node]:
                dfs(v)
        dfs(0)
        return len(visited)==n