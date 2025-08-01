class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        result = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visited, prev_height):
            if not (0 <= r < rows and 0 <= c < cols) or heights[r][c] < prev_height or (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        for r in range(rows):
            dfs(r, 0, pacific, 0)
            dfs(r, cols - 1, atlantic, 0)
        for c in range(cols):
            dfs(0, c, pacific, 0)
            dfs(rows - 1, c, atlantic, 0)
        return list(pacific & atlantic)