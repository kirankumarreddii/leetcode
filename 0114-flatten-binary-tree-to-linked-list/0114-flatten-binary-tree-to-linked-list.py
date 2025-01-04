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

        if not root:
            return

        # Initialize a stack to store nodes
        stack = [root]
        prev = None

        while stack:
            # Pop the current node from the stack
            curr = stack.pop()

            # Connect the previous node to the current node
            if prev:
                prev.left = None
                prev.right = curr

            # Push the right and left children of the current node onto the stack
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

            # Update the previous node
            prev = curr