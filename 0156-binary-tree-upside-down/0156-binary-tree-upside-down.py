# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        mewroot=self.upsideDownBinaryTree(root.left)
        root.left.left=root.right
        root.left.right=root
        root.left=None
        root.right=None
        return mewroot