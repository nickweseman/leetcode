class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        path = []
        def backtrack(r, c, index):
            if len(path) == len(word):
                return True
            if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in visited or word[index] != board[r][c]:
                return False
            path.append(board[r][c])
            visited.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if backtrack(r + dr, c + dc, index + 1):
                    return True
            visited.remove((r, c))
            path.pop()
            return False
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        return False