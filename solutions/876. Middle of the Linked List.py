# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        nodes = []
        curr = head
        
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        return nodes[len(nodes)//2]
