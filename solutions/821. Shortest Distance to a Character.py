class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        position = []
        for key,value in enumerate(S):
            if value == C:
                position.append(key)
        
        output = []        
        for key,value in enumerate(S):
            print(min(list(map(lambda x:abs(x-key) ,position))))
            output.append(min(list(map(lambda x:abs(x-key) ,position))))
        
        return output
