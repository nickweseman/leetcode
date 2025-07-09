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
        def is_uniform(x, y, size) -> bool:
            first = grid[x][y]
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != first:
                        return False
            return True
        def create_tree(x, y, size) -> 'Node':
            if is_uniform(x, y, size):
                return Node(val=grid[x][y], isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            node = Node(val=True, isLeaf=False)
            half = size // 2
            node.topLeft = create_tree(x, y, half)
            node.topRight = create_tree(x, y + half, half)
            node.bottomLeft = create_tree(x + half, y, half)
            node.bottomRight = create_tree(x + half, y + half, half)
            return node
        return create_tree(0, 0, len(grid))
