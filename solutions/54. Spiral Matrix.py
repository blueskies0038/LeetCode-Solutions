class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        direction = "right"
        output = []
        while top <= bottom and left <= right:
            if direction == "right":
                for i in range(left, right + 1):
                    output.append(matrix[top][i])
                top += 1
                direction = "down"
            elif direction == "down":
                for i in range(top, bottom + 1):
                    output.append(matrix[i][right])
                right -= 1
                direction = "left"
            elif direction == "left":
                for i in range(right, left - 1, -1):
                    output.append(matrix[bottom][i])
                bottom -= 1
                direction = "up"
            else:
                for i in range(bottom, top - 1, -1):
                    output.append(matrix[i][left])
                left += 1
                direction = "right"
        
