class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        square_to_pos = {}
        square = 1
        board.reverse() # make row 0 the bottom
        for r in range(n):
            cols = range(n) if r % 2 == 0 else reversed(range(n))
            for c in cols:
                square_to_pos[square] = (r, c)
                square += 1
        queue = collections.deque([(1, 0)]) # square, moves
        visited = {1}
        while queue:
            square, moves = queue.popleft()
            for i in range(1, 7):
                next_square = square + i
                r, c = square_to_pos[next_square]
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == n * n:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        return -1