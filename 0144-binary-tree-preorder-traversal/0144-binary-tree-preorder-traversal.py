# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodee=[]
        if not root:
                return nodee
        def helper(root, nodee ):
            if root is None:
                return nodee
            nodee.append(root.val)
            helper(root.left, nodee)
            helper(root.right, nodee)
        helper(root, nodee )
        return nodee