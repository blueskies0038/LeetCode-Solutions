# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        current = head
        output = 0
        
        while current:
            if current.val in G and current.next is None:
                output += 1
            elif current.val in G and current.next.val not in G:
                output += 1
            current = current.next
        return output
    
      
