# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        queue=deque([root])
        count=0
        while queue:
            length=len(queue)
            l=[]
            for _ in range(length):
                node=queue.popleft()
                l.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if count%2==1:
                res.append(list(reversed(l)))
            else:
                res.append(l)      
            count+=1
        return res