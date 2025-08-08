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
        queue = collections.deque([1]) # square
        visited = {1}
        moves = 0
        while queue:
            for _ in range(len(queue)):
                square = queue.popleft()
                if square == n * n:
                    return moves
                for i in range(1, 7):
                    next_square = square + i
                    if next_square > n * n:
                        break # don't overshoot the board
                    r, c = square_to_pos[next_square]
                    if board[r][c] != -1:
                        next_square = board[r][c]
                    if next_square not in visited:
                        visited.add(next_square)
                        queue.append((next_square))
            moves += 1
        return -1