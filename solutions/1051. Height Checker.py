class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = Counter(heights)
        i, output = 1, 0
        
        for h in heights:
            while count[i] == 0:
                i += 1
            if i != h:
                output += 1
            count[i] -= 1
            
        return output
