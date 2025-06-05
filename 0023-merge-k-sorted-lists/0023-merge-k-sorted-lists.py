# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l=[]
        t=ListNode(0)
        head=t
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(l, (node.val, i, node)) 
        while len(l)!=0:
            v,i,n=heapq.heappop(l)
            if n.next:
                heapq.heappush(l,(n.next.val,i,n.next))
            t.next=ListNode(v)
            t=t.next
        return head.next

            

        