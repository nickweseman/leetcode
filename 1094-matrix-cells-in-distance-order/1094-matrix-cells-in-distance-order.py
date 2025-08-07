class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result = []
        queue = collections.deque()
        queue.append((rCenter, cCenter))
        visited = {(rCenter, cCenter)}
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                result.append([r, c])
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols) or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return result



        