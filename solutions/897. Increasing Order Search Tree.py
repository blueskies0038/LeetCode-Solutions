# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[0]
        
    def dfs(self, node):
        l1, r2 = node, node
            
        if node.left: 
            l1, l2 = self.dfs(node.left)
            l2.right = node
            node.left = None
                
        if node.right:
            r1, r2 = self.dfs(node.right)
            node.right = r1
​
        return (l1, r2)
