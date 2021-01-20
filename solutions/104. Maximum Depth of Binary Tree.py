# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [[root, 1]]
        max_depth = 0
        
        while stack:
            curr = stack.pop()
            node = curr[0]
            level = curr[1]
        
            if node.left:
                stack.append([node.left, level + 1])
            
            if node.right:
                stack.append([node.right, level + 1])
                
            max_depth = max(max_depth, level)
            
        return max_depth
