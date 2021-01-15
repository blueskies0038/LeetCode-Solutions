class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        provs = 0
        length = len(M)
        visited = [False] * length
​
        def dfs(city):
            if visited[city]: return
            visited[city] = True
            for connect, is_connect in enumerate(M[city]):
                if is_connect and not visited[connect]:
                    dfs(connect)
​
        for city in range(length):
            if visited[city]: continue
            provs += 1
            dfs(city)
            
        return provs
