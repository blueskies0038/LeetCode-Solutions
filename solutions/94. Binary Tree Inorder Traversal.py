# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.helper(root, output)
        return output
​
    def helper(self, root, arr):
        if root:
            self.helper(root.left, arr)
            arr.append(root.val)
            self.helper(root.right, arr)
