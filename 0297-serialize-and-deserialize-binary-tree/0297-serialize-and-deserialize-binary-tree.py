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
        values = data.split(",")
        values_index = 0
        
        def dfs() -> Optional[TreeNode]:
            nonlocal values_index
            curr = values[values_index]
            values_index += 1
            if curr == "#":
                return None
            node = TreeNode(curr)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

        
        
        
        return TODO