class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        counter = 0
        numbers = nums1 + nums2
        numbers = sorted(numbers)
        length = len(numbers)
        if length%2 == 0:
            index = length/2
            return (numbers[int(index - 1)] + numbers[int(index)])/2
        else:
            index = (length - 1)/2
            return float(numbers[int(index)])