class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for i in range(k):
            heappush(hp, (self.findDistance(points[i]), points[i]))
            
        for j in range(k, len(points)):
            if self.findDistance(points[j]) > self.findDistance(hp[0][1]):
                heappushpop(hp, (self.findDistance(points[j]), points[j]))
        
        return [heappop(hp)[1] for i in range(k)]
    
    def findDistance(self, point):
        return -(point[0] * point[0] + point[1] * point[1])
