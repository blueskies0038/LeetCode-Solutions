"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)
        output = 0
        
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()
                for child in currentNode.children:
                    queue.append(child)
            output += 1
        
        return output
