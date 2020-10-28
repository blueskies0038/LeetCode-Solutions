class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        output = 0
        
        if len(s) == 0:
            return output
        
        g.sort(reverse=True)
        s.sort(reverse=True)
        
        i = 0
        for child in g:
            if s[i] >= child:
                output += 1
                i += 1
                if i == len(s):
                    break
        
        return output
