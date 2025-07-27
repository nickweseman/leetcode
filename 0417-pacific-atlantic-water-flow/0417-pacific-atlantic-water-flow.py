class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        rows, cols = len(heights), len(heights[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, visited, prev_height):
            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or heights[r][c] < prev_height:
                return
            visited.add((r, c))
            for dr, dc in neighbors:
                dfs(r + dr, c + dc, visited, heights[r][c])
        for r in range(rows):
            dfs(r, 0, pacific, 0)
            dfs(r, cols - 1, atlantic, 0)
        for c in range(cols):
            dfs(0, c, pacific, 0)
            dfs(rows - 1, c, atlantic, 0)
        return list(pacific & atlantic)