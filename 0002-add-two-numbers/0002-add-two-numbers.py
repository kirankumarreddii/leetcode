# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ls1=""
        ls2=""
        d=n=ListNode(0,None)
        while l1 is not None:
            ls1=ls1+str(l1.val)
            l1=l1.next
        while l2 is not None:
            ls2=ls2+str(l2.val)
            l2=l2.next
        rever=str(int(ls1[::-1])+int(ls2[::-1]))[::-1]
        for i in rever:
            con=int(i)
            newnode=ListNode(con)
            d.next=newnode
            d=d.next
        return n.next
    """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """