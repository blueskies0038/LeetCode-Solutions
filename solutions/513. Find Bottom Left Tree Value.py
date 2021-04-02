# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        output = -1
        
        if root is None:
            return output
        
        queue = deque()
        queue.append(root)
        
        while queue:
            currentNode = queue.popleft()
            output = currentNode.val
            if currentNode.right:
                queue.append(currentNode.right)
            if currentNode.left:
                queue.append(currentNode.left)    
        
        return output
