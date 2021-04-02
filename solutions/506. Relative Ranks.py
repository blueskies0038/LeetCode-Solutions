class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        newNums = sorted(nums,reverse = True)
        dic = {}
        n = len(newNums)
        dic[newNums[0]] = "Gold Medal"
        
        if n > 1:
            dic[newNums[1]] = "Silver Medal"
        if n > 2:
            dic[newNums[2]] = "Bronze Medal"      
        for i in range(3, n):
            dic[newNums[i]] = str(i+1)
        
        return [dic[k] for k in nums]
​
