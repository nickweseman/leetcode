class Codec:
    def serialize(self, root):
        result = []
        def preorder(node) -> None:
            if node:
                result.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                result.append("#")
        preorder(root)
        return ",".join(result)
    def deserialize(self, data) -> TreeNode:
        values = iter(data.split(","))
        
        def build_tree() -> TreeNode:
            val = next(values)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()
            return node
        return build_tree()