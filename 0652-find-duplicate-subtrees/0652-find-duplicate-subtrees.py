# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = collections.defaultdict(int)
        result = []

        def dfs(n):
            if not n:
                return
            s = self.serialize(n)
            subtrees[s] += 1
            if subtrees[s] == 2:
                result.append(n)
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return result

    def serialize(self, node) -> str:
        result = []
        def dfs(n) -> None:
            if not n:
                result.append("#")
                return
            else:
                result.append(str(n.val))
                dfs(n.left)
                dfs(n.right)
        dfs(node)
        return "," + ",".join(result) + ","