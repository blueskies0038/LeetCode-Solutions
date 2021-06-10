class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {(x, y) for x, y in obstacles}
        output = 0
        x, y = 0, 0
        dx, dy = 0, 1
        
        for move in commands:
            if move == -2:
                dx, dy = -dy, dx
            elif move == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(move):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = x + dx, y + dy
                
                output = max(output, x*x + y*y)
                
        return output
