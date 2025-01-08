"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        # visited={}

        # def dfs(node):
        #     if node in visited:
        #         return visited[node]
        #     clone=Node(node.val)
        #     visited[node]=clone
        #     for n in node.neighbors:
        #             clone.neighbors.append(dfs(n))
        #     return clone
        # return dfs(node)
        Clone={}
        queue=deque([node])
        Clone[node]=Node(node.val)

        while queue:
            current=queue.popleft()
            for adj in current.neighbors:
                if adj not in Clone:
                    Clone[adj]=Node(adj.val)
                    queue.append(adj)
                Clone[current].neighbors.append(Clone[adj])
        return Clone[node]