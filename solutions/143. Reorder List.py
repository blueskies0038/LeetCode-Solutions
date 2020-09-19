# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head:
            return
            
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        second_head = self.reverseList(slow.next)
        slow.next = None
        
        current = head
        current2 = second_head
        
        while current2:
            current_next = current.next
            current2_next = current2.next
            current.next = current2
            current2.next = current_next
            current = current_next
            current2 = current2_next
        
    def reverseList(self, head):
        prev = None
        current = head
            
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
