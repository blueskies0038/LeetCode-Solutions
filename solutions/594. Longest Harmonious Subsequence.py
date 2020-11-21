class Solution:
    def findLHS(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                h[num] += 1
        count = 0
        for key in h:
            if key + 1 in h:
                curr = h[key] + h[key + 1]
                if curr > count:
                    count = curr
        return count
