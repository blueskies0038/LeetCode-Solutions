class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        output = []
        
        if "+" not in input and "-" not in input and "*" not in input:
            output.append(int(input))
        else:
            for i in range(len(input)):
                char = input[i]
                if not char.isdigit():
                    leftPart = self.diffWaysToCompute(input[0:i])
                    rightPart = self.diffWaysToCompute(input[i+1:])
                    for left in leftPart:
                        for right in rightPart:
                            if char == "+":
                                output.append(left + right)
                            elif char == "-":
                                output.append(left - right)
                            elif char == "*":
                                output.append(left * right)
        
        return output
