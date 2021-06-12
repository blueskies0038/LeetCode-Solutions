# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.bfs(root1, []) == self.bfs(root2, [])
        
    def bfs(self, root, leaves):
        if root is not None:
            queue = deque()
            queue.append(root)
            
            while queue:
                currentNode = queue.pop()
                if currentNode.left is None and currentNode.right is None:
                    leaves.append(currentNode.val)
                    continue
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        
        return leaves
