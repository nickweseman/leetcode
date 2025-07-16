# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def serialize(node):
            result = []
            def dfs(curr):
                if not curr:
                    result.append("#")
                    return
                result.append(str(curr.val))
                dfs(curr.left)
                dfs(curr.right)
            dfs(node)
            return "," + ",".join(result) + ","
        result = []
        subtrees = collections.defaultdict(int)
        def dfs(node):
            if not node:
                return
            s = serialize(node)
            subtrees[s] += 1
            if subtrees[s] == 2:
                result.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result