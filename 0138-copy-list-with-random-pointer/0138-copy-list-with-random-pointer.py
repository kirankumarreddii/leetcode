"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # cur=head
        # while cur:
        #     clone=Node(cur.val)
        #     clone.next=cur.next
        #     cur.next=clone
        #     cur=cur.next.next
        # cur=head
        # while cur:
        #     if cur.random:
        #         cur.next.random=cur.random.next
        #     cur=cur.next.next
        # clone_head=head.next
        # cur=head
        # while cur:
        #     clone=cur.next
        #     cur.next=clone.next
        #     cur=cur.next
        #     if clone.next:
        #         # clone.next=cur.next or below line same
        #         clone.next=clone.next.next
        # return clone_head
        
        cur=head
        visited={}
        while cur:
            clone=Node(cur.val)
            visited[cur]=clone
            cur=cur.next
        cur=head
        while cur:
            if cur.next:
                visited[cur].next=visited[cur.next]
            if cur.random:
                visited[cur].random=visited[cur.random]
            cur=cur.next
        return visited[head]




        
