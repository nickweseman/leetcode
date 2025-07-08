# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        imap = {}
        for i, val in enumerate(inorder):
            imap[val] = i
        pre_index = 0
        def create_tree(left, right) -> Optional[TreeNode]:
            nonlocal pre_index
            if left > right:
                return None
            mid_value = preorder[pre_index]
            pre_index += 1
            inorder_index = imap[mid_value]

            node = TreeNode(mid_value)
            node.left = create_tree(left, inorder_index - 1)
            node.right = create_tree(inorder_index + 1, right)
            return node
        return create_tree(0, len(preorder) - 1)