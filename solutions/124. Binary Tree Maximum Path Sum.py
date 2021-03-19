# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = -math.inf
        self.dfs(root)
        return self.maxSum
        
    def dfs(self, currentNode):
        if currentNode is None:
            return 0
        
        maxLeftSum = self.dfs(currentNode.left)
        maxRightSum = self.dfs(currentNode.right)
        
        maxLeftSum = max(maxLeftSum, 0)
        maxRightSum = max(maxRightSum, 0)
        
        localMax = maxLeftSum + maxRightSum + currentNode.val
        self.maxSum = max(self.maxSum, localMax)
        
        return max(maxLeftSum, maxRightSum) + currentNode.val
