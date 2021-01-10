class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        temp = ""
        count = 0
        while len(temp) < len(b):
            temp += a
            count += 1
            if b in temp:
                return count
        temp += a
        if b in temp:
            return count + 1
        return -1
