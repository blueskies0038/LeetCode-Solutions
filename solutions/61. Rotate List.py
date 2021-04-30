# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        pointer = head
        count = 1
        
        while pointer.next:
            count += 1
            pointer = pointer.next
        
        n = k % count
        if n == 0:
            return head
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next, fast.next, head = None, head, slow.next
        
        return head
