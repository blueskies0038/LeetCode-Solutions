# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        queue = deque()
        queue.append(root)
        minDepth = 0
        while queue:
            levelSize = len(queue)
            minDepth += 1
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if not currentNode.left and not currentNode.right:
                    return minDepth
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
