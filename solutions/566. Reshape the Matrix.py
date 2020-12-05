class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r*c:
            return nums
        flat = [n for num in nums for n in num]
        res = []
        for i in range(0, len(flat), c):
            res.append(flat[i:i+c]) 
        return res
