# Definition for singly-linked list. 
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head:
            h = head.next
            if h:
                h.next, head.next = head, h.next
                h.next.next = self.swapPairs(h.next.next)  
                return h
        return head    