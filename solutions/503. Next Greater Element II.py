class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = []
        reverse = nums[::-1]
        for num in nums[::-1]:
            while reverse and reverse[-1] <= num:
                reverse.pop()
            if reverse:
                output.append(reverse[-1])
            else:
                output.append(-1)
            reverse.append(num)
        return output[::-1]
