class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        P = len(p)
        output = []
        c = Counter(p)
        for i in range(len(s) - P + 1):
            temp = s[i:i+P]
            if c == Counter(temp):
                output.append(i)
        return output
​
