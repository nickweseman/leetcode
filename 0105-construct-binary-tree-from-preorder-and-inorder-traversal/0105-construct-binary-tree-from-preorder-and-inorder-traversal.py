class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.preorder_index = 0

        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = preorder[self.preorder_index]
            self.preorder_index += 1
            root = TreeNode(root_val)
            inorder_root_index = inorder_map[root_val]

            root.left = array_to_tree(left, inorder_root_index - 1)
            root.right = array_to_tree(inorder_root_index + 1, right)
            return root
        return array_to_tree(0, len(inorder) - 1)