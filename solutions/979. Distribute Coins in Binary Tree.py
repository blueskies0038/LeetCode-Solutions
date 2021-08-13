# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            (l_bal, l_cnt), (r_bal, r_cnt) = dfs(node.left), dfs(node.right)
            bal = node.val + l_bal + r_bal - 1
            return bal, l_cnt + r_cnt + abs(bal)
        return dfs(root)[1]
