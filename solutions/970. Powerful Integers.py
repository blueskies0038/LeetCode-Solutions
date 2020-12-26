class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        output = set()
        xb = math.ceil(math.log(bound, x)) if x != 1 else 1
        yx = math.ceil(math.log(bound, y)) if y != 1 else 1
        
        for i in range(xb + 1):
            for j in range(yx + 1):
                if x ** i + y ** j <= bound:
                    output.add(x ** i + y ** j)
                else:
                    break
                    
        return output
        
