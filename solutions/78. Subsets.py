class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for num in nums:
            n = len(output)
            for i in range(n):
                currentSet = list(output[i])
                currentSet.append(num)
                output.append(currentSet)
        
        return output
