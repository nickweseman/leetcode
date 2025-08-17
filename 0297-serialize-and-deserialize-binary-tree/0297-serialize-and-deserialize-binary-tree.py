# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        output = []
        def dfs(node):
            if not node:
                output.append("#")
                return
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(output)
    def deserialize(self, data):
        node_iter = iter(data.split(","))
        def dfs():
            val = next(node_iter)
            if val == "#":
                return None
            node = TreeNode(val=val)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()