class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        h = {}
        for i in nums1:
            h[i] = h[i]+1 if i in h else 1
        for j in nums2:
            if j in h and h[j] > 0:
                output.append(j)
                h[j] = 0
​
        return output
