# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        cur=slow
        prev=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        first,second=head,prev
        while second.next:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1  # first=second.next
            second=temp2
