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
        def is_uniform(row, col, size):
            first = grid[row][col]
            for i in range(row, row + size):
                for j in range(col, col + size):
                    if grid[i][j] != first:
                        return False
            return True
        def dfs(row, col, size):
            if is_uniform(row, col, size):
                return Node(grid[row][col], True)
            node = Node(grid[row][col], False)
            half = size // 2
            node.topLeft = dfs(row, col, half)
            node.topRight = dfs(row, col + half, half)
            node.bottomLeft = dfs(row + half, col, half)
            node.bottomRight= dfs(row + half, col + half, half)
            return node
        return dfs(0, 0, len(grid))