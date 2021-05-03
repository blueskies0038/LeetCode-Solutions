# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.output = 0
        self.low = L
        self.high = R
        self.dfs(root)
        return self.output
        
    def dfs(self, node):
        if not node:
            return
        
        if self.low <= node.val <= self.high:
            self.output += node.val
        if node.val > self.low:
            self.dfs(node.left)
        if node.val < self.high:
            self.dfs(node.right)
