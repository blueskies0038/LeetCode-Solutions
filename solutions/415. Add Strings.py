class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = list(num1), list(num2)
        carry = 0
        output = ""
        while n1 or n2 or carry:
            if n1:
                carry += int(n1.pop())
            if n2:
                carry += int(n2.pop())
            output += str(carry%10)
            carry //= 10
        return output[::-1]
