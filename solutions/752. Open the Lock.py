class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        
        if "0000" in deadends:
            return -1      
        if target == "0000":
            return 0
        
        queue = collections.deque()
        visited = {}
        queue.append(["0000", 0])
        
        while len(queue) > 0:   
            current, level = queue.popleft()            
            new_nums = []       
            
            for i in range(4):
                new_nums.append(current[:i] + str((int(current[i]) + 1) % 10) + current[i+1:])                
                new_nums.append(current[:i] + str((int(current[i]) - 1) % 10) + current[i+1:])
            
            for num in new_nums:
                if num in visited or num in deadends:
                    continue
                visited[num] = True                
                if num == target:
                    return level + 1
                queue.append([num, level + 1])                
       
        return -1
