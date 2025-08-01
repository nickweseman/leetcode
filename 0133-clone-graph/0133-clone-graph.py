"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        def dfs(n):
            if not n:
                return None
            if n in old_to_new:
                return old_to_new[n]
            new = Node(n.val, [])
            old_to_new[n] = new
            for nei in n.neighbors:
                new.neighbors.append(dfs(nei))
            return new
        return dfs(node)