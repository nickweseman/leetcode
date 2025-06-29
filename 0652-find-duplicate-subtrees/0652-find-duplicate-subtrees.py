# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return []
        subtrees = collections.defaultdict(int)
        result = []
        def dfs(n) -> None:
            if n:
                subtrees[self.serialize(n)] += 1
                if subtrees[self.serialize(n)] == 2:
                    result.append(n)
                dfs(n.left)
                dfs(n.right)
        dfs(root)
        return result
        
    def serialize(self, node) -> str:
        result = []
        def preorder(n) -> None:
            if not n:
                result.append("#")
                return
            result.append(str(n.val))
            preorder(n.left)
            preorder(n.right)
        preorder(node)
        return "," + ",".join(result) + ","

        