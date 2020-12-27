class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        s = set(A)
        required = {}
        for i in B:
            for j in i:
                count = i.count(j)
                if j not in required or count > required[j]:
                    required[j] = count
​
        for i in A:
            for j in required:
                if i.count(j) < required[j]:
                    s.remove(i)
                    break
        return s
