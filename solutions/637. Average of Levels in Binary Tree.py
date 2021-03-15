# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        output = []
        
        if root is None:
            return output
        
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            currentTotal = 0
            for _ in range(levelSize):
                currentNode = queue.popleft()
                currentTotal += currentNode.val
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            output.append(currentTotal / levelSize)
        
        return output
