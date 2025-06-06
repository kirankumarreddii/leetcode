# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (True,float('inf'),float('-inf'),0)
            
            
            left_bst, left_Min_val, left_Max_val, left_Size = dfs(node.left)
            right_bst, right_Min_val, right_Max_val, right_Size = dfs(node.right)
            if left_bst and right_bst and left_Max_val<node.val<right_Min_val:
                Size=left_Size+right_Size+1
                Max_val = max(node.val, right_Max_val)
                Min_val = min(node.val, left_Min_val)
                return (True, Min_val, Max_val, Size)

            else:
                
                return (False, 0, 0, max(left_Size, right_Size))
        return dfs(root)[3]