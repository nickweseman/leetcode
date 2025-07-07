# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def get_max_index(left, right) -> int:
            maxx = -math.inf
            max_index = -1
            for i in range(left, right + 1):
                if nums[i] > maxx:
                    maxx = nums[i]
                    max_index = i
            return max_index
        def create_tree(left, right) -> Optional[TreeNode]:
            if left > right:
                return None
            max_i = get_max_index(left, right)
            return TreeNode(val=nums[max_i], left=create_tree(left, max_i - 1), right=create_tree(max_i + 1, right))
        return create_tree(0, len(nums) - 1)