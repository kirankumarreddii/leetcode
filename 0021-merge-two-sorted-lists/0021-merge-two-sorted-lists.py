# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(0)
        head=temp
        temp1=list1
        temp2=list2
        while temp1!=None and temp2!=None:
            if temp1.val>=temp2.val:
                temp.next=temp2
                temp2=temp2.next
            else:
                temp.next=temp1
                temp1=temp1.next
            temp=temp.next
        if temp1!=None:
            temp.next=temp1
        else:
            temp.next=temp2
        return head.next
        