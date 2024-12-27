# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less=ListNode(0)
        grether=ListNode(0)
        dummy1,dummy2=less,grether
        
        while head:
            if head.val<x:
                less.next=head
                less=less.next
            else:
                grether.next=head
                grether=grether.next
            head=head.next
        grether.next = None
        less.next=dummy2.next
        return dummy1.next