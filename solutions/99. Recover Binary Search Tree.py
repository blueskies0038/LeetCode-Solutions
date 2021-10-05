# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prev = None, None, TreeNode(float('-inf')) 
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            if self.prev.val >= node.val: 
                self.first = self.first or self.prev
                self.second = node
            self.prev = node
            self.inorder(node.right)    
