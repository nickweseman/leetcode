class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        bottom_left, top_right = 0, sum(grid[0])
        best_robot2_score = -math.inf
        for c in range(len(grid[0])):
            top_right -= grid[0][c]
            bottom_left += grid[1][c]
            robot2_score = min(top_right, bottom_left)
            best_robot2_score = max(best_robot2_score, robot2_score)
        return best_robot2_score