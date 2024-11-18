# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev=None
        min_diff=float('inf')
        if root is None:
            return None
        def travs(node):
            nonlocal prev, min_diff
            if node is None:
                return 
            travs(node.left)
            
            if prev is not None:
                min_diff=min(min_diff,node.val-prev)
            prev=node.val
            travs(node.right)
        travs(root)
        return min_diff