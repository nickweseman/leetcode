class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        n = len(word)
        def backtrack(r, c, index):
            if index == n:
                return True
            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or board[r][c] != word[index]:
                return False
            visited.add((r, c))
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, index + 1):
                    return True
            visited.remove((r, c))
            return False
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False