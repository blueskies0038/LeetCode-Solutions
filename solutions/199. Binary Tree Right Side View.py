# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        output = []
        if root is None:
            return output
        
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                currentNode = queue.popleft()
                if i == levelSize - 1:
                    output.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        
        return output
