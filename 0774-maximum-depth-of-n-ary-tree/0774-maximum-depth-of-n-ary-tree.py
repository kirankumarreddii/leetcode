"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # stack=[]
        # if root:
        #     stack.append((root,1))
        # depth=0
        # while stack:
        #     node,level=stack.pop()
        #     depth=max(level,depth)
        #     for child in node.children:
        #         stack.append((child,level+1))
    
        # return depth
        queue=[]
        if root:
            queue.append((root,1))
        depth=0
        for (node,level) in queue:
            depth=level
            for child in node.children:
                queue.append((child,level+1))
        return depth
