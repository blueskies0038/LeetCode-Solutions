# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        output = []
        
        if root is None:
            return output
    
        queue = deque()
        queue.append(root)
        
        while queue:
            currentMax = -math.inf
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.popleft()
                currentMax = max(currentMax, currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            output.append(currentMax)
        
        return output
