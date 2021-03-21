# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        output = 0
        
        if root is None:
            return output
        
        queue = deque()
        queue.append(root)
        
        while queue:
            n = len(queue)
            for _ in range(n):
                output += 1
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        
        return output
