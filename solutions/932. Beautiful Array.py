class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        nums = list(range(1, N+1))
        
        def divide(nums) -> List[int]:
            if len(nums) < 3:
                return nums
            even = nums[::2]
            odd = nums[1::2]
            return divide(even) + divide(odd)
        
        return divide(nums)   
