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
        gen = iter(data.split(","))
        def create_tree() -> TreeNode:
            val = next(gen)
            if val == "#":
                return None
            curr = TreeNode(val=val)
            curr.left = create_tree()
            curr.right = create_tree()
            return curr
        return create_tree()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))