"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            curr = stack.pop()
            for child in curr.children:
                if child:
                    stack.append(child)
            result.append(curr.val)
        return result[::-1]