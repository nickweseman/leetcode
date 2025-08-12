class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        queue = collections.deque([(rCenter, cCenter)])
        visited = {(rCenter, cCenter)}
        output = []
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            output.append([r, c])
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in visited:
                    continue
                queue.append((nr, nc))
                visited.add((nr, nc))
        return output
