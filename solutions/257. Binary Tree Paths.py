# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        output = []
        self.findPath(root, "", output)
        return output
        
    def findPath(self, currentNode, currentPath, allPaths):
        if currentNode is None:
            return
        
        currentPath = currentPath + str(currentNode.val) + "->"        
        
        if currentNode.left is None and currentNode.right is None:
            allPaths.append(currentPath[0: len(currentPath) - 2])
            
        else:
            self.findPath(currentNode.left, currentPath, allPaths)
            self.findPath(currentNode.right, currentPath, allPaths)
        
        
