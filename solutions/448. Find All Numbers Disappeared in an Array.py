class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr =[0] * len(nums)
        for num in nums:
            arr[num-1] = 1
        output = []
        for i in range(len(arr)):
            if arr[i] == 0:
                output.append(i+1)
        return output
        
