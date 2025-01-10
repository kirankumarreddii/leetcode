# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # visited=set()
        # cur=head
        # while cur:
        #     if cur not in dist:
        #         dist[cur]=cur  
        #     else:
        #         pos=cur
        #     cur=cur.next
        
        visited = set()  # Use a set to store visited nodes
        current = head

        while current:
            if current in visited:  # If the node is already in the set, a cycle is detected
                return current  # Return the node where the cycle begins
            visited.add(current)  # Mark the node as visited
            current = current.next

        return None  # If no cycle exists, return None