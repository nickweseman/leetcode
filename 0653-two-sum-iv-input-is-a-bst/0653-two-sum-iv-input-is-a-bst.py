# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder_generator(node: Optional[TreeNode]):
            """Yields nodes from smallest to largest."""
            if not node:
                return
            yield from inorder_generator(node.left)
            yield node
            yield from inorder_generator(node.right)

        def reverse_inorder_generator(node: Optional[TreeNode]):
            """Yields nodes from largest to smallest."""
            if not node:
                return
            yield from reverse_inorder_generator(node.right)
            yield node
            yield from reverse_inorder_generator(node.left)

        # Create the two iterators
        gen_l = inorder_generator(root)
        gen_r = reverse_inorder_generator(root)
        
        # Get the first elements
        left_ptr = next(gen_l)
        right_ptr = next(gen_r)
        
        while left_ptr and right_ptr and left_ptr.val < right_ptr.val:
            current_sum = left_ptr.val + right_ptr.val
            
            if current_sum == k:
                return True
            elif current_sum < k:
                left_ptr = next(gen_l) # Get next smallest
            else: # current_sum > k
                right_ptr = next(gen_r) # Get next largest
        
        return False
        