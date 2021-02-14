class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        return len(self.dfs(rooms, [])) == len(rooms)
    
    def dfs(self, rooms, path, source = 0):
        path += [source]
        
        for k in rooms[source]:
            if k not in set(path):
                self.dfs(rooms, path, k)
        return path
