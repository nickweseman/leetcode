# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        path = []
        def dfs(node):
            if not node:
                path.append("#")
                return
            path.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(path)
    def deserialize(self, data):
        tree_iter = iter(data.split(","))
        def dfs():
            val = next(tree_iter)
            if val == "#":
                return None
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))