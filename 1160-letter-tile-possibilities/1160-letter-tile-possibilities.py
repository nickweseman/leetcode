class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        num_possibilities = 0
        path = []
        n = len(tiles)
        my_tiles = list(tiles)
        my_tiles.sort()
        used = [False] * n
        def backtrack(index):
            nonlocal num_possibilities
            if index == n:
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and my_tiles[i] == my_tiles[i - 1] and not used[i - 1]:
                    continue
                num_possibilities += 1
                path.append(my_tiles[i])
                used[i] = True
                backtrack(index + 1)
                path.pop()
                used[i] = False
        backtrack(0)
        return num_possibilities