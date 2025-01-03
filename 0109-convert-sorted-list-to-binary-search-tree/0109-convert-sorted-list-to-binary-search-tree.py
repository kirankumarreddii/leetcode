# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def midNode(start,end):
            fast=start
            slow=start
            while fast!=end and fast.next!=end:
                fast=fast.next.next
                slow=slow.next
            return slow

        def buildTree(start,end):
            if start==end:
                return None
            mid=midNode(start,end)
            root=TreeNode(mid.val)
            root.left=buildTree(start,mid)
            root.right=buildTree(mid.next,end)
            return root
        return buildTree(head,None)
       