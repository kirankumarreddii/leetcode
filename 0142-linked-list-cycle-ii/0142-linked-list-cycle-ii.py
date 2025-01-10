# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # space o(n)
        # visited=set()
        # while head:
        #     if head in visited:
        #         return head
        #     visited.add(head)
        #     head=head.next
        # return None
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                break
        else:
            return None
        slow=head
        while slow!=fast:
            fast=fast.next
            slow=slow.next
        return slow
            