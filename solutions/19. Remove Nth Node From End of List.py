# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = ListNode(None)
        node.next = head
        prev = node
        left = head
        right = head
        for i in range(n-1):
            right = right.next
        while right and right.next:
            prev, left = left, left.next
            right = right.next
        prev.next = left.next
        return node.next

        
    