class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        output = ""
        current = 'a' if A > B else 'b'
        while A > 0 or B > 0:
            if current == 'a':
                if A > B and A > 1:
                    output += "aa"
                    A -= 2
                else:
                    output += "a"
                    A -= 1
                current = 'b'
            else:
                if B > A and B > 1:
                    output += "bb"
                    B -= 2
                else:
                    output += "b"
                    B -= 1
                current = 'a'
                
        return output
