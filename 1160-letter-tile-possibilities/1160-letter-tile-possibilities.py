class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        path = []
        n = len(tiles)
        used = [False] * n
        def backtrack(index):
            if index == n:
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(tiles[i])
                result.add(tuple(path))
                backtrack(index + 1)
                path.pop()
                used[i] = False
        backtrack(0)
        return len(result)