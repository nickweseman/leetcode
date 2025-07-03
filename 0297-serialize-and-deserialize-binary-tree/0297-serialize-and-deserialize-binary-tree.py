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
        values_iter = iter(data.split(","))
        def build_tree() -> TreeNode:
            v = next(values_iter)
            if v == "#":
                return
            node = TreeNode(v)
            node.left = build_tree()
            node.right = build_tree()
            return node
        return build_tree()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))