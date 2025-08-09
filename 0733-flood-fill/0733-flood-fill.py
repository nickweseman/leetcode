class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(image), len(image[0])
        flood_color = image[sr][sc]
        if flood_color == color:
            return image
        queue = collections.deque([(sr, sc)])
        visited = {(sr, sc)}
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                image[r][c] = color
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in visited or image[nr][nc] != flood_color:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return image