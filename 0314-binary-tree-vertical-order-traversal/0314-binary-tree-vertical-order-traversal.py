# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        queue=deque([(root,0)])
        order=defaultdict(list)
        while queue:
            n=len(queue)
            for i in range(n):
                node,le=queue.popleft()
                order[le].append(node.val)
                if node.left:
                    queue.append((node.left,le-1))
                if node.right:
                    queue.append((node.right,le+1))
        for i in sorted(order.keys()):
            res.append(order[i])
        return res
        




        