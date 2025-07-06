# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {num: i for i, num in enumerate(inorder)}
        preorder_index = 0
        def create_tree(left, right) -> Optional[TreeNode]:
            nonlocal preorder_index
            if left > right:
                return None
            node_val = preorder[preorder_index]
            preorder_index += 1
            node = TreeNode(node_val)
            inorder_index = inorder_map[node_val]
            node.left = create_tree(left, inorder_index - 1)
            node.right = create_tree(inorder_index + 1, right)
            return node
        return create_tree(0, len(preorder) - 1)