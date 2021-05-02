class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        for word in words:
            if self.isMatch(word, pattern):
                output.append(word)
                
        return output
    
    def isMatch(self, word, pattern):
        if len(word) != len(pattern):
            return False
        
        count = {}
        for w, p in zip(word, pattern):
            if w not in count:
                if p in count.values():
                    return False
                count[w] = p
            elif count[w] != p:
                return False
        
        return True
    
    
