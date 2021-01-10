class Solution:
    def calPoints(self, ops: List[str]) -> int:
        output = []
        score = 0
        for op in ops:
            if op == "C":
                output.pop()
            elif op == "D":
                add = str(int(output[-1]) * 2)
                output.append(add)
            elif op == "+":
                add = str(int(output[-1]) + int(output[-2]))
                output.append(add)
            else:
                output.append(op)
        for o in output:
            score += int(o)
        return score
