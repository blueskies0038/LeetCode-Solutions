class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        
        for x in s:
            if x == "(" or x == "*":
                stack.append(x)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
                
        stack = []        
​
        for x in s[::-1]:
            if x == ")" or x == "*":
                stack.append(x)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
                
        return True
