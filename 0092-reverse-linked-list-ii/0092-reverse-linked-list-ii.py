# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        for _ in range(left-1):
            cur=cur.next
        prev_left=cur
        start=cur.next


        prev=None
        cur=start
        for _ in range(right-left+1):
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        prev_left.next=prev
        start.next=cur
        return dummy.next







