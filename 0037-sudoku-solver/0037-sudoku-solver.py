class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        num_rows, num_cols = len(board), len(board[0])
        empty_positions = []
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == ".":
                    empty_positions.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r//3,c//3)].add(num)
        def backtrack(index):
            if index == len(empty_positions):
                return True
            r, c = empty_positions[index]
            for i in range(1, 10):
                digit = str(i)
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[(r//3,c//3)]:
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[(r//3,c//3)].add(digit)
                    board[r][c] = str(digit)
                    if backtrack(index + 1):
                        return True
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[(r//3,c//3)].remove(digit)
                    board[r][c] = "."
            return False
        backtrack(0)
        