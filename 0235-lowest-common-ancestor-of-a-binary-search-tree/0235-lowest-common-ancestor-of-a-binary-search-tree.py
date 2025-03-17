# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root==None or root==p or root==q:
        #     return root
        # left=self.lowestCommonAncestor(root.left,p,q)
        # right=self.lowestCommonAncestor(root.right,p,q)
        # if right and left:
        #     return root
        # if not left:
        #     return right
        # else:
        #     return left
        while root:
            if root.val>p.val and root.val>q.val:
                root=root.left
            elif root.val<p.val and root.val<q.val:
                root=root.right
            else:
                return root

