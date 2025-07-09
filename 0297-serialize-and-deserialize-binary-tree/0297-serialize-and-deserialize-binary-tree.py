# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        result = []
        def dfs(node) -> None:
            if not node:
                result.append("#")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        values = iter(data.split(","))
        def dfs() -> Optional[TreeNode]:
            curr = next(values)
            if curr == "#":
                return None
            node = TreeNode(curr)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()