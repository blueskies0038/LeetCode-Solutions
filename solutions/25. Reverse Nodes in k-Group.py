# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l, node = 0, head
        while node:
            l += 1
            node = node.next
        
        if k <= 1 or l < k:
            return head
        
        node, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = node
            node = curr
            curr = nxt
        
        head.next = self.reverseKGroup(curr, k)
        return node
