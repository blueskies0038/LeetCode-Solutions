class Solution:
    def numSquares(self, n: int) -> int:
        queue = deque([(0, 0)])
        visited = set()
        while queue:
            i, step = queue.popleft()
            step += 1
            for j in range(1, n + 1):
                k = i + j * j
                if k > n:
                    break
                if k == n:
                    return step
                if k not in visited:
                    visited.add(k)
                    queue.append((k, step))
