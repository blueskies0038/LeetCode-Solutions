# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        flag = True
        
        if root.left is not None:
            root.left = self.sufficientSubset(root.left, limit - root.val)
            flag = False
            
        if root.right is not None:
            root.right = self.sufficientSubset(root.right, limit - root.val)   
            flag = False
            
        if root.left is None and root.right is None and (root.val < limit or not flag):
            root = None
​
        return root
