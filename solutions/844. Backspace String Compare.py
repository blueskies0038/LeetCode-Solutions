class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = []
        stack_t = []
        for char in S:
            if char == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(char)
        for char in T:
            if char == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(char)

        return stack_s == stack_t