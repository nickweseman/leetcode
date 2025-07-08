# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root or depth == 1:
            return TreeNode(val, left=root)
        queue = collections.deque([(root, 1)]) # node, curr_depth
        while queue:
            for _ in range(len(queue)):
                curr, curr_depth = queue.popleft()
                if curr_depth == depth - 1:
                    curr.left = TreeNode(val, left=curr.left)
                    curr.right = TreeNode(val, right=curr.right)
                else:
                    if curr.left:
                        queue.append((curr.left, curr_depth + 1))
                    if curr.right:
                        queue.append((curr.right, curr_depth + 1))
        return root
        
        
        