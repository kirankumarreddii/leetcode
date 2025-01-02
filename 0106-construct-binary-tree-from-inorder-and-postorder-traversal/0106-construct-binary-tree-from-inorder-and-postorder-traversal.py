# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            node=postorder.pop()
            print(node)
            idx=inorder.index(node)
            root=TreeNode(node)
            
            root.right=self.buildTree(inorder[idx+1:],postorder)
            root.left=self.buildTree(inorder[:idx],postorder)
            return root
    