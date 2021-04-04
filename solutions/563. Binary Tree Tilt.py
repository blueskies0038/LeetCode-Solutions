# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.tilt = 0
        self.dfs(root)
        return self.tilt
        
    def dfs(self, currentNode):
        if not currentNode:
            return 0
        left = self.dfs(currentNode.left)
        right = self.dfs(currentNode.right)
        self.tilt += abs(right - left)
        return left + right + currentNode.val
