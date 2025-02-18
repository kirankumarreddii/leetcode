# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        pre=None
        current=head
        nextnode=None
        while current:
            nextnode=current.next
            current.next=pre
            pre=current
            current=nextnode
        return pre


        
        