# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        level, num, output = 1, 1, 0
        queue = deque([[level, num, root]])
​
        while queue:    
            [currentNum, currentLevel, currentNode] = queue.popleft()
            if currentLevel > level:
                level, num = currentLevel, currentNum
                
            output = max(output, currentNum - num + 1)
            if currentNode.left:
                queue.append([currentNum*2, currentLevel+1, currentNode.left])
            if currentNode.right:
                queue.append([currentNum*2+1, currentLevel+1, currentNode.right])
                
        return output
