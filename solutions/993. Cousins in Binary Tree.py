# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        hm = {}
        def dfs(root, i, p):
            if root:
                if root.val in (x, y): hm[root.val] = (i, p)
                dfs(root.left, i+1, root.val)
                dfs(root.right, i+1, root.val)
        dfs(root, 0, None)
        return hm[x][0] == hm[y][0] and hm[x][1] != hm[y][1]
