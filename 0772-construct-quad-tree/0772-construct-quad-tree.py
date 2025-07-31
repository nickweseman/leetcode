"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        rows, cols = len(grid), len(grid[0])
        def is_uniform(r, c, size):
            first = grid[r][c]
            for row in range(r, r + size):
                for col in range(c, c + size):
                    if grid[row][col] != first:
                        return False
            return True
        def dfs(r, c, size):
            if is_uniform(r, c, size):
                return Node(grid[r][c], True)
            node = Node(grid[r][c], False)
            half = size // 2
            node.topLeft = dfs(r, c, half)
            node.bottomLeft = dfs(r + half, c, half)
            node.topRight = dfs(r, c + half, half)
            node.bottomRight = dfs(r + half, c + half, half)
            return node
        return dfs(0, 0, rows)