class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        def int_to_pos(square):
            r = (square - 1) // n
            c = (square - 1) % n
            if r % 2 != 0:
                c = n - 1 - c
            return (r, c)
        queue = collections.deque([(1, 0)]) # square, moves
        visited = {(1, 0)}
        while queue:
            square, moves = queue.popleft()
            for i in range(1, 7):
                next_square = square + i
                r, c = int_to_pos(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == n * n:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        return -1