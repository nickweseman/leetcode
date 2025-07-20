from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Create sets to track numbers in each row, col, and 3x3 box
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        empty_positions = []

        # Pre-process the board to populate sets and find empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_positions.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3, c // 3)].add(num)

        def backtrack(k: int):
            if k == len(empty_positions):
                return True
            
            r, c = empty_positions[k]
            box_id = (r // 3, c // 3)

            for digit_char in "123456789":
                # The validation is now a fast O(1) set lookup
                if (digit_char not in rows[r] and
                    digit_char not in cols[c] and
                    digit_char not in boxes[box_id]):
                    
                    # Place
                    board[r][c] = digit_char
                    rows[r].add(digit_char)
                    cols[c].add(digit_char)
                    boxes[box_id].add(digit_char)

                    if backtrack(k + 1):
                        return True
                    
                    # Backtrack
                    board[r][c] = "."
                    rows[r].remove(digit_char)
                    cols[c].remove(digit_char)
                    boxes[box_id].remove(digit_char)
            
            return False

        backtrack(0)