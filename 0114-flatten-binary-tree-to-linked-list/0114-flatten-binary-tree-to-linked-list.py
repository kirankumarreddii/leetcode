# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # if not root:
        #     return None
        # nodes=[]
        # stack=[]
        # stack.append(root)
        # while stack:
        #     node=stack.pop()
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        #     nodes.append(node)
        # root=nodes.pop(0) 
        # for node in nodes:
        #     root.right=node
        #     root.left=None
        #     root=root.right
        # return root

        if not root or (not root.left and not root.right):
            return root
        
        newLeft = self.flatten(root.left)
        newRight = self.flatten(root.right)

        curr = newLeft
        if not curr:
            return root
        
        while curr.right:
            curr = curr.right
        
        curr.right = newRight
        root.left = None
        root.right = newLeft

        return root