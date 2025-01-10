# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         slow,fast=head,head
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#         cur=slow
#         prev=None
#         while cur:
#             temp=cur.next
#             cur.next=prev
#             prev=cur
#             cur=temp
#         first,second=head,prev
#         while second.next:
#             temp1=first.next
#             temp2=second.next
#             first.next=second
#             second.next=temp1
#             first=temp1  # first=second.next
#             second=temp2
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        # Step 1: Find the middle of the list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse the second half of the list
        second = slow.next
        slow.next = None
        node = None

        while second:
            temp = second.next
            second.next = node
            node = second
            second = temp

        # Step 3: Merge the two halves
        first = head
        second = node

        while second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2