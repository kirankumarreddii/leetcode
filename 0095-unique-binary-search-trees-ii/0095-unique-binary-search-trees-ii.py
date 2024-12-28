# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        def track(start,end):
            if start>end:
                return [None]
            trees = []
            for i in range(start,end+1):
                left_nodes=track(start,i-1)
                right_nodes=track(i+1,end)
                for left in left_nodes:
                    for right in right_nodes:
                        root=TreeNode(i)
                        root.left=left
                        root.right=right
                        trees.append(root)
            return trees
        return track(1,n)
        