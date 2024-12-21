# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next or k == 0:
            return head
        dummy=head
        count=1
        while dummy.next:
            dummy=dummy.next
            count+=1
        k=k%count
        if k == 0:
            return head
        dummy.next=head
        length=count-k
        while 0<length:
            dummy=dummy.next
            length-=1
        head=dummy.next
        dummy.next=None
        return head