# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        def build_bst(preorder,inorder,left,right):
            if left>right:
                return None
            node=preorder.pop(0)
            indx=inorder.index(node)
            root=TreeNode(node)
            root.left=build_bst(preorder,inorder,left,indx-1)
            root.right=build_bst(preorder,inorder,indx+1,right)
            return root
        return build_bst(preorder,inorder,0,len(inorder)-1)
            