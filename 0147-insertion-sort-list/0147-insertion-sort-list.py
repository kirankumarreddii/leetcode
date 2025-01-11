# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        cur=head
        while cur.next and cur:
            if cur.val<=cur.next.val:
                cur=cur.next
                continue
            insert=cur.next
            cur.next=cur.next.next
            prev=dummy
            while prev.next and prev.next.val < insert.val:
                prev=prev.next
            insert.next=prev.next
            prev.next=insert
        return dummy.next