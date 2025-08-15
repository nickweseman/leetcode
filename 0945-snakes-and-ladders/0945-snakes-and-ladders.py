class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        square_to_pos = {}
        rows, cols = len(board), len(board[0])
        square = 1
        for r in range(rows):
            col_order = range(cols) if r % 2 == 0 else reversed(range(cols))
            for c in col_order:
                square_to_pos[square] = r, c
                square += 1
        queue = collections.deque([(1, 0)])
        visited = {1}
        while queue:
            square, turns = queue.popleft()
            if square == rows * cols:
                return turns
            for dice in range(1, 7):
                next_square = square + dice
                if next_square > rows * cols:
                    break
                r, c = square_to_pos[next_square]
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square not in visited:
                    queue.append((next_square, turns + 1))
                    visited.add(next_square)
        return -1