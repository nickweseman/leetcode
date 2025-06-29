class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        bottom_left, top_right = 0, sum(grid[0])
        lowest_robot2_score = math.inf

        for col in range(len(grid[0])):
            top_right -= grid[0][col]

            robot2_score = max(top_right, bottom_left)
            lowest_robot2_score = min(lowest_robot2_score, robot2_score)

            bottom_left += grid[1][col]

        return lowest_robot2_score
