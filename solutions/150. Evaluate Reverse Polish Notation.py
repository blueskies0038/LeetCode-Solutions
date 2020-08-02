class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda a,b: a+b,
            "-": lambda a,b: a-b,
            "/": lambda a,b: int(a/b),
            "*": lambda a,b: a*b
        }
​
        for token in tokens:
            if token in operations:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(operations[token](num2, num1))
            else:
                stack.append(int(token))
        return stack[0]
