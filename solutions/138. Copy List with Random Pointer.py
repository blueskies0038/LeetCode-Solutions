"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
​
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        table = {}
        curr = head
        
        while curr:
            table[curr] = Node(curr.val, None, None)
            curr = curr.next
            
        curr = head
        while curr:
            if curr.next:
                table[curr].next = table[curr.next]
            if curr.random:
                table[curr].random = table[curr.random]
            curr = curr.next
        
        return table[head]
