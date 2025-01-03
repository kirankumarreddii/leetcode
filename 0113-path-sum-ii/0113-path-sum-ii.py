# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]

        def path(root,Sum,l):
            if not root:
                return
            Sum+=root.val
            l.append(root.val)
            if Sum==targetSum and root.right==None and root.left==None:
                    res.append(l[:])
            path(root.left,Sum,l)
            
            path(root.right,Sum,l)
            l.pop()
        path(root,0,[])
        return res