# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count=0

        def track(node):
            if not node:
                return True
            left_sub=track(node.left)
            right_sub=track(node.right)
            if not left_sub or not right_sub:
                return False
            if node.left and node.val!=node.left.val:
                return False
            if node.right and node.val!=node.right.val:
                return False
            self.count+=1
            return True
            
            

        track(root)
        return self.count