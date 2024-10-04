# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            lefty=dfs(root.left)
            righty=dfs(root.right)
            res+=abs(lefty-righty)
            return lefty+righty+root.val
        dfs(root)
        return res