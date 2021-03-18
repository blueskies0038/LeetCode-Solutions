# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)
        
    def dfs(self, currentNode, pathSum):
        if currentNode is None:
            return 0
        
        pathSum = 10 * pathSum + currentNode.val
        
        if currentNode.left is None and currentNode.right is None:
            return pathSum
        
        return self.dfs(currentNode.left, pathSum) + self.dfs(currentNode.right, pathSum)
