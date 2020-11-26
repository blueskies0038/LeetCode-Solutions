class Solution:
    def customSortString(self, S: str, T: str) -> str:
        s, t = Counter(S), Counter(T)
        output = ""
        for x in list(s.keys()):
            if x in t.keys():
                output += x * t[x]
        for y in list(t.keys()):
            if y not in s.keys():
                output += y * t[y]
        return output
