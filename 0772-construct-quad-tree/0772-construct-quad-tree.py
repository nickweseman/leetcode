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
        def is_uniform(row, col, size) -> bool:
            first = grid[row][col]
            for i in range(row, row + size):
                for j in range(col, col + size):
                    if grid[i][j] != first:
                        return False
            return True
        def create_tree(row, col, size) -> 'Node':
            if is_uniform(row, col, size):
                return Node(val=grid[row][col], isLeaf=True)
            node = Node(val=grid[row][col], isLeaf=False)
            half = size // 2
            node.topLeft = create_tree(row, col, half)
            node.topRight = create_tree(row, col + half, half)
            node.bottomLeft = create_tree(row + half, col, half)
            node.bottomRight = create_tree(row + half, col + half, half)
            return node
        return create_tree(0, 0, len(grid))