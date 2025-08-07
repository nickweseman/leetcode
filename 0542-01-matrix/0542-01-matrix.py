class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        result = [[-1] * cols for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    queue.append((r, c))
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols) or result[nr][nc] != -1:
                        continue
                    result[nr][nc] = result[r][c] + 1
                    queue.append((nr, nc))
        return result