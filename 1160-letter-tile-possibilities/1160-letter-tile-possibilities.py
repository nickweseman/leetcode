class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        path = []
        result = set()
        used = [False] * n
        def backtrack(index):
            if index == n:
                return
            for i in range(n):
                if used[i]:
                    continue
                path.append(tiles[i])
                result.add(tuple(path))
                used[i] = True
                backtrack(index + 1)
                used[i] = False
                path.pop()
        backtrack(0)
        return len(result)