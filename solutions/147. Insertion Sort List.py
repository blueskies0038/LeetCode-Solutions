# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(0)
        curr = dummy.next = head
        
        while curr and curr.next:
            val = curr.next.val
            if curr.val < val:
                curr = curr.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            new = curr.next
            curr.next = new.next
            new.next = p.next
            p.next = new
            
        return dummy.next
