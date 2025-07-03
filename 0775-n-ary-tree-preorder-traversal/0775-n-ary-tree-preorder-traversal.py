"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def dfs(node) -> None:
            if not node:
                return
            stack = [node]
            while stack:
                curr = stack.pop()
                result.append(curr.val)
                for child in reversed(curr.children):
                    stack.append(child)
        dfs(root)
        return result

            
        
        