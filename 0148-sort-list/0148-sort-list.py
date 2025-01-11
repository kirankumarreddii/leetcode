# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid=self.midpoint(head)
        left=head
        right=mid.next
        mid.next=None

        left=self.sortList(head)
        right=self.sortList(right)
        return self.merge(left,right)
    def midpoint(self,cur):
        slow,fast=cur,cur
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def merge(self,left,right):
        dummy=ListNode(0)
        tail=dummy
        while left and right:
            if left.val<right.val:
                tail.next=left
                left=left.next
                tail=tail.next
            else:
                tail.next=right
                right=right.next
                tail=tail.next
        tail.next=right or left

        return dummy.next
                
        



    