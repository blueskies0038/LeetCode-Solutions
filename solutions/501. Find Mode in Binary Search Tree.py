# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        hashmap = collections.defaultdict(int)
        output = []
        
        if root is None:
            return output
        
        stack = [root]
        
        while stack:
            currentNode = stack.pop()
            hashmap[currentNode.val] += 1
            if currentNode.left:
                stack.append(currentNode.left)
            if currentNode.right:
                stack.append(currentNode.right)
        
        mode = max(hashmap.values())
        for key in hashmap:
            if hashmap[key] == mode:
                output.append(key)
        
        return output
