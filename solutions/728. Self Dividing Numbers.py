class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        isSelfDividing = True
        for i in range(left, right+1):
            if i < 10:
                output.append(i)      
            elif '0' not in str(i):
                for d in str(i):
                    if i % int(d):
                        isSelfDividing = False
                        break
                if isSelfDividing:
                    output.append(i)
            
                isSelfDividing = True
        return output  
