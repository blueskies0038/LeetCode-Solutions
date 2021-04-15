class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        hashset = []
        for num in A:
            if num in hashset:
                return num
            hashset.append(num)
            
