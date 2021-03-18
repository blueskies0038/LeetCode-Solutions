# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        output = []
        self.findPath(root, targetSum, [], output)
        return output
    
    def findPath(self, currentNode, target, currentPath, allPaths):
        if currentNode is None:
            return 
        
        currentPath.append(currentNode.val)
        
        if currentNode.val == target and currentNode.left is None and currentNode.right is None:
            allPaths.append(list(currentPath))
        else:
            self.findPath(currentNode.left, target - currentNode.val, currentPath, allPaths)
            self.findPath(currentNode.right, target - currentNode.val, currentPath, allPaths)
            
        del currentPath[-1]
        
