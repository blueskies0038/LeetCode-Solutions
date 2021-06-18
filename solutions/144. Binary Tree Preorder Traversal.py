# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output =[]
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        
        return output
