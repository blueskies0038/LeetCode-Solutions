class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        num_dict = {}
        for c in C:
            for d in D:
                nsum = c + d
                if nsum in num_dict:
                    num_dict[nsum] += 1
                else:
                    num_dict[nsum] = 1
​
        for a in A:
            for b in B:
                target = 0 - (a+b)
                if target in num_dict:
                    count += num_dict[target]
        return count 
