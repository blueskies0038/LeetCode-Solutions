class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        count = num = 0
    
        for i in range(min(k, len(matrix))):
            heappush(minHeap, (matrix[i][0], 0, matrix[i]))
            
        while minHeap:
            num, i, row = heappop(minHeap)
            count += 1
            if count == k:
                break
            if len(row) > i + 1:
                heappush(minHeap, (row[i+1], i+1, row))
        
        return num
