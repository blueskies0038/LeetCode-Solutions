class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, triples = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        visited = collections.deque([])
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r // 3, c // 3)].add(board[r][c])
                else:
                    visited.append((r, c))
        def dfs():
            if not visited:
                return True
            r, c = visited[0]
            t = (r // 3, c // 3)
            for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                    board[r][c] = dig
                    rows[r].add(dig)
                    cols[c].add(dig)
                    triples[t].add(dig)
                    visited.popleft()
                    if dfs():
                        return True
                    else:
                        board[r][c] = "."
                        rows[r].discard(dig)
                        cols[c].discard(dig)
                        triples[t].discard(dig)
                        visited.appendleft((r, c))
            return False
        dfs()
