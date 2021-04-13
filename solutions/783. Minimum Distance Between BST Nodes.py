# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        return self.dfs(root, -math.inf, math.inf)
        
    def dfs(self, node, low, high):
        if node is None:
            return high - low
        left = self.dfs(node.left, low, node.val)
        right = self.dfs(node.right, node.val, high)
        return min(left, right)
