# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        
        if root is None:
            return output
        
        queue = deque()
        queue.append(root)
        leftStart = True
        while queue:
            levelSize = len(queue)
            currentLevel = deque()
            for _ in range(levelSize):
                currentNode = queue.popleft()
                if leftStart:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.appendleft(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            output.append(currentLevel)
            leftStart = not leftStart
        
        return output
