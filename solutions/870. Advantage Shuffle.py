class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = deque(sorted(nums1, reverse=True))
        nums2 = sorted([(num, i) for i, num in enumerate(nums2)], reverse=True)
        
        output = [-1] * len(nums1) 
        for num, i in nums2:
            if num < nums1[0]:
                output[i] = nums1.popleft()
            else:
                output[i] = nums1.pop()
        
        return output
