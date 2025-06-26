class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        bottom_left, top_right = 0, sum(grid[0])
        lowest_robot_2_score = math.inf

        for col in range(len(grid[0])):
            top_right -= grid[0][col]

            robot_2_score = max(top_right, bottom_left)
            lowest_robot_2_score = min(lowest_robot_2_score, robot_2_score)

            bottom_left += grid[1][col]
        return lowest_robot_2_score