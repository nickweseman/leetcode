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
        def serialize(node) -> str:
            serialized_result = []
            def dfs(n) -> None:
                if not n:
                    serialized_result.append("#")
                    return
                else:
                    serialized_result.append(str(n.val))
                    dfs(n.left)
                    dfs(n.right)
            dfs(node)
            return "," + ",".join(serialized_result) + ","
        
        def dfs(node) -> None:
            if node:
                s = serialize(node)
                subtrees[s] += 1
                if subtrees[s] == 2:
                    result.append(node)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return result
        