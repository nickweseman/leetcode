class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(mat), len(mat[0])
        queue = collections.deque()
        result = [[-1] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols) or result[nr][nc] != -1:
                    continue
                result[nr][nc] = result[r][c] + 1
                queue.append((nr, nc))
        return result
                    
