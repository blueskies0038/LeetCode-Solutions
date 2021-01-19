class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.defaultdict(int)
        
        for num in nums:
            frequency[num] += 1
        
        inverse = collections.defaultdict(list)
        output = []
        
        for key, freq in frequency.items():
            inverse[freq].append(key)
        
        for i in range(len(nums), 0, -1):
            output.extend(inverse[i])
            if len(output) >= k:
                break
                
        return output[:k]
