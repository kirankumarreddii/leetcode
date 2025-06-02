class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited=set()
        components=0

        def dfs(node):
            for nieg in graph[node]:
                if nieg not in visited:
                    visited.add(nieg)
                    dfs(nieg)
                
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                components+=1
        return components
        
            