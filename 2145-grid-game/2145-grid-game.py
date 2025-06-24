class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_row_right_sum = sum(grid[0])
        bottom_row_left_sum = 0
        lowest_score = float('inf')

        for col in range(len(grid[0])):
            top_row_right_sum -= grid[0][col]

            # Robot 2's best choice is max of:
            # - Going all top (what's left on top row)
            # - Going all bottom (what we've seen on bottom row)
            robot2_score = max(top_row_right_sum, bottom_row_left_sum)
            
            # Robot 1 wants to minimize Robot 2's score
            lowest_score = min(lowest_score, robot2_score)

            bottom_row_left_sum += grid[1][col]
        return lowest_score