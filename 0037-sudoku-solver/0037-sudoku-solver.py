class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        empty_positions = []
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                if board[r][c] == ".":
                    empty_positions.append((r, c))
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r//3,c//3)].add(board[r][c])
        def backtrack(index):
            if index == len(empty_positions):
                return True
            r, c = empty_positions[index]
            for num in "123456789":
                if num not in rows[r] and num not in cols[c] and num not in boxes[r//3,c//3]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[r//3,c//3].add(num)
                    if backtrack(index + 1):
                        return True
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[r//3,c//3].remove(num)
        backtrack(0)

        