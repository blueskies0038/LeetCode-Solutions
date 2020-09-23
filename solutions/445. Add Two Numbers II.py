# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        curr = None
        total = 0
        while num1 or num2 or total:
            if num1:
                total += num1.pop()
            if num2:
                total += num2.pop()
            node = ListNode(total%10)
            node.next = curr
            curr = node
            total //= 10
        return curr
    
        
