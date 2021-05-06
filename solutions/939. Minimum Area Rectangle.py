class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        output = float('inf')
        seen = set()
        
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    output = min(output, area)
            seen.add((x1, y1))
        
        return 0 if output == float('inf') else output
