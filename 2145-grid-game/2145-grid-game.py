class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        right_top = sum(grid[0])
        left_bottom = 0
        lowest_robot_2_score = float('inf')

        for col in range(len(grid[0])):
            right_top -= grid[0][col]

            robot2_score = max(right_top, left_bottom)
            lowest_robot_2_score = min(lowest_robot_2_score, robot2_score)

            left_bottom += grid[1][col]
        return lowest_robot_2_score
        
        