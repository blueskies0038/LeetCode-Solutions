"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        
        if root is None:
            return output
        
        stack = [root]
        
        while stack:
            currentNode = stack.pop()
            output.append(currentNode.val)
            stack.extend(currentNode.children[::-1])
        
        return output
