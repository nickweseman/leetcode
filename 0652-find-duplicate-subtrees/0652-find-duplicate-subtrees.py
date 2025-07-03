# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []
        subtrees = collections.defaultdict(int)
        def dfs(node) -> None:
            if not node:
                return
            s = self.serialize(node)
            subtrees[s] += 1
            if subtrees[s] == 2:
                result.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result
    def serialize(self, root: TreeNode) -> str:
        result = []
        def dfs(node) -> None:
            if not node:
                result.append("#")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return "," + ",".join(result) + ","