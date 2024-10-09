# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        res=[]
        queue=deque([root])
        while queue:
            som=0
            lq=len(queue)
            for _ in range(lq):
                node=queue.popleft()
                som+=node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(som/lq)
        return res
