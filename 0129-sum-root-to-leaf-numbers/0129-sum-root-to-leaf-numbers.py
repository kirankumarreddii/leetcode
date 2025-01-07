# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        Total_Sum=0
        def track(node,Sum):
            nonlocal Total_Sum
            if not node:
                return
            Sum=10*Sum+node.val
            if not node.left and not node.right:
                Total_Sum+=Sum
                return 
            # Sum+=node.val
            track(node.left,Sum)
            track(node.right,Sum)

                
        track(root,0)
        return Total_Sum