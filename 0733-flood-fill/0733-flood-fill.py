class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(image), len(image[0])
        flood_color = image[sr][sc]
        if flood_color == color:
            return image
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or image[r][c] != flood_color:
                return
            image[r][c] = color
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        dfs(sr, sc)
        return image
        