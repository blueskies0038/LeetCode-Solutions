class Solution:
    def removeDuplicates(self, s: str) -> str:
        end, a = -1, list(s)
        for c in a:
            if end >= 0 and a[end] == c:
                end -= 1
            else:
                end += 1
                a[end] = c
        return ''.join(a[: end + 1])
