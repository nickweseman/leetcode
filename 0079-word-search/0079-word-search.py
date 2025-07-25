class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def backtrack(r, c, index):
            if len(path) == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[index]:
                return False
            path.append(board[r][c])
            prev = board[r][c]
            board[r][c] = "#"
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, index + 1):
                    return True
            path.pop()
            board[r][c] = prev
            return False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        return False