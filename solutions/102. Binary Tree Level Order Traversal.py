# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        
        if root is None:
            return output
        
        queue = deque()
        queue.append(root)
        while queue:
            levelNodes = len(queue)
            level = []
            for _ in range(levelNodes):
                currentNode = queue.popleft()
                level.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            output.append(level)
        
        return output
