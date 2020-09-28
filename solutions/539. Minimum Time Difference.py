class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        max_minutes = 24 * 60
        minutes = [0] * max_minutes
        
        for time_point in timePoints:
            time_point = time_point.split(":")
            index = int(time_point[0]) * 60 + int(time_point[1])
            minutes[index] += 1
            if (minutes[index] > 1):
                return 0
            
        output = max_minutes + 2
        start_minutes = None
        last_minutes = None
        
        for i in range(max_minutes):
            if (minutes[i]):
                if (start_minutes == None):
                    start_minutes = i
                else:
                    difference = i - last_minutes
                    if (difference < output):
                        output = difference
                last_minutes = i
                
        difference = max_minutes - last_minutes + start_minutes
        
        if (difference < output):
            return difference
        else:
            return output
