class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        num_rows, num_cols = len(board), len(board[0])
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        empty_queue = []
        for r in range(num_rows):
            for c in range(num_cols):
                if board[r][c] == ".":
                    empty_queue.append((r, c))
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes[(r//3, c//3)].add(board[r][c])
        def backtrack(index):
            if index == len(empty_queue):
                return True
            r, c = empty_queue[index]
            for i in "123456789":
                if i not in rows[r] and i not in cols[c] and i not in boxes[(r//3, c//3)]:
                    board[r][c] = i
                    rows[r].add(i)
                    cols[c].add(i)
                    boxes[(r//3, c//3)].add(i)
                    if backtrack(index + 1):
                        return True
                    board[r][c] = "."
                    rows[r].remove(i)
                    cols[c].remove(i)
                    boxes[(r//3, c//3)].remove(i)
        backtrack(0)