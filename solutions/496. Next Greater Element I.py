class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        
        for i, n in list(enumerate(nums1)):
            idx = nums2.index(n)
            flag = False
            for i in range(idx, len(nums2)):
                if nums2[i] > n:
                    output.append(nums2[i])
                    flag = True
                    break
            if not flag:
                output.append('-1')
                
        return output
