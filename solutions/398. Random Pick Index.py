class Solution:
​
    def __init__(self, nums: List[int]):
        self.nums = nums
​
    def pick(self, target: int) -> int:
        index = [i for i, val in enumerate(self.nums) if val == target]
        return random.choice(index)
                
​
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
