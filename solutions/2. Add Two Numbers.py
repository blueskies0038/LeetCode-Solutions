# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, carry = 0) -> ListNode:
        value = l1.val + l2.val + carry
        carry = (value)//10
        total = ListNode(value % 10)
        if l1.next or l2.next or carry:
            v1 = l1.next if l1.next else ListNode(0)
            v2 = l2.next if l2.next else ListNode(0)
            total.next = self.addTwoNumbers(v1, v2, carry)
        return total